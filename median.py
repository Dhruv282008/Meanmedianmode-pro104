import csv

with open("DATA.csv") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)

newdata = []

for i in range(len(filedata)):
   weight = filedata[i][2]
   newdata.append(float(weight))

n = len(newdata)
newdata.sort()

if n % 2 == 0:
    median1 = float(newdata[n//2])
    median2 = float(newdata[n//2-1])
    median = (median1 + median2)/2
else:
    median = float(newdata[n//2])
print("The Median is -> " + str(median))