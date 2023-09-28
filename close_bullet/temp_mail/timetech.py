import time, re, base64, json
from .. import  Requests, Randoms


class TimeTech:
	req = Requests.proxy_session(Proxy=True)
	domain_list = ['gmail10p.com', 'oletters.com', 'oemails.com', 'oegmail.com', 'stempemail.com', 'suiemail.com', 'voewo.com', 'yanemail.com']
	
	def __init__(self, full_name: str, text_from_message: str, timeout: int = 20):
		self.full_name = full_name
		self.timeout = timeout
		self.text_from_message = text_from_message
		self.email_id = None
		self.email = self.make_email()
	
	@staticmethod
	def base64_decode(text: str):
		return base64.b64decode(text[::-1]).decode("utf-8")
	
	@staticmethod
	def base64_encode(text: str):
		return str(base64.b64encode(text.encode("utf-8")).decode("utf-8"))[::-1]
	
	def make_email(self) -> str:
		_ = Randoms.from_list(['_', '.', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		login = self.full_name.replace(' ', _).lower()
		email = login + '@' + Randoms.from_list(self.domain_list)
		self.email = email
		self.email_id = email.replace('@', '_').replace('.', '_')
		return email
	
	def get_messages_id(self):
		headers = {
			'Host': 'mail-server.1timetech.com',
			'Accept': 'application/json',
			'X-App-Key': 'f07bed4503msh719c2010df3389fp1d6048jsn411a41a84a3c',
			'User-Agent': 'TemporaryEmailPro/308301032 CFNetwork/1410.0.3 Darwin/22.6.0',
			'Accept-Language': 'en-US,en;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
		}
		for _ in range(int(self.timeout / 3)):
			time.sleep(3)
			try:
				req = self.req.get(f'https://mail-server.1timetech.com/api/email/{self.email_id}/messages?params=%3D03e', headers=headers)
				# print(req.json())
				if req.json()['data'] != '':
					messages = json.loads(self.base64_decode(req.json()['data']))
					for message in messages:
						if f'{self.text_from_message}' in str(message):
							return message['id']
			except:
				continue
	
	def read_message(self):
		headers = {
			'Host': 'mail-server.1timetech.com',
			'Accept': 'application/json',
			'X-App-Key': 'f07bed4503msh719c2010df3389fp1d6048jsn411a41a84a3c',
			'User-Agent': 'TemporaryEmailPro/308301032 CFNetwork/1410.0.3 Darwin/22.6.0',
			'Accept-Language': 'en-US,en;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
		}
		try:
			res = self.req.get(f'https://mail-server.1timetech.com/api/email/{self.email_id}/messages/{self.get_messages_id()}', headers=headers)
			message = json.loads(self.base64_decode(res.json()['data']))
			return message
		except Exception as e:
			raise Exception('Cant Get Otp.')
	
	def otp(self, length):
		try:
			message = self.read_message()
			pattern = '(\d{' + str(length) + '})'
			matches = re.findall(pattern, str({message}))
			if len(matches) >= 1:
				return matches
			else:
				raise Exception('Cant Get Otp.')
		except:
			raise Exception('Cant Get Otp.')
	
	def link(self):
		try:
			message = self.read_message()
			# print(message)
			pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
			urls = re.findall(pattern, message['html'])
			# print(urls)
			if len(urls) >= 1:
				return urls
			else:
				raise Exception('Cant Get email links.')
		except:
			raise Exception('Cant Get email links.')
	
	def otp_mix(self, length: int):
		try:
			message = self.read_message()
			# print(message)
			pattern = r'([0-9a-fA-F]+)'
			matches = re.findall(pattern, message['html'])
			valid_codes = [code for code in matches if len(code) == length and code != 'ffffff']
			return valid_codes
		except:
			raise Exception('Cant Get Otp.')
