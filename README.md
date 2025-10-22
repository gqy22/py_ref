# py_ref - Python 标准项目参照模板# py_ref



[![CI](https://github.com/gqy22/py_ref/actions/workflows/ci.yml/badge.svg)](https://github.com/gqy22/py_ref/actions/workflows/ci.yml)[![CI](https://github.com/gqy22/py_ref/actions/workflows/ci.yml/badge.svg)](https://github.com/gqy22/py_ref/actions/workflows/ci.yml)

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)



**一个生产就绪的 Python 项目参照模板，配置了完整的代码质量工具链和丰富的终端输出。**一个标准的 Python 项目模板，配置了完整的代码质量工具链和丰富的终端输出。



> 💡 **使用说明**: 本项目是一个**参照模板**，你可以直接下载或 fork 这个项目，然后在它的基础上开始你的规范化 Python 开发。所有配置、工具链和最佳实践都已预置，让你专注于业务逻辑而不是项目搭建。## ✨ 特性



## 🎯 项目定位- 📦 使用 [uv](https://github.com/astral-sh/uv) 进行快速的包管理和环境管理

- 🎨 使用 [black](https://github.com/psf/black) 进行代码格式化

py_ref 是一个**可直接使用的项目参照模板**，而不是一个需要安装的 Python 包。它提供了：- 🔤 使用 [isort](https://github.com/PyCQA/isort) 进行导入排序

- ⚡ 使用 [ruff](https://github.com/astral-sh/ruff) 进行快速的代码检查

- ✅ 完整的项目结构和配置- ✅ 使用 [pytest](https://github.com/pytest-dev/pytest) 进行单元测试

- ✅ 现代化的 Python 工具链- 🔍 集成测试覆盖率报告

- ✅ 生产级的代码质量保证- 📝 使用 [rich](https://github.com/Textualize/rich) 提供美观的日志和终端输出

- ✅ 自动化的测试和 CI/CD- 🪝 使用 [pre-commit](https://pre-commit.com/) 进行 Git 提交前检查

- ✅ 详细的中文文档和注释- 🔄 配置 GitHub Actions CI/CD 工作流

- ✅ AI 辅助开发指南- 🚀 自动化发布到 GitHub Release 和 PyPI



## ✨ 核心特性## 📁 项目结构



### 项目管理```

- 📦 **uv** - 极速的 Python 包管理器（比 pip 快 10-100 倍）py_ref/

- 🏗️ **src layout** - 标准的项目结构├── .github/

- 📋 **pyproject.toml** - 现代化的项目配置│   └── workflows/

│       ├── ci.yml           # GitHub Actions CI 配置

### 代码质量│       ├── release.yml      # 自动创建 GitHub Release

- 🎨 **black** - 代码格式化│       └── publish.yml      # 自动发布到 PyPI

- 🔤 **isort** - 导入排序├── src/

- ⚡ **ruff** - 快速的代码检查和修复│   └── py_ref/

- 🪝 **pre-commit** - Git 提交前自动检查│       ├── __init__.py      # 包初始化文件

│       ├── core.py          # 核心功能模块

### 测试与覆盖│       ├── logger.py        # 日志管理模块

- ✅ **pytest** - 强大的测试框架│       └── main.py          # 主入口文件

- 📊 **pytest-cov** - 代码覆盖率报告├── tests/

- 🎯 目标覆盖率 >90%│   ├── conftest.py          # pytest 配置和 fixtures

│   ├── test_core.py         # 核心功能测试

### 日志与输出│   ├── test_logger.py       # 日志模块测试

- 📝 **rich** - 美观的终端输出和日志格式化│   ├── test_main.py         # 主入口测试

- 📁 完善的日志系统（控制台 + 文件）│   └── test_package.py      # 包级别测试

- 🎨 彩色输出、表格、进度条等├── scripts/

│   └── check.py             # 本地检查脚本

### 自动化├── .gitignore               # Git 忽略文件配置

- 🔄 **GitHub Actions CI** - 自动化测试和代码检查├── .pre-commit-config.yaml  # pre-commit 钩子配置

- 🚀 **自动发布** - 基于 tag 自动创建 Release├── .python-version          # Python 版本指定

- 📦 **PyPI 发布** - 自动发布到 PyPI（可选）├── CHANGELOG.md             # 变更日志

├── LICENSE                  # 许可证文件

### 文档与指南├── RELEASE.md               # 发布指南

- 📚 完整的中文文档├── pyproject.toml           # 项目配置和依赖管理

- 🤖 **AI 辅助开发指南** (`docs/prompt.md`)└── README.md                # 项目说明文档

- 📖 快速开始、发布指南等```



## 🚀 快速开始## 🚀 快速开始



### 方法一：直接使用本项目（推荐）### 前置要求



```bash- Python 3.11 或更高版本

# 1. 克隆或下载本项目- [uv](https://github.com/astral-sh/uv) - 快速的 Python 包管理器

git clone https://github.com/gqy22/py_ref.git my-project

cd my-project### 安装 uv



# 2. 删除 git 历史，初始化为你自己的项目```bash

rm -rf .git# macOS/Linux

git initcurl -LsSf https://astral.sh/uv/install.sh | sh

git add .

git commit -m "初始提交: 基于 py_ref 模板"# Windows

powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 3. 修改项目信息

# 编辑 pyproject.toml 中的项目名称、描述、作者等# 或使用 pip

# 编辑 src/py_ref/ 目录名为你的项目名pip install uv

```

# 4. 安装依赖

uv venv### 设置项目

source .venv/bin/activate  # Windows: .venv\Scripts\activate

uv pip install -e ".[dev]"1. **克隆仓库**



# 5. 开始开发！```bash

```git clone https://github.com/gqy22/py_ref.git

cd py_ref

### 方法二：作为模板创建新仓库```



在 GitHub 上点击 "Use this template" 按钮，创建你自己的仓库。2. **创建虚拟环境**



### 前置要求```bash

uv venv

- Python 3.13+```

- [uv](https://github.com/astral-sh/uv) - 安装方法：

3. **激活虚拟环境**

```bash

# macOS/Linux```bash

curl -LsSf https://astral.sh/uv/install.sh | sh# Linux/macOS

source .venv/bin/activate

# Windows

powershell -c "irm https://astral.sh/uv/install.ps1 | iex"# Windows

```.venv\Scripts\activate

```

## 📁 项目结构

4. **安装依赖**

```

py_ref/```bash

├── .github/workflows/      # GitHub Actions 工作流# 安装项目及开发依赖

│   ├── ci.yml             # 持续集成uv pip install -e ".[dev]"

│   ├── release.yml        # 自动创建 Release```

│   └── publish.yml        # 发布到 PyPI

├── docs/                  # 文档目录5. **安装 pre-commit 钩子**

│   ├── prompt.md          # AI 辅助开发指南 ⭐

│   ├── QUICKSTART.md      # 快速开始指南```bash

│   ├── RELEASE.md         # 发布指南pre-commit install

│   └── CHANGELOG.md       # 变更日志```

├── examples/              # 示例代码

│   └── demo.py           # 完整功能演示## 🧪 运行测试

├── src/py_ref/            # 源代码目录

│   ├── __init__.py       # 包初始化```bash

│   ├── core.py           # 核心功能# 运行所有测试

│   ├── logger.py         # 日志模块 ⭐pytest

│   └── main.py           # 主程序

├── tests/                 # 测试目录# 运行测试并显示详细输出

│   ├── test_core.py      # 核心功能测试pytest -v

│   ├── test_logger.py    # 日志模块测试

│   └── test_main.py      # 主程序测试# 运行测试并生成覆盖率报告

├── scripts/pytest --cov=src/py_ref --cov-report=html

│   └── check.py          # 代码质量检查脚本

└── pyproject.toml         # 项目配置 ⭐# 运行特定测试文件

```pytest tests/test_core.py



## 🧪 运行测试# 运行特定测试函数

pytest tests/test_core.py::TestGreet::test_greet_default

```bash```

# 运行所有测试

pytest## 🎨 代码质量检查



# 生成覆盖率报告### 使用 Ruff（推荐）

pytest --cov=src/py_ref --cov-report=html

open htmlcov/index.html```bash

```# 检查代码问题

ruff check .

## 🎨 代码质量检查

# 自动修复可修复的问题

```bashruff check --fix .

# 运行所有检查（推荐）

python scripts/check.py# 检查代码格式

ruff format --check .

# 单独运行各项检查

ruff check .          # 代码检查# 自动格式化代码

ruff check --fix .    # 自动修复ruff format .

black .               # 格式化代码```

isort .               # 排序导入

```### 使用 Black



## 📝 使用日志系统```bash

# 检查代码格式

```pythonblack --check .

from py_ref import logger, console, print_success

# 格式化代码

logger.info("应用程序已启动")black .

print_success("操作成功！")```

console.print("[bold green]成功![/bold green]")

```### 使用 isort



查看示例:```bash

```bash# 检查导入排序

python -m py_ref.main      # 主程序演示isort --check-only .

python examples/demo.py    # 完整功能展示

```# 排序导入

isort .

## 🤖 AI 辅助开发```



本项目提供详细的 AI 辅助开发指南：**[`docs/prompt.md`](docs/prompt.md)**### 运行所有检查



快速提示词模板：```bash

```# 使用自定义脚本

我正在基于 py_ref 项目开发，这是一个 Python 标准项目模板。python scripts/check.py

项目特点：使用 src layout、所有注释和日志使用中文、

black + isort + ruff 代码质量控制、pytest 测试、# 或手动运行 pre-commit

rich 日志输出、uv 包管理、Python 3.13。pre-commit run --all-files

```

请帮我实现 [你的需求]...

```## 🔧 开发工作流



## 🔧 开发工作流1. **创建新功能分支**



1. **创建功能分支** → 2. **编写代码和测试** → 3. **运行质量检查** → 4. **提交代码**```bash

git checkout -b feature/your-feature-name

```bash```

git checkout -b feature/my-feature

# 编写代码...2. **编写代码和测试**

python scripts/check.py

git commit -m "feat: 添加新功能"3. **运行本地检查**

```

```bash

## 🚀 发布流程# 自动格式化代码

black .

```bashisort .

# 1. 更新版本号（__init__.py 和 pyproject.toml）ruff format .

# 2. 更新 docs/CHANGELOG.md

# 3. 创建并推送标签# 运行检查

git tag -a v0.2.0 -m "版本 0.2.0"ruff check .

git push origin v0.2.0pytest

# 4. GitHub Actions 自动完成剩余工作```

```

4. **提交代码**（pre-commit 会自动运行检查）

详细说明: [`docs/RELEASE.md`](docs/RELEASE.md)

```bash

## 📖 文档git add .

git commit -m "Add your feature"

- **[快速开始指南](docs/QUICKSTART.md)** - 5 分钟上手```

- **[AI 辅助开发](docs/prompt.md)** - 如何使用 AI 提升开发效率 ⭐

- **[发布指南](docs/RELEASE.md)** - 如何发布新版本5. **推送并创建 Pull Request**

- **[变更日志](docs/CHANGELOG.md)** - 版本历史

```bash

## 🛠️ 自定义项目git push origin feature/your-feature-name

```

### 重命名项目

```bash## 📝 使用日志模块

mv src/py_ref src/your_project_name

# 更新 pyproject.toml 中的 name, description 等项目包含一个功能完善的日志管理模块，基于 Rich 库提供美观的终端输出和文件日志。

# 更新所有导入语句

```### 基本用法



### 添加新依赖```python

在 `pyproject.toml` 添加依赖后运行:from py_ref import logger, get_logger

```bash

uv pip install -e ".[dev]"# 使用默认 logger

```logger.info("Application started")

logger.warning("This is a warning")

## 💡 最佳实践logger.error("An error occurred")



- ✅ 始终使用虚拟环境# 创建自定义 logger

- ✅ 提交前运行质量检查my_logger = get_logger("my_module")

- ✅ 编写测试（覆盖率 >90%）my_logger.debug("Debug information")

- ✅ 使用中文注释```

- ✅ 使用 Rich 日志

- ✅ 遵循 PEP 8### 高级配置



## 📄 许可证```python

from py_ref.logger import setup_logger

MIT 许可证 - 可自由用于商业项目import logging



## 🔗 相关资源# 创建带自定义配置的 logger

logger = setup_logger(

- [uv](https://github.com/astral-sh/uv) | [Ruff](https://docs.astral.sh/ruff/) | [Black](https://black.readthedocs.io/)    name="my_app",

- [pytest](https://docs.pytest.org/) | [Rich](https://rich.readthedocs.io/) | [pre-commit](https://pre-commit.com/)    level=logging.DEBUG,

    log_to_file=True,

## ❓ 常见问题    log_dir=Path("logs"),

    log_file="app.log"

**Q: 为什么选择 uv?**  )

A: 速度极快（10-100倍），兼容 pip。```



**Q: 可以用于商业项目吗?**  ### Rich 格式化输出

A: 可以！MIT 许可证允许商业使用。

```python

## 📊 项目统计from py_ref import (

    console,

- 代码行数: ~1500+    print_success,

- 测试用例: 34 个    print_error,

- 代码覆盖率: 94%    print_warning,

- 质量检查: 全部通过 ✅    print_info,

    print_header

---)



<div align="center"># 使用便捷函数

print_success("Operation completed successfully!")

**用 py_ref 开始你的规范化 Python 之旅！** 🚀print_error("Something went wrong")

print_warning("Be careful!")

[快速开始](docs/QUICKSTART.md) | [AI 开发指南](docs/prompt.md) | [查看示例](examples/demo.py)print_info("For your information")

print_header("Section Title")

</div>

# 使用 rich console
from rich.table import Table

table = Table(title="Results")
table.add_column("Name", style="cyan")
table.add_column("Value", style="green")
table.add_row("Status", "✓ Success")
console.print(table)
```

### 运行示例程序

```bash
# 查看所有功能演示
python -m py_ref.main
```

这将展示：
- 基本功能演示
- Rich 格式化表格
- 日志系统演示

日志文件会自动保存到 `logs/py_ref.log`。

## 📝 配置说明

### pyproject.toml

项目的核心配置文件，包含：

- 项目元数据（名称、版本、作者等）
- 依赖声明
- 工具配置（black、isort、ruff、pytest）

### .pre-commit-config.yaml

定义了提交前自动运行的检查：

- trailing-whitespace：移除行尾空白
- end-of-file-fixer：确保文件以换行符结尾
- check-yaml/json/toml：验证配置文件格式
- black：代码格式化
- isort：导入排序
- ruff：代码质量检查

### GitHub Actions CI

`.github/workflows/ci.yml` 定义了自动化的 CI 流程：

- 在多个 Python 版本上运行测试（3.11、3.12）
- 运行所有代码质量检查
- 生成测试覆盖率报告
- 自动在每次 push 和 PR 时执行

## 🛠️ 使用 uv 的优势

- ⚡ **极快的速度**：比 pip 快 10-100 倍
- 🔒 **可靠的依赖解析**：使用先进的 SAT 求解器
- 🎯 **简单易用**：与 pip 命令兼容
- 📦 **内置虚拟环境管理**：不需要额外的 virtualenv 工具
- 🔄 **lockfile 支持**：确保可重复的构建

### 常用 uv 命令

```bash
# 创建虚拟环境
uv venv

# 安装包
uv pip install package-name

# 安装项目（可编辑模式）
uv pip install -e .

# 安装项目及开发依赖
uv pip install -e ".[dev]"

# 卸载包
uv pip uninstall package-name

# 列出已安装的包
uv pip list

# 导出依赖（类似 pip freeze）
uv pip freeze > requirements.txt

# 从 requirements.txt 安装
uv pip install -r requirements.txt
```

## 📚 扩展项目

### 添加新模块

1. 在 `src/py_ref/` 下创建新的 Python 文件
2. 在 `tests/` 下创建对应的测试文件
3. 在 `src/py_ref/__init__.py` 中导出需要公开的 API

### 添加新依赖

1. 编辑 `pyproject.toml`，在 `dependencies` 中添加包名和版本
2. 运行 `uv pip install -e ".[dev]"` 重新安装

示例：

```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]
```

### 配置新的代码检查规则

在 `pyproject.toml` 中调整 `[tool.ruff.lint]` 部分：

```toml
[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
]
```

## 🚀 发布流程

本项目支持自动化发布到 GitHub Release 和 PyPI。

### 自动发布（推荐）

当推送带有版本标签的提交时，会自动触发发布流程：

```bash
# 1. 更新版本号
# 编辑 src/py_ref/__init__.py 和 pyproject.toml 中的 version

# 2. 提交更改
git add .
git commit -m "chore: bump version to 0.2.0"
git push origin main

# 3. 创建并推送标签
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

自动化流程将：
1. ✅ 运行所有测试和代码检查
2. 📦 构建分发包（wheel 和 sdist）
3. 📝 生成 changelog
4. 🎉 创建 GitHub Release
5. 🚀 发布到 PyPI 和 TestPyPI

### GitHub Actions 工作流

项目包含三个主要的 CI/CD 工作流：

#### 1. CI (`ci.yml`)
- 在每次 push 和 PR 时运行
- 多 Python 版本测试（3.11、3.12）
- 运行所有 linting 和格式检查
- 生成测试覆盖率报告

#### 2. Release (`release.yml`)
- 检测到版本标签时触发
- 创建 GitHub Release
- 附加分发包到 Release

#### 3. Publish (`publish.yml`)
- 检测到版本标签时触发
- 验证版本一致性
- 发布到 TestPyPI（测试）
- 发布到 PyPI（生产）

### PyPI 发布配置

推荐使用 **Trusted Publishing**（无需 API token）：

1. 访问 [PyPI Trusted Publishers](https://pypi.org/manage/account/publishing/)
2. 添加发布者：
   - PyPI Project Name: `py-ref`
   - Owner: `gqy22`
   - Repository: `py_ref`
   - Workflow: `publish.yml`
   - Environment: `pypi`

详细的发布指南请参阅 [RELEASE.md](RELEASE.md)。

### 版本号规范

遵循 [语义化版本](https://semver.org/)：

- **MAJOR.MINOR.PATCH** (例如：1.2.3)
  - **MAJOR**: 不兼容的 API 变更
  - **MINOR**: 向后兼容的新功能
  - **PATCH**: 向后兼容的问题修复

示例：
- `v0.1.0` → `v0.1.1`: 修复 bug
- `v0.1.1` → `v0.2.0`: 新功能
- `v0.2.0` → `v1.0.0`: 重大变更或稳定版本

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🔗 相关资源

- [uv 文档](https://github.com/astral-sh/uv)
- [Ruff 文档](https://docs.astral.sh/ruff/)
- [Black 文档](https://black.readthedocs.io/)
- [isort 文档](https://pycqa.github.io/isort/)
- [pytest 文档](https://docs.pytest.org/)
- [pre-commit 文档](https://pre-commit.com/)
- [Rich 文档](https://rich.readthedocs.io/)

## 💡 提示

- 使用 `uv` 代替 `pip` 可以获得更快的安装速度
- `ruff` 集成了多个 linter 的功能，可以替代 flake8、pylint 等
- 定期运行 `pre-commit autoupdate` 更新钩子版本
- 在 CI 中使用缓存可以加快构建速度
- 日志文件自动保存在 `logs/` 目录
- 使用 `rich` 让终端输出更美观

## 📚 文档

- [CHANGELOG.md](CHANGELOG.md) - 变更日志
- [RELEASE.md](RELEASE.md) - 详细的发布指南
- [LICENSE](LICENSE) - MIT 许可证

---

**祝你编码愉快！** 🎉
