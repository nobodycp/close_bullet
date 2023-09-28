import time, re
from .. import  Requests, Randoms


class Onesecmail:
	def __init__(self, full_name: str, text_from_message: str, timeout: int = 20):
		self.full_name = full_name
		self.timeout = timeout
		self.text_from_message = text_from_message
		self.domain_list = self.domain_list()
		self.s = Requests.proxy_session()
		self.email: str = self.make_email()
	
	@classmethod
	def domain_list(cls) -> list:
		try:
			req = Requests.proxy_session(Proxy=True).get('https://www.1secmail.com/api/v1/?action=getDomainList')
			# print(req.text)
			return req.json()
		except Exception:
			raise Exception("connection error in 1secmail server.")
	
	def make_email(self):
		_ = Randoms.from_list(['_', '.', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		login = self.full_name.replace(' ', _).lower()
		email = login + '@' + Randoms.from_list(self.domain_list)
		return email
	
	def get_message_id(self):
		login, domain = self.email.split("@")
		# print(self.email)
		for _ in range(int(self.timeout / 3)):
			time.sleep(3)
			try:
				req = self.s.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
				# print(req.text)
				for message in req.json():
					# print(message)
					if self.text_from_message in str(message):
						message_body = self.s.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message["id"]}')
						# print(message_body.text)
						if 'htmlBody' in message_body.text:
							# print(message_body.text)
							return message_body.json()
			except:
				continue
	
	def otp(self, length):
		try:
			message = self.get_message_id()
			# print(message['htmlBody'])
			pattern = '(\d{' + str(length) + '})'
			matches = re.findall(pattern, str({message['htmlBody']}))
			if len(matches) >= 1:
				return matches
			else:
				raise Exception('Cant Get Otp.')
		except:
			raise Exception('Cant Get Otp.')
	
	def link(self):
		try:
			message = self.get_message_id()
			# print(message['body'])
			pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
			urls = re.findall(pattern, message['htmlBody'])
			if len(urls) >= 1:
				return urls
			else:
				raise Exception('Cant Get email links.')
		except:
			raise Exception('Cant Get email links.')
