import XMLtoJSON1
import XMLtoJSON2
import XMLtoJSON3
import time
ts = 0
for i in range(100):
    t = time.time()
    XMLtoJSON1.XMLtoJSON()
    ts += (time.time()-t)
print(ts)
ts = 0
for i in range(100):
    t = time.time()
    XMLtoJSON2.XMLtoJSON()
    ts += (time.time()-t)
print(ts)
ts = 0
for i in range(100):
    t = time.time()
    XMLtoJSON3.XMLtoJSON()
    ts += (time.time()-t)
print(ts)

