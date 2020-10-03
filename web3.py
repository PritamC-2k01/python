from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_902129.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
num=1
sum=0
for tag in tags:
    
    print("stud "+ str(num)+" "+tag.text)
    sum=sum+int(tag.text)
    num+=1
print(num-1)
print(sum)


