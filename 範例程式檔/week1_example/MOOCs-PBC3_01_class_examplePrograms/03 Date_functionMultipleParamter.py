class Date:
  def isLaterThan(self, aDate):
    if self.year > aDate.year:
      return True
    elif self.year == aDate.year:
      if self.month > aDate.month:
        return True
      elif self.month == aDate.month:
        if self.day > aDate.day:
          return True
    return False

  def toString(self):
    return str(self.year) + "/" + str(self.month) + "/" + str(self.day)


          
def strToDate(birthday): # birthday is a yyyy/mm/dd string
  d = Date()
  year, month, day = birthday.split("/")
  d.year = int(year)
  d.month = int(month)
  d.day = int(day)
  return d   
          
          

day1 = input("yyyy/mm/dd: ")
day1 = strToDate(day1)

day2 = input("yyyy/mm/dd: ")
day2 = strToDate(day2)

if day1.isLaterThan(day2):
  print(day1.toString() + " is later than " + day2.toString())
else:
  print(day1.toString() + " is note later than " + day2.toString())

