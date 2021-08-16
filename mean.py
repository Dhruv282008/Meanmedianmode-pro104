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
total = 0

for i in newdata:
    total += i

mean = total / n
print("The Mean(Average) is -> "+ str(mean))
