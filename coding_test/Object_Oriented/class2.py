class CreditCard:
    """ 신용 카드를 나타내는 CreditCard 클래스 """
    
    MAX_PAYMENT_LIMIT = 30000000
    
    def __init__(self, name, password, payment_limit):
        """ __init__ 메소드 : 이름, 비밀번호, 카드 한도 정보를 인스턴스로 가짐 """
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit
        
    def get_name(self):
        """ getter 메소드 : __name의 값을 리턴 """
        return self.__name
    
    def set_name(self, value):
        """ setter 메소드 : 파라미터로 받은 값을 변수에 설정 """
        self.__name = value
        
    def get_password(self):
        """ getter 메소드 : "비밀번호는 볼 수 없습니다"를 리턴 """
        return "비밀 번호는 볼 수 없습니다"
    
    def set_password(self, value):
        """ setter 메소드 : 파라미터로 받은 값을 변수에 설정 """
        self.__password = value
        
    def get_payment_limit(self):
        """ getter 메소드 : __payment_limit의 값을 리턴 """
        return self.__payment_limit
    
    def set_payment_limit(self, value):
        """ setter 메소드 : 파라미터로 받은 값을 변수에 설정 """
        """ 파라미터로 받은 값이 0과 MAX_PAYMENT_LIMIT 사이에 있는 값이 아니면 "카드 한도는 0원 ~ 3첨만 원 사이로 설정해 주세요!"라는 메시지를 출력 """
        if 0 <= value and value <= CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = value
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
            
            
card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())