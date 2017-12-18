import urllib.request # basic urllib requests
import urllib.parse #basic parsing for urllib
# opening a url
x = urllib.request.urlopen('https://google.com')
# printing the data you get from the site (get request)
print(x.read())
# post request
url = 'http://pythonprogramming.net' # the basic url
values = {'s':'basic', 'submit':'search'} # values of the post request values
data = urllib.parse.urlencode(values) # encoding the values into url format
data = data.encode('utf-8') # encoding the url into utf-8 
req = urllib.request.Request(url, data) # the actual post request 
resp = urllib.request.urlopen(reg) # opening and reading from the site
respData  = resp.read() # reading information from site
print(respData) # printing the information from the site
# now trying to open a request in google which is not going to work so putting a try
try:
    x = urllib.request.urlopen('https://google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e)) # printing the error message (HTTP Error 403: Forbidden)
# Now for the solution
try:
    url = 'https://google.com/search?q=test'
    headers = {} # headers are informatino about the user making the request
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile = open('withHeaders.txt','w') # saveing the search results into a file
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e)




