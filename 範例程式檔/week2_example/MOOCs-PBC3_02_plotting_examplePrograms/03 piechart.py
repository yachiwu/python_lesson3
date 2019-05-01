import csv, datetime

def findProp(filePath):
  fh = open(filePath, "r")
  csvFile = csv.DictReader(fh)

  propDict = dict()

  for row in csvFile:
    result = row["Status"]
    if result in propDict:
      propDict[result] += 1
    else:
      propDict[result] = 1
    
  fh.close()

  return propDict

  
  
  
  
  
  
import matplotlib.pyplot as py

pf = findProp("midterm2.csv")

freqs = list(pf.values())
results = list(pf.keys())

#py.pie(freqs, labels = results, autopct = "%1.1f%%")
py.pie(freqs, labels = results)
py.show()







