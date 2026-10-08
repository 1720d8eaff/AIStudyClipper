# Study Clipper

面向 Windows 的学习摘录与 Markdown 笔记工具：从其他窗口摘录内容，整理到多层笔记本中，再用阅读、分屏、导图和 PDF 导出复习。

**当前发行版：0.12.0。** [下载 Windows 完整包](https://github.com/1720d8eaff/AIStudyClipper/releases/latest) · [更新说明](docs/CHANGELOG-0.12.md) · [第三方许可](docs/THIRD_PARTY_NOTICES.md)

> 本仓库当前公开的是 Windows 发行包、使用文档和开源打包工具。现有交付目录不包含 0.12 版应用源码；第三方说明提及的配套源码归档尚未提供。因此当前无法从本仓库构建应用，也不能将 EXE 的公开下载等同于应用源码开源。后续补齐源码、应用许可证和构建说明后再更新此说明。

## 功能

- **全局摘录**：在 GPT 等窗口选中文字，按 `Ctrl+Shift+S` 并松开，将内容追加到笔记；也可复制后点击“摘录剪贴板”。
- **Markdown 笔记**：编辑、阅读、分屏切换，支持常见公式与表格，输入自动保存。
- **笔记本整理**：多层笔记本、拖动归档、移动、改名，以及文档和笔记本删除。
- **导图复习**：通过导图节点关联并打开文档。
- **沉浸阅读**：`F11` 进入宽屏阅读，`Esc` 或 `F11` 返回。
- **PDF 导出**：导出当前文档，A4 页面与页码，支持常见公式。
- **桌面使用**：窗口置顶、托盘驻留、可设置摘录快捷键，管理已验证的旧版本。

功能来自随附的 0.12 版使用说明；本仓库发布检查验证了文件完整性和打包内容，未重新执行原应用的功能测试。

## 安装与启动

1. 从 [Releases](https://github.com/1720d8eaff/AIStudyClipper/releases) 下载 `AIStudyClipper_0.12_Windows.zip`，**完整解压**到本机目录。
2. 如正在运行旧版，先通过系统托盘退出。
3. 在 Windows 资源管理器中双击 `安装并启动.cmd`。`正常启动.cmd` 也可作为启动入口。
4. 按提示选择笔记目录。若识别到已核实旧版配置，会尝试沿用原目录。

安装位置为当前用户的 `%LOCALAPPDATA%\Programs\StudyClipper\0.12.0`。运行发行包无需单独安装 Python，也无需管理员权限。请保留 `AIStudyClipper.exe`、`_internal/`、`third-party-licenses/` 和 `app-manifest.json` 的相对位置。

发布 ZIP 不附带个人学习笔记或 `data/config.json`。应用运行后的笔记及本机设置由使用者自行保存和备份。

## 快捷键

| 快捷键 | 操作 |
| --- | --- |
| `Ctrl+Shift+S` | 全局摘录，默认组合，可在设置中修改 |
| `Ctrl+S` | 立即保存当前文档并反馈结果 |
| `Ctrl+N` | 新建文档 |
| `Ctrl+Shift+N` | 新建笔记本 |
| `F2` | 改名 |
| `Ctrl+1` / `2` / `3` / `4` | 编辑 / 阅读 / 分屏 / 导图 |
| `F11` | 切换沉浸阅读 |
| `Esc` | 退出沉浸阅读 |
| `Ctrl+Shift+P` | 导出当前文档为 PDF |

## 笔记与删除行为

笔记保存在选择的本机笔记空间，编辑会自动保存。新摘录只追加正文，不自动添加来源、时间或末尾横线。

右键左侧条目可删除文档或笔记本。**单个文档直接删除**；整本笔记本移入笔记空间下的 `.study-clipper-trash/`，可手动恢复。回收目录仍占用磁盘空间。关闭主窗口会隐藏到托盘，需要通过托盘菜单“退出”才能结束程序。

## 常见问题

**摘录快捷键没有响应？** 检查设置中的注册提示，尝试其他组合，或复制后点击“摘录剪贴板”。全局摘录受 Windows 窗口权限影响；请从普通桌面的资源管理器启动。`Fn` 由硬件控制，无法通用注册。

**Windows 显示发布者或信誉提示？** 当前程序未附可信发布者签名。请核对下载来源和 Release 中的 SHA-256 文件，并按本机策略判断是否运行。

**公式导出与完整 LaTeX 不一致？** 公式转换离线进行，支持常见表达式，并非完整 TeX 编译器。

**如何卸载？** 使用设置底部“管理与卸载版本”，检索并选择已验证版本。随附说明表示该功能保留笔记及额外文件；操作前仍建议自行备份。

## 仓库结构

```text
README.md                     项目介绍和使用指南
LICENSE                       本仓库新增文档及打包工具的 MIT 许可证
docs/                         原始使用说明、更新说明和第三方声明
third-party-licenses/         随发行包提供的第三方许可证
scripts/package_release.py    校验发行清单并生成干净的 ZIP
artifacts/                    本地生成的发行文件，不进入 Git
AIStudyClipper_0.12_Windows/   本机原始发行目录，不进入 Git
```

应用与运行库通过 Release ZIP 分发，避免把二进制和本机数据纳入 Git 历史。

## 制作发行包

以下命令只重新打包已有 Windows 发行目录，**不编译应用**。打包工具仅使用 Python 标准库，Python 3.9 或更新版本即可：

```powershell
python scripts/package_release.py --bundle AIStudyClipper_0.12_Windows --output artifacts
```

工具按 `app-manifest.json` 的明确清单取文件，逐个核对 SHA-256，拒绝路径越界及用户数据，生成 ZIP 和 `SHA256SUMS.txt`。不修改原始发行目录。

在 PowerShell 中校验下载文件：

```powershell
Get-FileHash .\AIStudyClipper_0.12_Windows.zip -Algorithm SHA256
```

将结果与同一 Release 的 `SHA256SUMS.txt` 对照。

## 许可证与贡献

本次新增的仓库文档和打包脚本使用 [MIT License](LICENSE)。该许可证不重新授权已有应用二进制、原始交付文档或第三方组件。**应用本身的许可证尚未随当前目录提供**，在补齐源码和授权文件前，不声明应用已完整开源。

第三方库保留原许可证，详见 [THIRD_PARTY_NOTICES](docs/THIRD_PARTY_NOTICES.md) 与 [third-party-licenses](third-party-licenses/)。原声明列出的部分版本与当前包文件名存在差异，引用该声明不表示重新核定了依赖版本。

欢迎通过 [Issues](https://github.com/1720d8eaff/AIStudyClipper/issues) 反馈问题、完善文档和改进打包工具。应用功能修改需要先补齐对应源码。提交日志或截图前请移除个人笔记、路径及其他隐私信息。
