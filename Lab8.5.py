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