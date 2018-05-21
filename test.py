import time
import random

curNum = lambda: int(round(time.time()) % 100000000)
ranNum = lambda: random.randrange(100, 999)

print(curNum())
print(ranNum())
print("{}{}".format(curNum(), ranNum()))

def testmain():
  return render_template('home.html')