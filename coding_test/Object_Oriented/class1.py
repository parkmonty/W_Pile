class User:
    """ User 클래스: SNS의 유저를 나타내는 클래스 """
    count = 0
    
    def __init__(self, name, email, pw):
        """ __init__ 메소드: 이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다. """
        self.name = name
        self.email = email
        self.pw = pw
        
        User.count += 1
        
    def say_hello(self):
        """ say_hello 메소드: 유저의 이름을 포함한 인사 메시지를 출력한다. """
        print(f"안녕하세요! 저는 {self.name}입니다!")
        
    def __str__(self):
        """ __str__ 메소드: 유저 정보를 정의된 문자열 형태로 리턴한다. """
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def number_of_users(cls):
        """ number_of_users 메소드: 총 유저 수를 출력하는 클래스 메소드 """
        print("총 유저 수는: {}입니다".format(cls.count))
        

help(User)