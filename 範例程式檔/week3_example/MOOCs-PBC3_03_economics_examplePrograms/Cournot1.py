import matplotlib.pyplot as plt

def plotEqUgly(q1, q2, a, c, n):
  for i in range(n): # for each iteration, draw two moves
    q1Cur = q1[i]
    q2Cur = q2[i]
    q1Next = q1[i + 1]
    q2Next = q2[i + 1]

    plt.plot([q1Cur, q1Next], [q2Cur, q2Cur], "g", linewidth = 2.0)
    plt.plot([q1Next, q1Next], [q2Cur, q2Next], "r", linewidth = 2.0)

  plt.show()

def plotEq(q1, q2, a, c, n):
  ub1 = (a - c) / 2 * 2.5
  ub2 = (a - c) / 2 * 2.5
  ub = max(ub1, ub2)

  # axes
  plt.plot([0, 0], [ub, -1], "k--")
  plt.plot([-1, ub], [0, 0], "k--")
  # best responses
  plt.plot([0, 0], [ub, a - c], "g")
  plt.plot([0, (a - c) / 2], [a - c, 0], "g")
  plt.plot([ub, a - c], [0, 0], "r")
  plt.plot([a - c, 0], [0, (a - c) / 2], "r")

  for i in range(n):
    q1Cur = q1[i]
    q2Cur = q2[i]
    q1Next = q1[i + 1]
    q2Next = q2[i + 1]

    plt.plot([q1Cur, q1Next], [q2Cur, q2Cur], "g", linewidth = 2.0)
    plt.plot([q1Next, q1Next], [q2Cur, q2Next], "r", linewidth = 2.0)

  # initial point and equilibrium point
  q1Eq = (a + c - 2 * c) / 3
  q2Eq = (a + c - 2 * c) / 3  
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
    
def CournotEq(a, c, n):
  q1 = list()
  q1.append((a - c) / 2)
  q2 = list()
  q2.append((a - q1[0] - c) / 2)

  for i in range(n):
    q1Next = (a - q2[i] - c) / 2
    q1.append(q1Next)
    q2Next = (a - q1Next - c) / 2
    q2.append(q2Next)

  return q1, q2
  
a = 10.0
c = 2.0
n = 10

q1, q2 = CournotEq(a, c, n)
printEq(q1, q2, n)
plotEq(q1, q2, a, c, n)


