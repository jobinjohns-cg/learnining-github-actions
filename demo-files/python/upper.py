import sys


def to_uppercase(input_string):
    """
    Convert a given string to uppercase.

    Parameters:
    input_string (str): The string to be converted.

    Returns:
    str: The uppercase version of the input string.
    """
    return input_string.upper()


# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upper.py <string>")
        sys.exit(1)

    sample_string = sys.argv[1]
    print(to_uppercase(sample_string))  # Output: HELLO WORLD
