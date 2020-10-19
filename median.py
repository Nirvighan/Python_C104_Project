# IMPORT NECESSARY LIBRARIES
import csv 

# READ THE CSV FILE
with open('SOCR-HeightWeight.csv',newline = '')as csv_data:
    reader = csv.reader(csv_data)
    file_data = list(reader)

# CUT THE FIRST LINE OF CSV DATA
file_data.pop(0)

# CREATE AN EMPTY LIST
new_data = []

# RUN A LOOP FOR STORING THE WEIGHT DATA IN THE EMPTY LIST
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#GETTING THE MEDIAN

n = len(new_data)

new_data.sort()

if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])

    median = (median1+median2)/2

else:
    median = new_data[n//2]

print("MEDIAN OF WEIGHT IS")
print(median)
