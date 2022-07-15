import base64
import hmac
import requests
from hashlib import sha1
from os import getenv

host = getenv('AWS_HOST').encode("UTF-8")
access_key = getenv('AWS_ACCESS').encode("UTF-8")
secret_key = getenv('AWS_SECRET').encode("UTF-8")
item_path = '/awsexamplebucket1/photos/puppy.jpg'

string_to_sign = f'GET\n\n\nTue, 27 Mar 2007 19:36:42 +0000\n{item_path}'.encode("UTF-8")
signature = base64.encodebytes(
                                hmac.new(
                                         secret_key, string_to_sign, sha1
                                         ).digest()
                                ).strip()
auth = f'AWS {access_key.decode()}:{signature.decode()}'

print(f'HOST: {host}')
print(f'AUTH: {auth}')

response = requests.get(url=host, auth=auth)

print(response)
