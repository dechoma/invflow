
from clients.owncloud_client import OwnCloudClient

options = {
 'webdav_hostname': "https://webdav.server.ru",
 'webdav_login':    "login",
 'webdav_password': "password",
 'webdav_timeout': 30
}

local = '/tmp/test'
remote = '/dev/ss'

client = OwnCloudClient(options)

client.upload_file(remote, local)




