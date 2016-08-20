class A:
    def __init__(self):
        print("A.__init__()")
        self.message = "Hello"

class B(A):
    def __init__(self):
        print("B.__init__()")

        super().__init__()
        print("self.message is " + self.message)

B()

''' '만일 이 파일이 인터프리터에 의해서 실행되는 경우라면'
if __name__ == "__main__":
    b = B()
'''