import urllib.request
import urllib.parse
import re
# requesting the data from the site using urllib
url = 'http://pythonprogramming.net'
values = {'s': 'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
# parsing the data using re
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
for p in paragraphs:
    print(p)