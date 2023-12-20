import secrets
import hashlib


def generate_apikey(user_info):    
    user_string = str(user_info)    
    random_api_key =  secrets.token_urlsafe(32)    
    hashed_api_key = hashlib.sha512(random_api_key.encode('utf-8')).hexdigest()
    hashed_user = hashlib.sha512(user_string.encode('utf-8')).hexdigest()    
    api_key = f"{hashed_api_key}-{hashed_user}"
    return api_key 


print(generate_apikey("Test.test@gmail.com"))

def extract_api_key_and_user_info(api_key):
    api_key = api_key.split("-")
    random_api_key = api_key[0]
    hashed_user = api_key[1]
    return random_api_key, hashed_user


print(extract_api_key_and_user_info(generate_apikey("Test.test@gmail.com")))