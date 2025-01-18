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
# print(data["temp"] )
# print(type(data))
temp_lis = data["temp"].to_list()
print(temp_lis)
avg = sum(temp_lis)/len(temp_lis)
print(avg)
        