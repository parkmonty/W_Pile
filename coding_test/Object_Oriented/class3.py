class CreditCard:
    """ 신용 카드를 나타내는 CreditCard 클래스 """
    
    MAX_PAYMENT_LIMIT = 30000000
    
    def __init__(self, name, password, payment_limit):
        """ __init__ 메소드 : 이름, 비밀번호, 카드 한도 정보를 인스턴스로 가짐 """
        self.name = name
        self._password = password
        self._payment_limit = payment_limit
    
    @property
    def password(self):
        """ getter 메소드: 문자열 "비밀 번호는 볼 수 없습니다"를 리턴한다. """
        return "비밀 번호는 볼 수 없습니다"
    
    @password.setter
    def password(self, value):
        """ setter 메소드: 파라미터로 받은 값을 변수에 설정한다. """
        self._password = value
    
    @property
    def payment_limit(self):
        """ getter 메소드: _payment_limit 변수를 리턴한다. """
        return self._payment_limit
    
    @payment_limit.setter
    def payment_limit(self, value):
        """ setter 메소드: 파라미터로 받은 값을 변수에 설정한다.  """
        """ 파라미터로 받은 값이 0과 MAX_PAYMENT_LIMIT 사이에 있는 값이 아니면 "카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!" 라는 메시지를 출력 """
        if 0 <= value and value <= CreditCard.MAX_PAYMENT_LIMIT:
            self._payment_limit = value
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
    
    
card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)