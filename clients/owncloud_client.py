from sink_clinet import SinkClient
from webdav3.client import Client


class OwnCloudClient(SinkClient):

    def __init__(self, options):
        self.client = Client(options)

    def upload_file(self, remote, local):
        self.client.upload_sync(remote_path=remote, local_path=local)
