import requests

import hashlib
import sys 
# le damos solo los 5 primeros caracteres
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# # captura la respuesta de una url
# res = requests.get(url)
# print(res)
# # response [200] es bien, response[400] es mal

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # for h in hashes:
    #     print(h, count)
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count
    return 0
    


def pwned_api_check(password):
    # Check password if it exists in API response

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    # print(response)
    # aqui puedo apreciar todos los pasword cuayas primeras 5 letras coinciden con la mia
    return get_password_leaks_count(response, tail)



def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

if __name__ =='__main__':
    sys.exit(main(sys.argv[1:]))

main(sys.argv[1:])
