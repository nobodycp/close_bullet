from .. import userdata
from twocaptcha import TwoCaptcha as twoCaptcha


class TowCaptcha:
	def __init__(self):
		self.solver = twoCaptcha(userdata['Captcha.2captcha'])
	
	def text_captcha(self, image_as_base64, **kwargs):
		try:
			result = self.solver.normal(
				image_as_base64,
				**kwargs
			)
			return result
		except Exception as e:
			print(e)
			raise Exception("Nopecha Error")