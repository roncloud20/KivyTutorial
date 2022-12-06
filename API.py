import requests
amt = 5
# consuming the online API
url = f"https://api.apilayer.com/fixer/convert?to=ngn&from=usd&amount={amt}"

payload = {}
headers= {
  "apikey": "ZEOcbrQz5MhCJ7U7O5hlwaTrjICVjjtU"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()['result']

print(result)