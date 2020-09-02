class Person:
    def __init__(self, age, name, address):
        self.hello = '안녕하세요'
        self.age = age
        self.name = name
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 용산구')
maria.greeting()

print('이름', maria.name)
print('나이', maria.age)
print('주소', maria.address)