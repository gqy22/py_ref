"""py_ref - Python 标准项目参照模板"""

__version__ = "0.1.0"

from .core import add, greet
from .logger import (
    console,
    get_logger,
    logger,
    print_error,
    print_header,
    print_info,
    print_section,
    print_success,
    print_warning,
    setup_logger,
)

# API 模块作为可选导入（需要安装 fastapi）
try:
    from .api import app as api_app
except ImportError:
    api_app = None

__all__ = [
    "greet",
    "add",
    "__version__",
    "logger",
    "get_logger",
    "setup_logger",
    "console",
    "print_success",
    "print_error",
    "print_warning",
    "print_info",
    "print_header",
    "print_section",
    "api_app",
]
