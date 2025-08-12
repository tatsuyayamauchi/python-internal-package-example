"""
pkgfoo package - Internal package for foo functionality
"""

from .__version__ import __version__

def foo(val: str) -> str:
    """
    Process a string value and return a formatted result.

    Args:
        val (str): Input string value

    Returns:
        str: Formatted string with 'foo:' prefix
    """
    return f"foo: {val}"
