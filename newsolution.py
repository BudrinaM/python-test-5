class Positions(Enum):  
    JUNIOR = 10  
    MIDDLE = 12  
    SENIOR = 20  
  
  
# class Programmer:
#     def __init__(self, name: float, position: Positions) -> None:
#         self.__name = name
#         self.__position = position
#         self.__hour_price = self.__position.value
#
#     def work(self, time: int) -> None:
#         self.__time += time
#
#     def rise(self) -> str:
#         if self.__position.name == 'JUNIOR':
#             self.__position = Positions.MIDDLE
#
#         elif self.__position.name == 'MIDDLE':
#             self.__position = Positions.SENIOR
#
#         else:
#             self.__hour_price += 2
#
#     def info(self) -> str:
#         return f'{self.__name}: {self.__time} ч. {self.__give_salary()} тгр.'
#
#     def __give_salary(self) -> int:
#         salary = self.__hour_price // self.__time
#         self.__time = 0
#         return salary


class Programmer:
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        self.money = 0
        self.jun = 10
        self.mid = 15
        self.sen = 20
        self.time = 0

    def work(self, time: int) -> int:
        self.time += time
        if self.position == 'JUNIOR':
            self.money += time * self.jun
        elif self.position == 'MIDDLE':
            self.money += time * self.mid
        else:
            self.money += time * self.sen
            return self.money


    def rise(self) -> str:
        if self.position == 'JUNIOR':
            self.position = 'MIDDLE'

        elif self.position == 'MIDDLE':
            self.position = 'SENIOR'

        elif self.position == 'SENIOR':
            self.sen += 1

    def info(self) -> str:
        return f'{self.name}:отработано {self.time} ч. оклад составляет:{self.money * self.time} тгр.'


def main():
    prog = Programmer('Valeria', 'Junior')
    print(prog.work(50))
    print(prog.info)
    prog.work(50)
    prog.rise()
    prog.work(50)
    prog.rise()
    prog.work(50)
    prog.rise()
    prog.work(50)
    print(prog.info())

if __name__ =='__main__':
    main()
