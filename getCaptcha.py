# import requests
# def ocr_space_file(filename, overlay=False, api_key='K85656633888957', language='eng'):
#     payload = {'isOverlayRequired': overlay,
#                'apikey': api_key,
#                'language': language,
#                }
#     with open(filename, 'rb') as f:
#         r = requests.post('https://api.ocr.space/parse/image',
#                           files={filename: f},
#                           data=payload,
#                           )
#     return r.content.decode()
# # Use examples:
# test_file = ocr_space_file(filename='download.png', language='pol')
# print(test_file)

import requests

api_url = 'https://api.api-ninjas.com/v1/imagetotext'
image_file_descriptor = open('download.png', 'rb')
files = {'image': image_file_descriptor}
Headers = { "X-Api-Key" :  "kVECTAGldECAYKWiqYbnfA==CZDT9FwujKw6dFeD"}
r = requests.post(api_url,headers=Headers, files=files)
print(r.json())