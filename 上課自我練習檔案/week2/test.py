import matplotlib.pyplot as py
test = [1,2,3,4,5,1,2,3,4,5,1,1,1,5,5]
endpoint = range(1,7,1)#1~2(不包含2) ,2~3(不包含3),3~4(不包含4),4~5,5~6
py.hist(test,bins=endpoint,facecolor ="blue",edgecolor ="black") #bins 切幾個長條
py.ylim(0,7)
py.xlim(0,7)
py.show()
n,bins,patches = py.hist(test,bins=endpoint)
print(n) #每個區間有幾個點
print(bins) #區間