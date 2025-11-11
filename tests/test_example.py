from pybase.myapi import myprint


def test_main():
    try:
        myprint()
    except Exception as e:
        assert False, f"main() raised an exception: {e}"