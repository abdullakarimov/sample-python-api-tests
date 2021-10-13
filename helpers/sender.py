from helpers.connector import connector

class sender(object):
    """sends http requests"""

    def send(method, path, data = {}):
        conn = connector()
        print(method + ': https://petstore.swagger.io/v2/user/' + path)
        return conn.sesh(method, 'https://petstore.swagger.io/v2/user/' + path, data)
        

