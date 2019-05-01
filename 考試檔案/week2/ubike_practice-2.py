import csv,os,datetime
import matplotlib.pyplot as py
f = open('ubike.csv','r')
station = {}#該站有幾台可租借的腳踏車
count = {}
lat = {} #緯度
lon = {} #經度
capacity = {}
for row in csv.DictReader(f):
	time = datetime.datetime.strptime(row['time'],"%Y/%m/%d %H:%M")
	hour = time.hour
	if hour==17 or hour==18: #在晚上5~7點間
		id = int(row['id'])
		if id not in station:
			lat[id] = float(row["latitude"])
			lon[id] = float(row["longitude"])
			station[id]= int(row["bike"])
			capacity[id]= int(row["lot"])
			count[id]=1
		else:
			station[id]+=int(row["bike"])
			capacity[id]+= int(row["lot"])
			count[id]+=1
f.close()
id_seq = station.keys()
id_seq = sorted(id_seq)
redlat = []
redlon = []			
yellowlat = []
yellowlon = []					
greenlat = []
greenlon = []					
bluelat = []
bluelon = []	
for k in id_seq:
	capacity[k] = float(capacity[k]) / count[k] #該站總共腳踏車數
	station[k] = (float(station[k]) / count[k]) / capacity[k]
	if station[k]<0.2:
		redlat.append(lat[k])
		redlon.append(lon[k])
	elif 0.2<=station[k]<0.3:
		yellowlat.append(lat[k])
		yellowlon.append(lon[k])
	elif 0.3<=station[k]<0.4:
		greenlat.append(lat[k])
		greenlon.append(lon[k])	
	else:
		bluelat.append(lat[k])
		bluelon.append(lon[k])		
py.xlabel('latitude')    	
py.ylabel('longitude')
py.title('bike distribution')
py.plot(redlat,redlon,'ro',label='<20%')
py.plot(yellowlat,yellowlon,'yo',label='20~30%')
py.plot(greenlat,greenlon,'go',label='30~40%')
py.plot(bluelat,bluelon,'bo',label='>40%')
py.axis([25.01,25.05,121.52,121.56])
py.legend(loc = 'lower right')
py.show()