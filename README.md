## Самостоятельная работа №8

### Задание №1
• Текст задания

Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

• Оформленный код

``` python
class Car:
  def __init__(self, make, model, year, color, mileage):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self.mileage = mileage

  def __str__(self):
    return f"{self.make} {self.model} ({self.year})"

  def drive(self, distance):
    self.mileage += distance
    print(f"Пройдено {distance} км.")

  def get_mileage(self):
    return self.mileage

car = Car("Toyota", "Camry", 2023, "белый", 0)

print(f"Информация об автомобиле: {car}")
car.drive(100)
print(f"Пробег: {car.get_mileage()} км.")
```

• Скрины консоли

![image](https://github.com/Bucka007/PI_ZB_22-2/assets/165667984/af77b396-46b1-4ba4-82b8-c9ad6d452398)

• Развернутый вывод

Класс Car (Автомобиль) в Python моделирует основные характеристики автомобиля, такие как Марка, Модель, год выпуска, пробег

### Задание №2
• Текст задания

Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

• Оформленный код

``` python
class Car:
  def __init__(self, make, model, year, color, mileage, fuel_tank_capacity):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self.mileage = mileage
    self.fuel_tank_capacity = fuel_tank_capacity
    self.fuel_level = fuel_tank_capacity

  def __str__(self):
    return f"{self.make} {self.model} ({self.year})"

  def drive(self, distance):
    self.mileage += distance
    print(f"Пройдено {distance} км.")

  def get_mileage(self):
    return self.mileage

  def refuel(self, amount):
    if amount > self.fuel_tank_capacity:
      print(f"Невозможно заправить {amount} л. Превышена вместимость бака ({self.fuel_tank_capacity} л).")
    else:
      self.fuel_level += amount
      print(f"Заправлено {amount} л.")

  def get_fuel_level(self):
    return self.fuel_level

car = Car("Toyota", "Camry", 2023, "белый", 0, 50)

print(f"Информация об автомобиле: {car}")
car.drive(100)
print(f"Пробег: {car.get_mileage()} км.")
car.refuel(20)
print(f"Уровень топлива: {car.get_fuel_level()} л.")
car.refuel(60)
```

• Скрины консоли

![image](https://github.com/Bucka007/PI_ZB_22-2/assets/165667984/aacecc99-bda1-4ece-9472-2b2747f334f1)

• Развернутый вывод

Этот код создает класс `Car`, представляющий автомобиль, с методами для передвижения, получения пробега, заправки и получения уровня топлива. Создается объект `car` (автомобиль Toyota Camry 2023) и для него вызываются методы для демонстрации различных функций автомобиля.

### Задание №3
• Текст задания

Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли
• Оформленный код

``` python
class Car:
  def __init__(self, make, model, year, color, mileage, fuel_tank_capacity):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self.mileage = mileage
    self.fuel_tank_capacity = fuel_tank_capacity
    self.fuel_level = fuel_tank_capacity

  def __str__(self):
    return f"{self.make} {self.model} ({self.year})"

  def drive(self, distance):
    self.mileage += distance
    print(f"Пройдено {distance} км.")

  def get_mileage(self):
    return self.mileage

  def refuel(self, amount):
    if amount > self.fuel_tank_capacity:
      print(f"Невозможно заправить {amount} л. Превышена вместимость бака ({self.fuel_tank_capacity} л).")
    else:
      self.fuel_level += amount
      print(f"Заправлено {amount} л.")

  def get_fuel_level(self):
    return self.fuel_level


class ElectricCar(Car):
  def __init__(self, make, model, year, color, mileage, battery_capacity):
    super().__init__(make, model, year, color, mileage, 0)
    self.battery_capacity = battery_capacity
    self.battery_level = battery_capacity

  def __str__(self):
    return f"{super().__str__()} (электромобиль)"

  def drive(self, distance):
    if distance > self.battery_level:
      print(f"Недостаточно заряда батареи. Пройдено {self.battery_level} км.")
      self.mileage += self.battery_level
      self.battery_level = 0
    else:
      self.mileage += distance
      self.battery_level -= distance
      print(f"Пройдено {distance} км.")

  def charge(self, amount):
    if amount > self.battery_capacity:
      print(f"Невозможно зарядить {amount} кВт⋅ч. Превышена емкость батареи ({self.battery_capacity} кВт⋅ч).")
    else:
      self.battery_level += amount
      print(f"Заряжено {amount} кВт⋅ч.")

  def get_battery_level(self):
    return self.battery_level

car = ElectricCar("Tesla", "Model 3", 2023, "белый", 0, 75)

print(f"Информация об автомобиле: {car}")
car.drive(100)
print(f"Пробег: {car.get_mileage()} км.")
car.charge(20)
print(f"Уровень заряда батареи: {car.get_battery_level()} кВт⋅ч.")
car.drive(80)
print(f"Пробег: {car.get_mileage()} км.")
car.charge(100)
```

• Скрины консоли

![image](https://github.com/Bucka007/PI_ZB_22-2/assets/165667984/5b26877b-cf0f-45b3-aa16-f5ffefca6836)

• Развернутый вывод

Этот код создает класс `ElectricCar`, который является подклассом класса `Car`. Оба класса представляют автомобили, но `ElectricCar` дополнительно имеет функционал для работы с электрическими автомобилями - зарядка и уровень заряда батареи. Выведенные команды демонстрируют работу методов для электрического автомобиля.

### Задание №4
• Текст задания

Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли
• Оформленный код

``` python
class ElectricCar:
  def __init__(self, make, model, year, color, mileage):
    self._make = make
    self._model = model
    self._year = year
    self._color = color
    self._mileage = mileage
    self._battery_capacity = 75  # Скрытый атрибут
    self._battery_level = 75  # Скрытый атрибут

  def __str__(self):
    return f"{self._make} {self._model} ({self._year}) (электромобиль)"

  def get_make(self):
    return self._make

  def get_model(self):
    return self._model

  def get_year(self):
    return self._year

  def get_color(self):
    return self._color

  def get_mileage(self):
    return self._mileage

  def drive(self, distance):
    if distance > self._battery_level:
      print(f"Недостаточно заряда батареи. Пройдено {self._battery_level} км.")
      self._mileage += self._battery_level
      self._battery_level = 0
    else:
      self._mileage += distance
      self._battery_level -= distance
      print(f"Пройдено {distance} км.")

  def charge(self, amount):
    if amount > self._battery_capacity:
      print(f"Невозможно зарядить {amount} кВт⋅ч. Превышена емкость батареи ({self._battery_capacity} кВт⋅ч).")
    else:
      self._battery_level += amount
      print(f"Заряжено {amount} кВт⋅ч.")

  def get_battery_level(self):
    return self._battery_level


car = ElectricCar("Tesla", "Model 3", 2023, "белый", 0)

print(f"Информация об автомобиле: {car}")
car.drive(100)
print(f"Пробег: {car.get_mileage()} км.")
car.charge(2)
```

• Скрины консоли

![image](https://github.com/Bucka007/PI_ZB_22-2/assets/165667984/45586e4b-b09f-4e21-8e49-e23dd37b3552)

• Развернутый вывод

Этот код создает класс `ElectricCar`, который представляет электромобиль с методами для передвижения, работы с зарядом и получения информации о машине. Код выполняет определенные действия для электромобиля, выводя информацию о пробеге и уровне заряда батареи в процессе использования.

### Задание №5
• Текст задания

Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли

• Оформленный код

``` python
class Vehicle:
  def __init__(self, make, model, year, color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def __str__(self):
    return f"{self.make} {self.model} ({self.year})"

  def get_info(self):
    return f"Тип: {self.__class__.__name__}"


class Car(Vehicle):
  def __init__(self, make, model, year, color, mileage):
    super().__init__(make, model, year, color)
    self.mileage = mileage

  def drive(self, distance):
    print(f"Пройдено {distance} км.")

  def get_info(self):
    return super().get_info() + f"\nПробег: {self.mileage} км."


class ElectricCar(Car):
  def __init__(self, make, model, year, color, mileage, battery_capacity):
    super().__init__(make, model, year, color, mileage)
    self.battery_capacity = battery_capacity

  def drive(self, distance):
    if distance > self.battery_capacity:
      print(f"Недостаточно заряда батареи. Пройдено {self.battery_capacity} км.")
    else:
      super().drive(distance)

  def get_info(self):
    return super().get_info() + f"\nЁмкость батареи: {self.battery_capacity} кВт⋅ч."

car = Car("Toyota", "Camry", 2023, "белый", 0)
print(car.get_info())

electric_car = ElectricCar("Tesla", "Model 3", 2023, "черный", 0, 75)
print(electric_car.get_info())
```

• Скрины консоли

![image](https://github.com/Bucka007/PI_ZB_22-2/assets/165667984/f3dfb6fa-aa93-47bd-ac60-b8aa56ff2fce)

• Развернутый вывод

Этот код создает классы `Vehicle`, `Car` и `ElectricCar`, представляющие типы транспортных средств с различным функционалом. При вызове метода `get_info()`, каждый класс возвращает информацию о себе, включая тип, пробег или ёмкость батареи в зависимости от класса. Создаются объекты `car` и `electric_car`, для которых выводится информация по вызову метода `get_info()`.
