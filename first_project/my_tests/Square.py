class Square:

    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @property
    def perimeter(self):
        if self.__perimeter is None:
            print('calculating perimeter')
            self.__perimeter = self.__side * 4
        return self.__perimeter

    @property
    def area(self):
        if self.__area is None:
            print('calculating area')
            self.__area = self.side ** 2
        return self.__area

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimeter = None


if __name__ == '__main__':
    s1 = Square(10)
    print(s1.area)
    print(s1.perimeter)
    print(s1.perimeter)
    s1.side = 15
    print(s1.area)
    print(s1.perimeter)
