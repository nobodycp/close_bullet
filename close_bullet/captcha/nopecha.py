import nopecha
from .. import userdata


class Nopecha:
    nopecha.api_key = userdata['Captcha.nopecha']

    @staticmethod
    def text_captcha(image_as_base64):
        try:
            text = nopecha.Recognition.solve(
                type='textcaptcha',
                image_data=[f'{image_as_base64}'],
            )
            return text[0]
        except:
            raise Exception("Nopecha Error")

    @staticmethod
    def reCAPTCHA2(url, key):
        try:
            token = nopecha.Token.solve(
                type='recaptcha2',
                sitekey=f'{key}',
                url=f'{url}',
            )
            print(token)
        except:
            raise Exception("Nopecha Error")

    @staticmethod
    def reCAPTCHA3(url, key, action='check'):
        try:
            token = nopecha.Token.solve(
                type='recaptcha2',
                sitekey=f'{key}',
                url=f'{url}',
                data={
                    'action': f'{action}',
                }
            )
            print(token)
        except:
            return "nopecha Error ...."
