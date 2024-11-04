# Калькулятор на сложение


def add(x, y):
    """
    Returns the sum of two numbers.

    Parameters:
    x (int or float): The first number to be added.
    y (int or float): The second number to be added.

    Returns:
    int or float: The sum of x and y.
    """
    return x + y


def subtract(x, y):
    """
    Returns the difference of two numbers.

    Parameters:
    x (int or float): The first number to be subtracted.
    y (int or float): The second number to be subtracted.

    Returns:
    int or float: The difference of x and y.
    """
    return x - y


def multiply(x, y):
    """
    Returns the product of two numbers.

    Parameters:
    x (int or float): The first number to be multiplied.
    y (int or float): The second number to be multiplied.

    Returns:
    int or float: The product of x and y.
    """
    return x * y


def divide(x, y):
    """
    Returns the quotient of two numbers.

    Parameters:
    x (int or float): The dividend.
    y (int or float): The divisor.

    Returns:
    int or float: The quotient of x and y.
    """
    return x / y


def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))


if __name__ == "__main__":
    main()
