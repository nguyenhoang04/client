import requests
url = 'http://surl.li/ebrpi'
r = requests.get(url, allow_redirects=True)
open('abc.png', 'wb').write(r.content)
