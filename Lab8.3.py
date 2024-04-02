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