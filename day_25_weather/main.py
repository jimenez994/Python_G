import csv
import pandas


# with open("weather_data.csv", mode="r") as file:
#     raw_data = file.readlines()
#     data = []
#     for item in raw_data:
#         data.append(item.strip())
#         print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# monday = data[data.day == "Monday"]
# print((monday.temp[0] * 9/5) + 32)


# create a dataframe from scratch
# new_data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(new_data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")

s_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(s_data[s_data["Primary Fur Color"] == "Gray"])
red_count = len(s_data[s_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(s_data[s_data["Primary Fur Color"] == "Black"])

s_dic = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_count, red_count, black_count]
}
df = pandas.DataFrame(s_dic)
df.to_csv("squirrel_count.csv")

print(df)

