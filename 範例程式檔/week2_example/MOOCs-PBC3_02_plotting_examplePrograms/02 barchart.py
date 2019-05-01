import csv, datetime

def findSubCnt(filePath):
  fh = open(filePath, "r")
  csvFile = csv.DictReader(fh)

  subCntDict = dict()

  for row in csvFile:
    sid = int(row["StudentID"])
    if sid in subCntDict:
      subCntDict[sid] += 1
    else:
      subCntDict[sid] = 1
    
  fh.close()

  return subCntDict


  
import matplotlib.pyplot as py

subCnt = findSubCnt("midterm2.csv")

# seq = range(0, len(subCnt))
width = 0.35
# py.bar(seq, sorted(subCnt.values()), width)
# py.show()
py.bar(subCnt.keys(),subCnt.values(),width)
py.show()   





