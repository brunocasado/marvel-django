import time, hashlib, requests

class MarvelDataContainer:
    
    def __init__(self, CustomerContainer, CurrentMarvelConnection, current_method):
        # @todo make validations and CustomerCli

        self.offset = CustomerContainer['offset']
        self.total = CustomerContainer['total']
        self.limit = CustomerContainer['limit']
        self.results = CustomerContainer['results']

        self.next_offset = self.offset * 2

        self._CustomerContainer = CustomerContainer
        self._CurrentMarvelConnection = CurrentMarvelConnection
        self._current_method = current_method

    # def __iter__(self):
    #     return self

    def next(self):
        # make generator
        if (len(self._CustomerContainer.results)):
            return self._CurrentMarvelConnection._call(self._current_method, { 'offset': self.next_offset })
        raise Exception('No more results =(')



# a very simple way to connect on marvel api
class MarvelConnect(object):
    def __init__(self, apikey, private):
        self.base_endpoint = 'https://gateway.marvel.com/v1/public/{0}'
        self.apikey = apikey
        self.ts = int(time.time())
        self.hash = self._generateHash(private)

    def _generateHash(self, private):
        md5 = hashlib.md5()
        md5.update('{0}{1}{2}'.format(self.ts, private, self.apikey).encode())
        return md5.hexdigest()
        
    def _call(self, method, params={}):

        # todo params like filters
        full_endpoint = self.base_endpoint.format(method)

        filters = {
            'ts': self.ts,
            'apikey': self.apikey,
            'hash': self.hash
        }

        filters.update(params)

        response = requests.get(full_endpoint, filters)
        response_data = response.json()
        
        if response.status_code == 200:
            return MarvelDataContainer(response_data['data'], self, method)
        
        raise Exception('an error occured Error: Code {0} - Msg: {1}'.format(response_data['code'], response_data['message']))


    @property
    def apikey(self):
        return self._apikey

    @apikey.setter
    def apikey(self, v):
        if not v:
            raise Exception('Public key must be informed')

        self._apikey = v
        return self



class MarvelCli(MarvelConnect):
    def __init__(self, *args, **kwargs):
        super(MarvelCli, self).__init__(*args, **kwargs)

    def get_all_customers(self, params={}):
        return self._call('characters', params)
        
    