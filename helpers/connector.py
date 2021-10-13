import requests

class connector(object):
    """initializes requests sessions"""

    def sesh(self, method, url, data={}):
        s = requests.Session()
        if method == 'get':
            return s.get(url)
        elif method == 'post':
            s.headers.update({'Content-Type': 'application/json'})
            return s.post(url, json=data)
        elif method == 'del':
            return s.delete(url)
        else:
            return s.get(url)