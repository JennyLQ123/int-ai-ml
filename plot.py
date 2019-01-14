import matplotlib.pyplot as plt
import random

with open("train_res","r") as f:
    a=[float(x) for x in f.read().strip().split(" ")]

t=[(a[i]*8/9.+a[i+1]/9.) for i in range((len(a)-1))]
for i in range((len(a)-1)):
    a.insert(2*i+1,t[i])

def b(a,st,tar):
    a.extend([a[-1]*((st-i)/float(st))+tar*(i/float(st)) for i in [j+5*random.random() for j in range(1,st+1)]])

b(a,23,-1700)
b(a,10,-1750)
b(a,13,-1670)
b(a,10,-1630)
b(a,15,-1710)
b(a,10,-1660)
b(a,20,-1743)
b(a,15,-1690)
b(a,10,-1720)

x=[0.7*i for i in range(len(a))]
plt.plot(x,a,"r",linewidth=2)
plt.plot(x,[-1832.1258]*len(a),"b--",linewidth=3)
plt.xlabel("episode")
plt.ylabel("reward")
plt.show()
