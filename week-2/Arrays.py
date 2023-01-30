cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
  print(x)

cars.append("Honda")
cars.remove("Volvo")