import requests
import hashlib


def request_data_from_api(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code} CODE. Please check API.')
	return res


def get_leaks_count(hashes_list, hash_to_check):
	hashes = (line.split(':') for line in hashes_list.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			print(f'Password leaked {count} times')
			return
		print('Congrats! Excellent password!')
		return


def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	res = request_data_from_api(first5_char)
	get_leaks_count(res, tail)


pwned_api_check('1234')
