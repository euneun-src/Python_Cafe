# ==================================================
# 프로젝트: ____________      팀 / 이름: ____________
# 한 문장 : ____________
# ==================================================
# 규칙: 타입 힌트는 전부 · 몸통은 pass + TODO · 실행해서 에러 0개
import json

FILENAME = "data.json"


class Item:
    """데이터 하나 (이름을 프로젝트에 맞게 바꾸세요)"""

    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict:
        pass  # TODO


class Manager:
    """여러 Item을 관리 (이름을 프로젝트에 맞게 바꾸세요)"""

    def __init__(self) -> None:
        self.items: list[Item] = []

    def add(self, item: Item) -> None:
        pass  # TODO

    def find(self, name: str) -> Item | None:
        pass  # TODO

    def save(self, filename: str) -> None:
        pass  # TODO

    def load(self, filename: str) -> None:
        pass  # TODO


def main() -> None:
    manager = Manager()
    manager.load(FILENAME)
    # TODO: while True 메뉴 (1 · 2 · 3 · q 저장 후 종료)


if __name__ == "__main__":
    main()
