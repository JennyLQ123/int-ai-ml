import pickle

def edges(s,n,d,path):
  if(n==d)and(len(path)<=6):
    res[str(s)+str(d)].append(path[:])
    return
  if len(path)>6:
    return
  for i in range(10):
    if((G[n][i]!=100)and(i not in path)):
      path.append(i)
      edges(s,i,d,path)
      path.pop()

G=[
[100,1,100,2,100,100,100,100,0,100],
[0,100,1,4,3,100,100,100,100,100],
[100,0,100,100,3,100,100,100,100,1],
[0,1,100,100,100,2,3,100,4,100],
[100,0,1,100,100,4,100,3,100,2],
[100,100,100,0,1,100,3,2,100,100],
[100,100,100,1,100,2,100,3,0,100],
[100,100,100,100,2,1,0,100,100,4],
[0,100,100,1,100,100,2,100,100,100],
[100,100,0,100,2,100,100,3,100,100]]

pair=['01', '02', '06', '07', '08', '12', '16', '17', '18', '26', '27', '28', '67', '68', '78']

res={i:[] for i in pair}
rres={i:[] for i in pair}

for p in pair:
  edges(int(p[0]),int(p[0]),int(p[1]),[int(p[0])])

print res

for i in pair:
  rres[i]=["%s"*len(x)%tuple(x) for x in res[i]]

print rres

with open("path.pickle","w") as f:
  pickle.dump(rres,f)
