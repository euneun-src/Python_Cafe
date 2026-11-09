CSVFILE = 'orders.csv'

class Order:
    def __init__(self, name: str) -> None:
        #elf.name = name
        #self.done_dates: list[str] = []
        
        # nickname, menu, price, datetime, quantity, size, shot, isCard
        # CSV 형태로 저장

        # def 가격계산 추가():
	    # 결제시각은 자동추가
	    # def 주문 파일에 저장():

    # def to_dict(self) -> dict:
    #     return {"이름": self.name, "체크한날": self.done_dates}

class DailyOrder:
    def __init__(self) -> None:
        self.orders: list[Order] = []

    # 주문내역 1개 추가하는 메서드
    def add(self, name: str) -> None:
        self.orders.append(Order(name))

    # 날짜 입력 후 (통계정보?) 조회
    def show_today(self, day: str) -> None:
        # [✔] / [ ] 표시
        if len(self.orders) == 0:
            print("등록된 주문내역이 없습니다.")
            return
        for h in self.habits:
            mark = " "
            if h.is_done(day):
                mark = "✔"
            print(f"[{mark}] {h.name} (총 {h.total()}일)")

    # 주문내역 파일에 저장
    def save(self, filename: str) -> None:
        data = [h.to_dict() for h in self.habits]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # 해당 날짜의 주문내역 업로드
    def load(self, filename: str) -> None:
        try:
            with open(filename, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        for d in data:
            h = Habit(d["이름"])
            h.done_dates = d["체크한날"]
            self.habits.append(h)

# { '손님1', '라떼', 2, m, 2 } 입력받아 저장
def add_habit(tracker: HabitTracker) -> None:
    name = input("새 습관: ").strip()
    if name == "":
        print("이름을 입력하세요.")
    elif tracker.find(name) is not None:
        print("이미 있는 습관입니다.")
    else:
        tracker.add(name)
        print(f"'{name}' 추가 완료")


def main() -> None:
    order = DailyOrder()
    order.load(CSVFILE)

    print("1. 주문 | 2. 영수증 출력 | 3. 매출 통계")

# 메뉴판
# --------------------
# | 아메리카노    4500 ㅣ
# | 라떼        5000 ㅣ
# | 바닐라라떼	  5500 ㅣ
# | 핫초코		 5000 ㅣ
# | 망고스무디    6000 ㅣ
# | 샷 추가      +500 ㅣ
# | 사이즈업	  +500 ㅣ
# --------------------