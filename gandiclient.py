#Gandi API Xmlrpc Client
import xmlrpclib
import datetime

hosting_uri = 'https://rpc.gandi.net/xmlrpc/2.0/'

class GandiAPIClient(object):
    proxy = xmlrpclib.ServerProxy(hosting_uri)

    def __init__(self):
        pass

    def __getattr__(self, name):
        return self.function(self.proxy, name)

    class function:
        def __init__(self, proxy, name):
            self.proxy = proxy
            self.name = name

        def __call__(self, *args):
            func = self.proxy.__getattr__(self.name)
            return func(*args)
