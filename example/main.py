"""
Example application demonstrating usage of internal packages pkgfoo and pkgbar
"""

from pkgfoo import foo
from pkgbar import bar

def main():
    """Main function demonstrating package usage"""
    print("=== Python Internal Package Example ===")

    # Test pkgfoo directly
    print("\n1. Testing pkgfoo.foo() function:")
    result1 = foo("hello")
    print(f"   foo('hello') -> {result1}")

    result2 = foo("world")
    print(f"   foo('world') -> {result2}")

    # Test pkgbar (which internally uses pkgfoo)
    print("\n2. Testing pkgbar.bar() function:")
    result3 = bar()
    print(f"   bar() -> {result3}")

    print("\n=== Example completed successfully ===")

if __name__ == "__main__":
    main()