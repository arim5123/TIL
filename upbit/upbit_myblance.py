import jwt
import hashlib
import params as params
import requests
import uuid

from urllib.parse import urlencode, unquote

access_key = "안알"
secret_key = "랴줌"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get("https://api.upbit.com/v1/accounts", headers=headers)
res.json()

data = res.json()

won = float(data[0]["balance"])

print(won)
