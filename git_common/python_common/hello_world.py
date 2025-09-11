import time, datetime


msg = 'Hello, World!'
date = datetime.datetime.now()

print('The date now is')
for n in range(3):
    time.sleep(1)
    print('.')

time.sleep(1)
print(date)
time.sleep(1)
print(msg)
