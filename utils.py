"""Calculator."""


def add(a: int, b: int) -> int:
    """Function sums two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Function minue two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Function multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Function divide two numbers."""
    return a / b

def binary(a: int) -> str:
    """Function binary from number."""
    res = ''
    while a > 0:
        res = str(a % 2) + res
        a //= 2
    return res