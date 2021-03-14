def test_func2():
    print("program2.py hello_world")


def test_func3(*, word1: str, word2: str) -> dict:
    print(f"word1>{word1}, word2>{word2}")
    return {'word1': word1, 'word2': word2}


if __name__ == '__main__':
    print(f"uruchomilismy modul program {__name__}")
