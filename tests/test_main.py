from mblogs.main import main


def test_main_default_parameter(capsys):
    """Test that main() works with default parameter."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Your project is set up! \n"