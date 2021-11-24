class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

listOfCars = [None for i in range(10)]

with open('cars.txt') as f:
  lines = f.readlines()
  for i in range(10):
    arr = lines[i].split(" ")
    carToAdd = Car(lines[0], lines[1])
    listOfCars[i] = carToAdd
