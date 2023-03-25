import sys

def hello(name):
    print(f"Hello, {name}!")
    print("Something's weird", file=sys.stderr)


def test_hello_miro(capsys):
    hello("Miro")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Miro!"
    assert "Something" in captured.err


if __name__ == "__main__":
    hello("PyLadies")
