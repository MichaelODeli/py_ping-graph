# requied libs. to install - input in cmd "pip install matplotlib pythonping"
import matplotlib.pyplot as plt
from pythonping import ping
import time
import os
os.system("cls")

# get some variables
target_link=str(input("Enter URL, or IP-adress to ping: "))
time_sec=int(input("How long we must ping this URL? (sec): "))
time_msec=time_sec*1000
if time_sec%2!=0:
    time_sec+=1
counter=int(time_sec/2)
grid_ans=str(input("Do you want to get grid on your graph? [True/False]: "))
print("If server did not response in 2000 msec, in graph you will see '-1'.")

# set graph settings
plt.title("Ping graph")
xlabel_name="Time, sec"
ylabel_name="Server response time, msec"
plt.xlabel(xlabel_name)
plt.ylabel(ylabel_name)
plt.grid(grid_ans)

# pinging
resp_time=[]
while counter!=0:
    response=ping(target=target_link, count=1, timeout=2)
    rsptime=int(round(response.rtt_avg_ms, 0))
    if rsptime<2000:
        resp_time.append(rsptime)
    if rsptime==2000:
        resp_time.append('-1')
    counter-=1
    time.sleep(1)
print(resp_time)

# get time list
time_list=[ ]
cntr=0
while time_sec!=0:
    time_list.append(cntr)
    cntr+=2
    time_sec-=2
print(time_list)
plt.plot(time_list, resp_time)
plt.show()