# Third-party notices

AI Study Clipper uses the following unmodified third-party libraries. Original license files are preserved in `third-party-licenses/`. The application's original framework and the changes in this delivery are provided separately from these libraries.

| Component | Verified version | Upstream source |
| --- | --- | --- |
| CPython | 3.12.14 | https://github.com/python/cpython/tree/v3.12.14 |
| Qt / PySide6 / Shiboken | 6.11.2 | https://code.qt.io/cgit/qt/qtbase.git/tree/?h=v6.11.2 and https://code.qt.io/cgit/pyside/pyside-setup.git/ |
| pynput | 1.8.2 | https://github.com/moses-palmer/pynput |
| pywin32 | 312 | https://github.com/mhammond/pywin32 |
| Beautiful Soup | 4.15.0 | https://www.crummy.com/software/BeautifulSoup/ |
| markdownify | 1.2.3 | https://github.com/matthewwithanm/python-markdownify |
| soupsieve | 2.10 | https://github.com/facelessuser/soupsieve |
| six | 1.17.0 | https://github.com/benjaminp/six |
| typing_extensions | 4.16.0 | https://github.com/python/typing_extensions |
| PyInstaller bootloader | 6.22.3 | https://github.com/pyinstaller/pyinstaller |

Qt/PySide6/Shiboken and pynput are used under their LGPL terms. The included LGPL-3.0-only and GPL-3.0-only texts accompany the respective library notices. Qt's third-party acknowledgments are also provided as `Qt-6.11-third-party-notices.html`.

This release selects Qt's bundled FreeType font renderer on Windows. Its acknowledgment and license are included in `Qt-6.11-third-party-notices.html`. Windows fonts are read from the user's system and are not redistributed in this package.

The Windows distribution uses shared DLLs in `_internal`. Compatible modified versions of those libraries may be substituted. Reverse engineering for debugging modifications to LGPL-covered libraries is permitted. The application source and the reproducible build specification are delivered in the companion source archive.

Development-only tools and testing dependencies also have their original notices preserved where supplied by their installed distributions. They are not required by the running desktop application.

## latex2mathml 3.78.1

MIT license. Offline TeX-to-MathML conversion; original license included in third-party-licenses. Project: https://github.com/roniemartinez/latex2mathml
