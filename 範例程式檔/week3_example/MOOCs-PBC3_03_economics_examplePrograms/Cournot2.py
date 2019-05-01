import matplotlib.pyplot as plt

def plotEq(q1, q2, a, c1, c2, n):
  ub1 = (a - c1) / 2 * 2.5
  ub2 = (a - c2) / 2 * 2.5
  ub = max(ub1, ub2)

  # axes
  plt.plot([0, 0], [ub, -1], "k--")
  plt.plot([-1, ub], [0, 0], "k--")
  # best responses
  plt.plot([0, 0], [ub, a - c1], "g")
  plt.plot([0, (a - c1) / 2], [a - c1, 0], "g")
  plt.plot([ub, a - c2], [0, 0], "r")
  plt.plot([a - c2, 0], [0, (a - c2) / 2], "r")

  for i in range(n):
    q1Cur = q1[i]
    q2Cur = q2[i]
    q1Next = q1[i + 1]
    q2Next = q2[i + 1]

    plt.plot([q1Cur, q1Next], [q2Cur, q2Cur], "g", linewidth = 2.0)
    plt.plot([q1Next, q1Next], [q2Cur, q2Next], "r", linewidth = 2.0)
  
  # initial point and equilibrium point
  q1Eq = (a + c2 - 2 * c1) / 3
  q2Eq = (a + c1 - 2 * c2) / 3  

  if a < 2 * c2 - c1:
    q1Eq = (a - c1) / 2
    q2Eq = 0
  elif a < 2 * c1 - c2: 
    q1Eq = 0
    q2Eq = (a - c2) / 2

  plt.plot([q1[0]], [q2[0]], "bo")  
  plt.plot([q1Eq], [q2Eq], "bo") 
    
  plt.axis([-1, ub, -1, ub])  
  plt.xlabel('quantity of product 1')
  plt.ylabel('quantity of product 2')
  plt.show()

def printEq(q1, q2, n):
  for i in range(n + 1):
    s = "(" + str(round(q1[i], 4))
    s += ", " + str(round(q2[i], 4))
    s += ")"
    print(s)
        
def CournotEq(a, c1, c2, n):
  q1 = list()
  q1.append((a - c1) / 2)
  q2 = list()
  q2.append(max((a - q1[0] - c2) / 2, 0))

  for i in range(n):
    q1Next = max((a - q2[i] - c1) / 2, 0)
    q1.append(q1Next)
    q2Next = max((a - q1Next - c2) / 2, 0)
    q2.append(q2Next)

  return q1, q2
  
def CournotEqFinal_c2(a, c1, c2List, n):
  for c2 in c2List:
    # get the equilibrium
    q1, q2 = CournotEq(a, c1, c2, n)
    q1Eq = q1[n - 1] 
    q2Eq = q2[n - 1]
    
    # print it out
    s = str(c2) 
    s += " (" + str(round(q1Eq, 4))
    s += ", " + str(round(q2Eq, 4))
    s += ")"
    print(s)

    
  
  
  
  
  
a = 10.0
c1 = 8.0
c2 = 1.0
n = 10

q1, q2 = CournotEq(a, c1, c2, n)
printEq(q1, q2, n)
plotEq(q1, q2, a, c1, c2, n)

c2List = range(1, 10)
CournotEqFinal_c2(a, c1, c2List, n)
