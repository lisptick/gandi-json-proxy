# For WSGIImportScript in apache configuration.
from jsonrpc_server import JsonRpcApp
from xmlrpclib import DateTime
from gandiclient import GandiAPIClient

dthandler = lambda obj: str(obj) if isinstance(obj, DateTime) else None
client = GandiAPIClient()
application = JsonRpcApp(client, dthandler)
