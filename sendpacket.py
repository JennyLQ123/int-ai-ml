from scapy.all import *
import time
import random

d=[2,6]

for m in xrange(1000):
  for i in range(10):
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="10.0.0."+str(i),dst="10.0.7.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s6-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="11.0.0."+str(i),dst="10.0.8.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s6-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="12.0.0."+str(i),dst="10.0.1.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s6-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="13.0.0."+str(i),dst="10.0.2.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s6-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="14.0.0."+str(i),dst="10.0.1.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s0-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="15.0.0."+str(i),dst="10.0.2.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s0-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="16.0.0."+str(i),dst="10.0.7.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s0-trf")
    p = Ether(src="00:00:00:00:02:02",dst="00:00:00:00:07:07") / IP(src="17.0.0."+str(i),dst="10.0.8.1") / TCP() / "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    sendp(p,iface= "s0-trf")
