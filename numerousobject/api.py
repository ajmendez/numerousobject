import os
import requests
from pprint import pprint


VERSION = '1.1'
URL = 'https://{subdomain}.manything.com/{request}'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}


def credentials(filename=None):
    if filename is None:
        filename = '~/.limited/numerousobject'
    return open(os.path.expanduser(filename), 'r').read().strip().split(' ')


class API(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.s = requests.session()
        self.headers = HEADERS
        self.version = VERSION
    
    
    def __del__(self):
        self.s.close()
    
    
    def _get(self, url, isjson=True, iscomplex=False, **kwargs):
        tmp = {'headers':self.headers}
        tmp.update(kwargs)
        response = self.s.get(url, **tmp)
        if isjson:
            if iscomplex:
                return response.json()
            else:
                return response.json()['result']
        else:
            return response.content
    
    def _logger(self, device, item, isjson=True, iscomplex=False, **kwargs):
        url = '{}/{}'.format(device['logger'], item)
        params = {
            'uid': device['uidd'],
            'token': device['loggerToken'],
        }
        params.update(kwargs)
        return self._get(url, params=params, isjson=isjson, iscomplex=iscomplex)
        
    def getsub(self, suffix=1, region='useast1'):
        return '{region}-auth-{suffix}'.format(**locals())
    
    
    def login(self, **kwargs):
        '''Login using the credentials to get token and ddevice information'''
        url = URL.format(subdomain=self.getsub(), request='login')
        params = {
            'email':    self.username,
            'password': self.password,
            'version':  self.version,
        }
        params.update(**kwargs)
        self.logininfo = self._get(url, params=params)
        self.uid = self.logininfo['uid']
        self.token = self.logininfo['authToken']
        print 'Logged in as {} [{}]'.format(self.username, self.uid)
    
    
    

    def deviceinfo(self, device_id=1, **kwargs):
        '''UID is a combination of the UID of the user and the device number starting at 1'''
        url = URL.format(subdomain=self.getsub(), request='deviceinfo')
        params = {
            'uid':   '{}.{}'.format(self.uid, device_id),
            'token': self.token,
        }
        params.update(kwargs)
        return self._get(url, params=params)
    
    def getsettings(self, device, **kwargs):
        '''get the settings for the device'''
        return self._logger(device, 'getsettings', **kwargs)
    
    def capturethumb(self, device, **kwargs):
        '''Request a thumbnail from the camera?'''
        self._logger(detice, 'capturethumb', **kwargs)
    
    
    def livesession(self, device, **kwargs):
        '''Get the live data from the camera.'''
        return self._logger(device, 'livesession', **kwargs)
        
    
    def session(self, device, **kwargs):
        '''Get a list of sessions
        {"err":"expecting uid startt [endt] [offset] [limit]"}'''
        params = {
            'startt': 1, # start time?
            'offset': 0, # for multiple pages
            'limit': 20, # default from web
        }
        params.update(kwargs)
        return self._logger(device, 'session', **params)
    
    def sessionthumb(self, device, sessionid, **kwargs):
        '''Get a 192x144 jpg image for a sessionid'''
        params = {
            'session': sessionid,
        }
        params.update(kwargs)
        return self._logger(device, 'sessionthumb', isjson=False, **params)
    
    
    def listthumbs(self, device, startime, endtime, **kwargs):
        params = {
            'startt': starttime,
            'endt': endtime,
            'mingap': 900,
        }
        params.update(kwargs)
        return self._logger(device, 'listthumbs', **params)
    
    
    def get(self, device, time, **kwargs):
        '''Get the video and audio data (intensity)'''
        params = {
            'time': time,
            'lod': 2, # no idea what this is.  is either 0 or 2
        }
        params.update(kwargs)
        return self._logger(device, 'get', iscomplex=True, **params)
    
    
    def getthumb(self, device, time, **kwargs):
        url = '{logger}/getthumb/{uid}/{time}/{token}'.format(time=time, **device)
        return self._get(url, isjson=False)
    
    
    def getstill(self, device, time, **kwargs):
        '''get a still image'''
        url = '{logger}/getstill/{uidd}/{time}/{loggerToken}'.format(time=time, **device)
        return self._get(url, isjson=False)
    
    
    def liststills(self, device, session, starttime, endtime, **kwargs):
        params = {
            'session': session,
            'startt': starttime,
            'endt': endtime,
            'mingap': 1,
        }
        params.update(kwargs)
        return self._logger(device, 'liststills', **params)
    
    
    def listclips(self, device, **kwargs):
        '''List the clips from this device'''
        return self._logger(device, 'listclips', **kwargs)
    
    
    def video(self, device, starttime, endtime, **kwargs):
        params = {
            'startt': starttime,
            'endt': endtime,
        }
        params.update(kwargs)
        return self._logger(device, 'video', **params)
    
    
    def alert(self, device, starttime=1, offset=0, limit=20, **kwargs):
        '''Events (on the website), but where motion was captured'''
        params = {
            'startt': starttime,
            'offset': offset,
            'limit': limit,
        }
        params.update(kwargs)
        return self._logger(device, 'alert', **params)
    
    def editclip(self, device, **kwargs):
        params = {
            'id': clipid, 
            'description': description,
            'shared': 0,
            'allowmanything': 0,
        }
        params.update(kwargs)
        return self._logger(device, 'editclip', **params)
        
    
    def timelapse(self, device, session, description, starttime, endtime, **kwargs):
        '''Create a timelapse'''
        params = {
            'description': description,
            'session': session, 
            'shared': 0, 
            'allowmanything': 0,
        }
        params.update(kwargs)
        return self._logger(device, 'timelapse', **params)
    
    

if __name__ == '__main__':
    username, password = credentials()
    api = API(username, password)
    api.login()
    device = api.deviceinfo(1)
    # pprint(api.livesession(device))
    # pprint(api.session(device))
    # pprint(api.getsettings(device))
    # pprint(api.get(device, 1450898100))
    pprint(api.alert(device, 1450898100))
    
    
    
    