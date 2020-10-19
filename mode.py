# IMPORT NEEDED LIBRARIES
from collections import Counter
import csv

# READ THE CSV FILE
with open('SOCR-HeightWeight.csv', newline='') as csv_data:
    reader = csv.reader(csv_data)
    file_data = list(reader)

# CUT THE FIRST LINE
file_data.pop(0)

# CREATE AN EMPTY LIST
new_data=[]

# RUN A LOOP FOR STORING THE WEIGHT DATA IN THE EMPTY LIST
for i in range(len(file_data)):
	n_num = file_data[i][2]
	new_data.append(n_num)



#CALCULATE THE MODE
data = Counter(new_data)
mode_data_for_range = {
                        "110-120": 0,
                        "120-130": 0,
                        "130-140": 0,
                        "140-150":0
                    }
for height, occurence in data.items():
    if 110 < float(height) < 120:
        mode_data_for_range["110-120"] += occurence
    elif 120 < float(height) < 130:
        mode_data_for_range["120-130"] += occurence
    elif 130 < float(height) < 140:
        mode_data_for_range["130-140"] += occurence
    elif 140 < float(height) < 150:
        mode_data_for_range["140-150"] += occurence
print(mode_data_for_range)
mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
print(mode_range)
print(mode_occurence)
print(mode_range[0])
print(mode_range[1])

mode = float((mode_range[0] + mode_range[1]) / 2)
print('MODE OF WEIGHT IS ')
print(mode)