#Задача "Изменять нельзя получать"

class Vehicle:
    def __init__(self, owner, __model, __color,__engine_power):
        self.owner = owner                      #владелец транспорта. (владелец может меняться)
        self.__model = __model                  #модель (марка) транспорта. (не можем менять название модели)
        self.__engine_power = __engine_power     #мощность двигателя (не меняется)
        self.__color = __color                   #название цвета

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        print(f'{self.__model} Модель: ')
    def get_horsepower(self):
        print(f'{self.__engine_power} Мощность двигателя: ')
    def get_color(self):
        print(f'{self.__color} Цвет: ')
    def print_info(self):
        print(f'Модель:{self.__model}\nМощность двигателя:{self.__engine_power}\nЦвет:{self.__color}\nВладелец:{self.owner}\n')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Невозможно покрасить в {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
vehicle1.print_info()