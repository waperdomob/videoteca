from django.test import TestCase
import vimeo
import json


videoid = "748103424"  # código del video en vimeo

client = vimeo.VimeoClient(
    token="9533cf67685a3e6417a1be4b5d800d35",
    key="875390dfbca228733bbf36c7c661185b8fbe2f2c",
    secret="5Z1LrvWHGB8vPeXxj6pcbm/TQKUWE7kuKOojrO0KywBUGvvUkJDaIsRmKXAYJV7lIe6+EgmuVg6Syu1F9qXB4RxJBZBfcOutY79RiBvcbqCq47AVQYPgTlaKRG2EHra8",
)

response = client.get("https://api.vimeo.com/videos/" + videoid).json()
print(response)
