# with open("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     for row in data:
#         print(row)
    

# import csv

# with open("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature  = []
    
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         # print(row)
#     print(temperature)

import pandas

data = pandas.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/weather_data.csv") 
print(data["temp"] )
print(type(data))
temp_lis = data["temp"].to_list()
print(temp_lis)
avg = sum(temp_lis)/len(temp_lis)
# print(avg)
# print(data["temp"].max())
print(data["condition"])
print(data.condition)

# get data in row
# print(data[data.day == data.day.max()])

# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(data.day, "temperature was",monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# dataxls = data.to_csv("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/new_data.csv")


# i have to analyse the csv file and findout the color, count and the total number of squrrels in the csv file


# data = pandas.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250119.csv")
# gray_squrrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squrrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squrrels = len(data[data["Primary Fur Color"] == "Black"])

# # print(gray_squrrels)
# # print(cinnamon_squrrels)
# # print(black_squrrels)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squrrels, cinnamon_squrrels, black_squrrels]
   
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("/Users/sudipto/Documents/code/projects/100days of code/day25 pandas/squrrel_count.csv")      