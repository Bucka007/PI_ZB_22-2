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