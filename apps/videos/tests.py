from django.test import TestCase
import vimeo
import re
import json
import requests

videoid = "748103424"  # código del video en vimeo
videoid2 = "661062330"  # código del video en vimeo


client = vimeo.VimeoClient(
    token="9533cf67685a3e6417a1be4b5d800d35",
    key="875390dfbca228733bbf36c7c661185b8fbe2f2c",
    secret="5Z1LrvWHGB8vPeXxj6pcbm/TQKUWE7kuKOojrO0KywBUGvvUkJDaIsRmKXAYJV7lIe6+EgmuVg6Syu1F9qXB4RxJBZBfcOutY79RiBvcbqCq47AVQYPgTlaKRG2EHra8",
)

client2 = vimeo.VimeoClient(
    token="438a13e91fb038b956189c3eba8becdc",
    key="130c6e80c9de8a4080958e5e497368d99374a15d",
    secret="Xoc2x8udkKQPKR3jmJSriCgtcKBDm1WjESbjQ3V7WOVzG91P7GCMn1xMLV8u4uaxuj0JlCvx5uUn0PoPZsTb2AwsoGW6nIh/UOy5hV4eGO2r2izsiR4suh95DvSUsBqS",
)

respondeSccot = client2.get("https://api.vimeo.com/videos/" + videoid2).json()

response = client.get("https://api.vimeo.com/videos/" + videoid).json()


#print(response)


#response2 = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=dfd1ae46d57141059e05cfdb0dd24b03")
#print(response2.status_code)
#print(response2.content)

#response3 = requests.get("https://ipwho.is/")
#print(response3)
#ipwhois = json.load(response3)
#print ("{0} {1}".format(ipwhois['country'],ipwhois['flag']['emoji']))
