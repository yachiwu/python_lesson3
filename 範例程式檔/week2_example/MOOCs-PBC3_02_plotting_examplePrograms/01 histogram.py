import csv, datetime

def findSubTimes(fileName):
  fh = open(fileName, "r")
  csvFile = csv.DictReader(fh)

  subTimes = [] # to store submission times
  for row in csvFile:
    dt = datetime.datetime.strptime(row["SubmissionTime"], "%H:%M:%S").time()
    sub = (dt.hour - 9) * 3600 + (dt.minute - 20) * 60 + dt.second
    subTimes.append(sub)

  fh.close()
  return subTimes



  
  
  
import matplotlib.pyplot as py

subTimes = findSubTimes("midterm2.csv")
# print(subTimes) # just testing

n, bins, patches = py.hist(subTimes, bins = range(0, 12000, 1000))

print(n) # the frequencies
print(bins) # the class endpoints

