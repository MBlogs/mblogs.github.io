def main(param: str = "") -> None:
    """Example main fuction for a Python project.

    Args:
        param (str): A greeting parameter to customize the output.

    Returns:
        None

    Examples:
        >>> main("Welcome to my project!")
        Your project is set up! Welcome to my project!
    """
    print(f"Your project is set up! {param}")


if __name__ == "__main__":
    main()
