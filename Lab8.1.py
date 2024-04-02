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