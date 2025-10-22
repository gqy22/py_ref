"""
日志模块 - 提供 Rich 格式化支持

本模块提供完整的日志系统：
- Rich 格式化的控制台输出
- 文件日志记录（支持自定义路径）
- 多种日志级别
- 结构化日志支持
"""

import logging
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install as install_rich_traceback

# 安装 rich traceback 处理器以获得更好的错误显示
install_rich_traceback(show_locals=True)

# 创建 rich 控制台用于直接输出
console = Console()


class LoggerConfig:
    """日志系统配置类"""

    DEFAULT_LOG_DIR = Path("logs")
    DEFAULT_LOG_FILE = "py_ref.log"
    DEFAULT_LEVEL = logging.INFO
    DEFAULT_FORMAT = "%(message)s"
    FILE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def setup_logger(
    name: str = "py_ref",
    level: int = LoggerConfig.DEFAULT_LEVEL,
    log_to_file: bool = True,
    log_dir: Optional[Path] = None,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """
    设置带有 Rich 格式化和可选文件输出的日志记录器

    参数:
        name: 日志记录器名称
        level: 日志级别 (例如: logging.INFO, logging.DEBUG)
        log_to_file: 是否记录到文件
        log_dir: 日志文件目录，默认为 'logs/'
        log_file: 日志文件名，默认为 'py_ref.log'

    返回:
        配置好的日志记录器实例

    示例:
        >>> logger = setup_logger("my_module", level=logging.DEBUG)
        >>> logger.info("应用程序已启动")
        >>> logger.debug("调试信息")
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 移除现有处理器以避免重复
    logger.handlers.clear()

    # Rich 控制台处理器
    console_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        markup=True,
    )
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(LoggerConfig.DEFAULT_FORMAT))
    logger.addHandler(console_handler)

    # 文件处理器
    if log_to_file:
        log_dir = log_dir or LoggerConfig.DEFAULT_LOG_DIR
        log_file = log_file or LoggerConfig.DEFAULT_LOG_FILE
        log_path = log_dir / log_file

        # 如果日志目录不存在则创建
        log_dir.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter(LoggerConfig.FILE_FORMAT))
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str = "py_ref") -> logging.Logger:
    """
    获取或创建日志记录器实例

    参数:
        name: 日志记录器名称

    返回:
        日志记录器实例

    示例:
        >>> logger = get_logger(__name__)
        >>> logger.info("模块已加载")
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name)
    return logger


# 默认日志记录器实例
logger = setup_logger()


# 便捷的日志记录函数
def debug(message: str, **kwargs) -> None:
    """记录调试消息"""
    logger.debug(message, **kwargs)


def info(message: str, **kwargs) -> None:
    """记录信息消息"""
    logger.info(message, **kwargs)


def warning(message: str, **kwargs) -> None:
    """记录警告消息"""
    logger.warning(message, **kwargs)


def error(message: str, **kwargs) -> None:
    """记录错误消息"""
    logger.error(message, **kwargs)


def critical(message: str, **kwargs) -> None:
    """记录严重错误消息"""
    logger.critical(message, **kwargs)


# Rich 控制台函数，用于增强输出
def print_success(message: str) -> None:
    """打印成功消息（Rich 格式化）"""
    console.print(f"[bold green]✓[/bold green] {message}")


def print_error(message: str) -> None:
    """打印错误消息（Rich 格式化）"""
    console.print(f"[bold red]✗[/bold red] {message}")


def print_warning(message: str) -> None:
    """打印警告消息（Rich 格式化）"""
    console.print(f"[bold yellow]⚠[/bold yellow] {message}")


def print_info(message: str) -> None:
    """打印信息消息（Rich 格式化）"""
    console.print(f"[bold blue]ℹ[/bold blue] {message}")


def print_header(message: str) -> None:
    """打印标题消息（Rich 格式化）"""
    console.print(f"\n[bold cyan]{message}[/bold cyan]")
    console.print("[cyan]" + "=" * len(message) + "[/cyan]")


def print_section(message: str) -> None:
    """打印章节标题（Rich 格式化）"""
    console.print(f"\n[bold]{message}[/bold]")
