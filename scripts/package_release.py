"""Package a verified existing Windows bundle without local user data."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_files(bundle):
    manifest = json.loads((bundle / "app-manifest.json").read_text(encoding="utf-8"))
    if manifest.get("app_id") != "AIStudyClipper" or manifest.get("format") != 1:
        raise ValueError("Unsupported application manifest")
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Manifest file list is empty or invalid")
    result = []
    seen = set()
    for entry in entries:
        name = entry["path"]
        relative = PurePosixPath(name)
        if (relative.is_absolute() or "\\" in name or ":" in name
                or ".." in relative.parts or not relative.parts):
            raise ValueError("Unsafe manifest path: " + name)
        folded = name.casefold()
        if folded in seen:
            raise ValueError("Duplicate manifest path: " + name)
        seen.add(folded)
        if any(part.casefold() in {"data", "学习笔记", ".study-clipper-trash",
                                  ".git", ".env", "__pycache__"}
               for part in relative.parts):
            raise ValueError("User data or generated file in manifest: " + name)
        file_path = bundle.joinpath(*relative.parts).resolve()
        try:
            file_path.relative_to(bundle)
        except ValueError:
            raise ValueError("Manifest path escapes bundle: " + name) from None
        if not file_path.is_file():
            raise ValueError("Missing bundle file: " + name)
        if sha256_file(file_path) != entry["sha256"].lower():
            raise ValueError("SHA-256 mismatch: " + name)
        result.append((name, file_path))
    if "aistudyclipper.exe" not in seen:
        raise ValueError("Application executable is absent from manifest")
    result.append(("app-manifest.json", bundle / "app-manifest.json"))
    return sorted(result)


def add_file(archive, name, path):
    # Fixed timestamps and ordering make repeated packages reproducible.
    info = zipfile.ZipInfo(name, date_time=(2026, 10, 8, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, path.read_bytes(), compresslevel=9)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("artifacts"))
    args = parser.parse_args()
    bundle = args.bundle.resolve()
    files = manifest_files(bundle)
    output = args.output.resolve()
    if output == bundle or bundle in output.parents:
        raise ValueError("Output directory must be outside the original bundle")
    output.mkdir(parents=True, exist_ok=True)
    target = output / "AIStudyClipper_0.12_Windows.zip"
    root = Path(__file__).resolve().parents[1]
    prefix = "AIStudyClipper_0.12_Windows/"
    with zipfile.ZipFile(target, "w") as archive:
        for name, file_path in files:
            add_file(archive, prefix + name, file_path)
        for name in ("README.md", "LICENSE"):
            add_file(archive, prefix + name, root / name)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        for name, file_path in files:
            if hashlib.sha256(archive.read(prefix + name)).hexdigest() != sha256_file(file_path):
                raise ValueError("Packaged content differs: " + name)
    digest = sha256_file(target)
    (output / "SHA256SUMS.txt").write_text(
        digest + "  " + target.name + "\n", encoding="utf-8")
    print(f"Verified {len(files) - 1} manifest entries; packaged {len(files) + 2} files")
    print(f"ZIP: {target} ({target.stat().st_size:,} bytes)")
    print("SHA-256: " + digest)


if __name__ == "__main__":
    main()
