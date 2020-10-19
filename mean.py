# IMPORT NEEDED LIBRARIES
import csv

# READ THE CSV FILE
with open('SOCR-HeightWeight.csv',newline = '')as csv_data:
    reader = csv.reader(csv_data)
    file_data = list(reader)

# CUT THE HEADING OR FIRST LINE OF CSV DATA FILE
file_data.pop(0)

new_data = []

# RUN A LOOP FOR GETTING THE WEIGHT DATA IN A LIST
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#GETTING THE MEAN

n = len(new_data)
total = 0
for x in new_data:
    total+=x

mean = total/n
print("MEAN/AVERAGE OF WEIGHT IS")
print(mean)