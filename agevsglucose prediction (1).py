from matplotlib import pyplot as plt
import pandas as pd
import math as ma
df = pd.read_csv(r"C:\Users\Amiya Kumar\Desktop\python\csvfile\abc.csv")
print(df)
a=len(df['age'])
sumx=0
sumy=0
sumxy=0
sumx2=0
for i in range(0,a,1):
    sumx=sumx+df['age'][i]
print("sumx is ",sumx)
for i in range(0,a,1):
    sumy=sumy+df['glucose'][i]
print("sumy is",sumy)
xy=[]
for i in range(0,a,1):
    su=(df['age'][i]*df['glucose'][i])
    xy.append(su)
print("xy is",xy)
for i in range(0,a,1):
    sumxy=sumxy+xy[i]
print("sumxy is",sumxy)
c=1
x2=[]
for i in range(0,a,1):
    c=pow(df['age'][i],2)
    x2.append(c)
print("x2 is",x2)
for i in range(0,a,1):
    sumx2=sumx2+x2[i]
print("sumx2 is",sumx2)
xc=1
#for i in range(0,a,1):
    #xc=(xc*(df['age'][i]*df['glucose'][i]))
#print("xc is",xc)
p=((sumy*sumx2)-(sumx*sumxy))
q=((a*(sumx2))-(pow(sumx,2)))
fd=p/q#a
print("a value is",fd)
rt=((a*sumxy)-(sumx*sumy))
tr=((a*sumx2)-(pow(sumx,2)))
ff=rt/tr#b
print("b value is",ff)
ag=int(input("enter your age"))
past=0
for i in range(0,a,1):
    if(ag==df['age'][i]):
        past=(df['glucose'][i])
        pre_age=(df['age'][i])
sg=((ff*ag)+fd)
print("your predicted sugar level is",sg)
if(sg>120):
    print("dibetic patient")
elif(sg<90):
    print("lowsugar")
else:
    print("perfectly fine")	
import csv
with open(r"C:\Users\Amiya Kumar\Desktop\python\csvfile\abc.csv",'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([ag,sg])
lag=[]
for i in range(0,a,1):
    while(ag==df['age'][i]):
        lag.append(ag)
print("no. of times yoyr entered agre present data",lag)
#for ag in df['age']:
    #sugar=(sg/past)
    #error_per=sugar*100
    #if(error_per<=1):
        #acc_per=1-error_per
    #else:
        #acc_per=1+error_per
    #print("accuracy of the prediction is",acc_per)

#plt.plot(45,df['glucose'],label="predict",color="green",linewidth=5)
#plt.plot(45,past,label="past",color='red',linewidth=5)
#plt.xlabel('glucose')
#plt.ylabel('age')
#plt.title('Information')
#plt.show()
