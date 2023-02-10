import requests
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
url = ""
auth ={
    'authorization': ''
}
msg1 = {
    'content':'$crime'
}
msg2 = {
    'content':'$slut'
}
msg3 = {
    'content':'$work'
}
msg4 = {
    'content':'$roulette all red'
}
msg5 = {
    'content':'$dep all'
}
while True:
    print("Envoi de message $crime")
    r = requests.post(url, headers=auth, data=msg1)
    time.sleep(1)
    print("Envoi de message $slut")
    r = requests.post(url, headers=auth, data=msg2)
    time.sleep(1)
    print("Envoi de message $work")
    r = requests.post(url, headers=auth, data=msg3)
    time.sleep(1)
    print("Envoi de message $roulette all red")
    r = requests.post(url, headers=auth, data=msg4)
    time.sleep(32)
    print("Envoi de message $dep all")
    r = requests.post(url, headers=auth, data=msg5)
    time.sleep(7260)
    print("Fin du sleep")
    print(current_time)

