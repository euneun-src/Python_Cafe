import json
ORDERFILE = 'orders.json'

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
    def add(self, cup: str) -> None:
        self.orders.append(Order(cup))

    # 날짜 입력 후 (통계정보?) 조회
    # def show_today(self, day: str) -> None:
    #     # [✔] / [ ] 표시
    #     if len(self.orders) == 0:
    #         print("등록된 주문내역이 없습니다.")
    #         return
    #     for h in self.habits:
    #         mark = " "
    #         if h.is_done(day):
    #             mark = "✔"
    #         print(f"[{mark}] {h.name} (총 {h.total()}일)")

    # 주문내역 파일에 저장
    def save(self, filename: str) -> None:
        data = [o.to_dict() for o in self.orders]
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
            o = Order(d["메뉴"])
            #o.done_dates = d["체크한날"]
            self.orders.append(o)

# { '손님1', '라떼', 2, m, 2 } 입력받아 저장
def add_order(order: DailyOrder) -> None:
    cup = input("메뉴 이름을 말씀해주세요.: ").strip()
    if cup == "":
        print("메뉴를 입력하세요.")
    else:
        order.add(cup)
        print(f"'{cup}' 추가 완료")


def main() -> None:
    order = DailyOrder()
    order.load(ORDERFILE)

    while True:
        print("1. 주문하기 | 2. 결제하기")
        print("3. 영수증 출력 | 4. 매출 통계 확인")

        choice = input("선택: ").strip()
        if choice == "1":
            # 메뉴판 출력
            # -------------------
            # | 아메리카노    4500 ㅣ
            # | 라떼        5000 ㅣ
            # | 바닐라라떼    5500 ㅣ
            # | 핫초코       5000 ㅣ
            # | 망고스무디    6000 ㅣ
            # | 샷 추가      +500 ㅣ
            # | 2샷 추가    +1000 ㅣ
            # | 사이즈업      +500 ㅣ
            # --------------------
            print("=====[메뉴판]=====")
            add_order(order)
            # 메뉴 이름, 사이즈, 추가하실 샷 수를 말씀해주세요.
            # 몇 잔 드릴까요?
        elif choice == "2":
            pass
            # 결제는 어떻게 하시겠어요?
            # 총 [12000원] 결제 완료되었습니다.
            # 총 금액 공식 ( {price} + {size} + {shot} ) * quantity
            # [500번]으로 불러드리겠습니다.
            # 총 금액, 결제 시간정보까지 저장됨
            # order.save(CSVFILE)
        elif choice == "3":
            pass
            # 고객 숫자 입력 - 500
            # 영수증 출력
        elif choice == "4":
            pass
            # 날짜 입력 0000-00-00
            # 일일 매출 통계 출력
        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()