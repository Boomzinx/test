import requests
from requests.auth import HTTPDigestAuth

# loginCred = HTTPDigestAuth('boomzinx', '9821937119Ab')
response1 = requests.post('https://github.com/login',auth= HTTPDigestAuth('boomzinx', '9821937119Ab'))
print(response1.status_code) 
if response1.status_code == 200:
    with open("response.html", "a") as f:f.write(str(response1.url))
    with open("response.html", "a") as f:f.write(str("  Login is Success, Status code:"))
    with open("response.html", "a") as f:f.write(str(response1.status_code))
    with open("response.html", "a") as f:f.write(str("\n"))
else:
     with open("response.html", "a") as f:f.write(str(response1.url))
     with open("response.html", "a") as f:f.write(str("  Login is Failed, Status code:"))
     with open("response.html", "a") as f:f.write(str(response1.status_code))
     with open("response.html", "a") as f:f.write(str("\n"))
