import base64
import hmac
from hashlib import sha1

host = 'https://example.s3.ap-southeast-2.amazonaws.com'
access_key = 'AKIAIOSFODNN7EXAMPLE'.encode("UTF-8")
secret_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'.encode("UTF-8")

string_to_sign = 'GET\n\n\nTue, 27 Mar 2007 19:36:42 +0000\n/awsexamplebucket1/photos/puppy.jpg'.encode("UTF-8")
signature = base64. encodebytes(
                                hmac.new(
                                         secret_key, string_to_sign, sha1
                                         ).digest()
                                ).strip()

auth = f'AWS {access_key.decode()}:{signature.decode()}'

print(f'AUTH: {auth}')
