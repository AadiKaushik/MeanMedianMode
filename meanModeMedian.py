import csv
from collections import Counter

with open('C:/Users/aadi_/Desktop/coding/python/MeanMedianMOde/SOCR-HeightWeight.csv',newline='') as f :
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newData = []

for i in range(len(file_data)):
    n_num = file_data[i][1] 
    newData.append(float(n_num))

n = len(newData)
total = 0
for x in newData:
    total=total+x
mean = total/n
print(mean)

newData.sort()
if n%2 == 0 :
    median1 = float(newData[n//2]) 
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2
else:
    medain = newData[n/2]    
print(str(median))

data = Counter(newData)
modeDataForRange = {'50-60': 0,'60-70' : 0,'70-80' : 0} 
for h,occ in data.items():
    if 50<float(h)<60:
        modeDataForRange['50-60'] += 1 

    elif  60<float(h)<70:
        modeDataForRange['60-70'] += 1  

    elif 70<float(h)<80:
        modeDataForRange['70-80'] += 1     

modeRange,modeOcc = 0,0
for range,occ in modeDataForRange.items():
    if occ > modeOcc:
        modeRange,modeOcc= [int(range.split('-')[0]),int(range.split('-')[1])],occ
mode = float((modeRange[0]+modeRange[1])/2)
print(mode)


