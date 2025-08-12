"""
pkgbar package - Internal package for bar functionality
"""

from .__version__ import __version__

def bar() -> str:
    """
    Execute bar functionality using pkgfoo.

    Returns:
        str: Result from calling foo function with 'bar' parameter
    """
    from pkgfoo import foo
    return foo("bar")