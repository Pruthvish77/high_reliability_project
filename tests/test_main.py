from src.main import main

def test_main():
    result = main()
    assert result["add"] == 8
    assert result["sub"] == 8
    assert result["mul"] == 24
    assert result["div"] == 4
