import requests
import hashlib
import sys

def request_api_data(query_str):
    url = 'https://api.pwnedpasswords.com/range/' + query_str
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} is found {count} times. Change your password now!')
        else:
            print(f'{password} is not found. Carry on!')
    return 'Done'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))