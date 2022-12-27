import requests
import json

url = 'https://api.lovo.ai/v1/conversion'
data = json.dumps({
    "text": "hello world! my name is Oleksandr Supriadkin",
    "speaker_id": "Oleksandr Supriadkin",
    "emphasis": '[0, 5]',
    "speed": 1,
    "pause": 0,
    "encoding": "mp3"
})

headers = {
    'apiKey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzYWEwZmYzNjk0NTY1MDAxNDI3YzA2OSIsImlhdCI6MTY3MjA4OTU4ODM0MH0.tGCv91bSr_Dr_xYXymcZdrrfdftfHa2QiGdZGwJO9EU',   # Your API key goes here
    'Content-Type': 'application/json; charset=utf-8'
}

res = requests.post(url, headers=headers, data=data)

outfile = 'sample.mp3'
with open(outfile, 'wb') as f:
    f.write(res.content)

print(f'Audio content written to file "{outfile}"')