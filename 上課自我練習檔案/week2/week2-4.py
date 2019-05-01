#散步圖與摺線圖
import matplotlib.pyplot as py
p1 = [0,6,38,52,57,62,65,70,75,81,85,88] #第一題在第0秒時有0個人答對 1秒時有6人答對等
p2 = [0,0,0,1,2,2,2,3,7,14,20,24]
p3 = [0,0,1,3,8,17,27,33,38,44,48,49]
p4 = [0,0,0,4,6,9,18,30,42,52,58,62]
times = range(0,12000,1000)
#散步圖方式
# py.plot(times,p1,'o')
# py.plot(times,p2,'o')
# py.plot(times,p3,'o')
# py.plot(times,p4,'o')
# py.plot(times,p1,'ro',label = 'problem1')
# py.plot(times,p2,'gs',label = 'problem2')
# py.plot(times,p3,'b+',label = 'problem3')
# py.plot(times,p4,'k',label = 'problem4')
#折線圖
py.plot(times,p1,label = 'problem1',marker = 'o')
py.plot(times,p2,label = 'problem2',marker = 'o')
py.plot(times,p3,label = 'problem3',marker = 'o')
py.plot(times,p4,label = 'problem4',marker = 'o')
py.legend(loc = 'upper left') #呈現上方label寫的東西
py.xlabel('time')
py.ylabel('number of accepted')
py.show()
