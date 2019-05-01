import matplotlib.pyplot as py

p1 = [0, 6, 38, 52, 57, 62, 65, 70, 75, 81, 85, 88]
p2 = [0, 0, 0, 1, 2, 2, 2, 3, 7, 14, 20, 24]
p3 = [0, 0, 1, 3, 8, 17, 27, 33, 38, 44, 48, 49] 
p4 = [0, 0, 0, 4, 6, 9, 18, 30, 42, 52, 58, 62]

times = range(0, 12000, 1000)
py.plot(times, p1, label = "Problem 1", marker = 'o') 
py.plot(times, p2, label = "Problem 2", marker = 'o') 
py.plot(times, p3, label = "Problem 3", marker = 'o') 
py.plot(times, p4, label = "Problem 4", marker = 'o') 
py.legend(loc = 'upper left')
py.xlabel('Time')
py.ylabel('Number of "Accepted"')
py.show()
