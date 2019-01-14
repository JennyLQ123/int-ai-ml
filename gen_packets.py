from scapy.all import *
import random

dst=[1,2,7,8]
ps=[]

for i in range(1000):
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="2%d.0.%d.%d"%((i%4+4),random.randint(2,250),random.randint(2,250)),dst="10.0.%d.1"%(dst[i%4],)) / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ps.append(p)

wrpcap("6.packet",ps)
