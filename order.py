CSVFILE = 'orders.csv'
from datetime import datetime

items= {"아메리카노":4500,"라떼":5000,"바닐라라떼":5500,"핫초코":5000,"망고스무디":6000}
class Order:
    def __init__(self, menu:str, quantity:int, size:str, shot:int) -> None:
        self.menu = menu
        self.price = 0
        self.paymentTime = None
        self.quantity = quantity
        self.size = size
        self.shot = shot
        self.isCard = None
        # CSV 형태로 저장

        # def 가격계산 추가():
	    # 결제시각은 자동추가
	    # def 주문 파일에 저장():

    def calculate_price(self) -> int:
        self.price = items[self.menu]
        #print(f"메뉴가격:  {self.price}")
        if self.size == "L":
            self.price += 500
        #print(f" 사이즈 UP 가격:  {self.price}")
        self.price += self.shot * 500
        #print(f"샷 추가 개수 :  {self.shot}")
        #print(f"샷 추가 가격 :  {self.price}")
        return self.price * self.quantity

    def payTime(self) -> None:
        self.paymentTime = datetime.now()

    def print_price(self) -> int:
        return self.price

    def isCard(self,card:bool) -> None:
        if card == True:
            self.isCard = True
        else:
            self.isCard = False
    def setQuantity(self,quantity:int):
        self.quantity = quantity
        
def main() -> None:
    order =  Order("아메리카노", 1, "L", 2)
    order.calculate_price()
    print(order.price)
    order.payTime()
    print(order.paymentTime)

if __name__ == "__main__":
    main()

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

    def find(self, title: str) -> Book | None:
        pass  # TODO
        for b in self.books:
            if b.title == title:
                return b
        return None
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


    #print("1. 주문 | 2. 영수증 출력 | 3. 매출 통계")

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