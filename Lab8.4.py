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