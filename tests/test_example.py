from pybase.main import main


def test_main():
    try:
        main()
    except Exception as e:
        assert False, f"main() raised an exception: {e}"
