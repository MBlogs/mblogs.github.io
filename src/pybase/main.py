def myprint(out: str="Hello, World!") -> None: 
    """
    Print a message to the console.

    Args:
        out (str): The message to print. Defaults to "Hello, World!".

    Returns:
        None

    Examples:
        >>> main()
        Hello, World!

        >>> main("Custom Output")
        Custom Output
    """
    print(out)

if __name__ == "__main__":
    myprint()