import http.client

conn = http.client.HTTPSConnection("")

payload = "grant_type=client_credentials&client_id=wxGMKUhjLSfFmVdR0CrFvMfC1S6U0Pr0&client_secret=hpIkGGx9sr6NCap5JL48uK2MBNhWsW8QGnfsciantzFAeLcPT4yOS-HeHCMcrTSw&audience=https://dev-ie13exvycq67h1fb.us.auth0.com/api/v2/"

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "https://dev-ie13exvycq67h1fb.us.auth0.com/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))