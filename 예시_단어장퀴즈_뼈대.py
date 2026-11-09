import json
import random

FILENAME = "words.json"


def load_words(filename: str) -> list[dict]:
    pass  # TODO: 없으면 []


def save_words(filename: str, words: list[dict]) -> None:
    pass  # TODO


def add_word(words: list[dict]) -> None:
    pass  # TODO: 영어 · 뜻 입력, 중복 확인


def quiz(words: list[dict], count: int) -> int:
    pass  # TODO: random.sample로 count개 출제, 맞힌 개수 return


def main() -> None:
    words = load_words(FILENAME)
    # TODO: 1 단어 추가 · 2 퀴즈 · 3 단어 목록 · q 저장 후 종료


if __name__ == "__main__":
    main()
