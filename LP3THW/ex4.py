# number of cars
cars = 100
# number of places in each car
space_in_car = 4
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of cars not driven
cars_not_driven = cars - drivers
# number of cars driven
cars_drinven = drivers
# total of places available in all cars
carpool_capacity = cars_drinven * space_in_car
# average passengers per car
average_passengers_per_car = passengers / cars_drinven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

#Erro do Zed:
#average_passengers_per_car = car_pool_capacity / passenger
#O 'bug' consistiu em 4 erros:
# . dois erros de digitação: 1 - '_' na variável car_pool_capacity
#                            2 - faltou 's' na variável 'passengers'
# . 1 erro por troca da variável 'cars_drinven' pela variável 'carpool_capacity'
# . 1 erro de matemática: a média desejada é composta de passengers / cars_drinven
