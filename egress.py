import requests
import os

timeout = 5

testcases = {
        1:{"category":"url-filtering","name":"block-github-test-repo","method":"get","url":"https://github.com/kavehvaltix/test2","header":"","data":""},
        2:{"category":"fqdn-filtering","name":"block-news","method":"get","url":"https://www.cnn.com/","header":"","data":""},
        3:{"category":"dlp","name":"dlp-block-ssn","method":"post","url":"https://hackme.valtixdemo.net","header":"","data":"332-43-5432"},
        4:{"category":"dlp","name":"dlp-us-phone","method":"post","url":"https://hackme.valtixdemo.net","header":"","data":"1-415-613-9999"},
        5:{"category":"ids","name":"cnc","method":"get","url":"https://hackme.valtixdemo.net/index.html","header":{'User-Agent':'windows launcher v1.0.20'},"data":""},
        6:{"category":"cnc","name":"nt1","method":"get","url":"https://www.example.com/api/Skipi18n","header":"","data":""},
        7:{"category":"cnc","name":"solarwinds-nt2","method":"get","url":"https://www.example.com/api/WebResource.axd","header":"","data":""},
        9:{"category":"DLP PII","name":"Send US Phone Number","method":"send","url":"https://www.example.com","header":"","data":"./usphone.txt"},
        10:{"category":"DLP PII","name":"US Social Security","method":"send","url":"https://www.example.com","header":"","data":"./usssn.txt"},
        11:{"category":"DLP PII","name":"US Bank Routing Numbers","method":"send","url":"https://www.example.com","header":"","data":"./bank-routing.txt"},
        12:{"category":"DLP PII","name":"RSA Key","method":"send","url":"https://www.example.com","header":"","data":"./rsa.key"},
        13:{"category":"DLP PII","name":"AWS Access Key","method":"send","url":"https://www.example.com","header":"","data":"./aws_access.key"},
        100:{"category":"All","name":"Test Cases","method":"","url":"","header":"","data":""},
        200:{"category":"Exit","name":"Test Cases","method":"","url":"","header":"","data":""},
} 

def menu(cases):
    for p_id ,p_info in cases.items():
       print ("Enter "+str(p_id)+ " for Test Case: " + p_info["category"] + " " + p_info["name"] )
    choice = input("Please Enter your Selection:")
    print ("\nSelection ="+choice)
    return int(choice)

def runall(cases):
    for p_id ,p_info in cases.items():
      webrequest(p_info["method"],p_info["url"],p_info["header"],p_info["data"])
    
def webrequest(method,url,headers,data):
    if method == "get":
     print ("GET -> "+url)
     try:
         res = requests.get(url, headers=headers,timeout=timeout,verify = False)
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
         print ("Sending out File: "+data)
         filehandle = open(data, "rb")
         res = requests.post(url,files = {"form_field_name": filehandle},verify = False)
         print(res)
         return res
     except: 
          print ("Connection Reset / Timeout")
    elif method == "dos":
         cmd="ab -c 50 -t 10 "+url
         print(cmd)
         print(os.system(cmd))
         return 
 

def sendfile(testcases):
    data = open(testcases[choice]["data"], "rb")
    try:
        res = requests.post(testcases[choice]["url"], files = {"form_field_name": data},verify = False)
        print(res)
        return res
    except requests.Timeout: 
        print ("in timeout")
    
    
loop = 1
choice = 0
#headers = {'user-agent': 'my-app/0.0.1'}
method = "get"
body="test"

while loop == 1:
    choice = menu(testcases)
    if choice == 8:
      endpoint = input('Please Enter the Test Endpoint Address:')
      res=webrequest(testcases[choice]["method"],endpoint,testcases[choice]["header"],testcases[choice]["data"])
    elif choice not in (100,200):
      res=webrequest(testcases[choice]["method"],testcases[choice]["url"],testcases[choice]["header"],testcases[choice]["data"])
    elif choice == 100:
        print ("All Test Cases\n")
        runall(testcases)
    elif choice == 200:
        print ("100 Exit")
        loop = 0
