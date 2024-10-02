#import csv
#with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)


#data = pandas.read_csv("weather_data.csv")
#temperature_average = data["temp"].mean()
#temperature_max = data["temp"].max()
#average = sum(temperature)/len(temperature)
#print(temperature_average)
#print(temperature_max)

#data_dict = {
#    "students": ["Louisa", "Søren", "Astrid"],
#    "scores": [20, 40, 60]
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
black_fur_count = len(data[data["Primary Fur Color"] == "Black"])
cinnanmon_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_fur_count)
print(black_fur_count)
print(cinnanmon_fur_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "number of squirrels": [gray_fur_count,black_fur_count,cinnanmon_fur_count]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Squirrel_fur_color.csv")