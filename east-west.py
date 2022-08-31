import requests
import os
 
host=input('Please enter Host URL: Example http://my.fqdn.com: ')
if "http://" not in host:
    host = "http://" + host
port = input('Enter custom port or press Enter for HTTP')
if port != "":
    port = input('Enter Port:')
    host= host+":"+port

timeout = 5

testcases = {
        1:{"category":"ids","name":"zip","method":"get","url":"/20MB.zip","header":"","data":""},
        2:{"category":"ids","name":"pdf","method":"get","url":"/5MB.pdf","header":"","data":""},
        3:{"category":"ids","name":"solarwinds-nt1","method":"get","url":"/api/Skipi18n","header":"","data":""},
        4:{"category":"ids","name":"solarwinds-nt2","method":"get","url":"/api/WebResource.axd","header":"","data":""},
        5:{"category":"ids","name":"nt3","method":"get","url":"/index.html","header":{'User-Agent':'windows launcher v1.0.20'},"data":""},
        6:{"category":"ids","name":"nt4","method":"get","url":"/conn.php?data=callback=","header":{"User-Agent": ""},"data":""},
        100:{"category":"All","name":"Test Cases","method":"","url":"","header":"","data":""},
        200:{"category":"Exit","name":"Test Cases","method":"","url":"","header":"","data":""},
} 

def menu(cases):
    for p_id ,p_info in cases.items():
       print ("Enter "+str(p_id)+ " for Test Case: " + p_info["category"] + " " + p_info["name"] )
    choice = input("Please Enter your Selection:")
    print ("\nSelection ="+choice)
    return int(choice)
    
def webrequest(method,url,headers,data):
    print ("in webrequest")
    if method == "get":
     print ("GET -> "+url)
     try:
         res = requests.get(url, headers=headers,timeout=timeout,verify = False)
         print ("headers:") 
         print(res)
         return res
     except: 
         print ("Connection Reset / Timeout")
    elif method == "post":
     try:
         print ("POST -> "+url+ "data:"+ data)
         res = requests.post(url, data=data,timeout=timeout,verify = False)
         print(res)
         return res
     except: 
         print ("Connection Reset / Timeout")
    elif method == "send":
     try:
         data = open(testcases[choice]["data"], "rb")
         res = requests.post(url,files = {"form_field_name": data},verify = False)
         print(res)
         return res
     except: 
         print ("Connection Reset / Timeout")
    elif method == "dos":
         cmd="siege -R ~/.siege/siege.conf -r 5000 -b "+url
         print(cmd)
         print(os.system(cmd))
         return url
#./siege -R ~/.siege/siege.conf -r 5000 -b http://valtix-l-ingresomalolvc-f856dc60f7eef929.elb.us-west-2.amazonaws.com/index.html        
def runall(cases):
    for p_id ,p_info in cases.items():
      endpoint=host+p_info["url"]
      print ("URL: "+endpoint)
      webrequest(p_info["method"],endpoint,p_info["header"],p_info["data"])
      
loop = 1
while loop == 1:
    choice = menu(testcases)
    if choice not in (100,200):
      endpoint = host + testcases[choice]["url"]
      res=webrequest(testcases[choice]["method"],endpoint,testcases[choice]["header"],testcases[choice]["data"])
    elif choice == 100:
        print ("All Test Cases\n")
        runall(testcases)
    elif choice == 200:
        print ("100 Exit")
        loop = 0
