from urllib import request, parse
import sys

myUrl = "https://www.google.com/search?"
value = {'q': 'ANDESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print("Error occuried during web request!!")
    print(sys.exc_info()[1])