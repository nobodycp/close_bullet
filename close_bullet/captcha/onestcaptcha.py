from .. import userdata
#from onest_captcha import OneStCaptchaClient

#client = OneStCaptchaClient(apikey=userdata['Captcha.1st_captcha'])


class OneStCaptcha:
    @staticmethod
    def text_captcha(image_as_base64):
        try:
            result = client.image_to_text(base64img=image_as_base64)
            if result["code"] == 0:  # success:
                # print(result["token"])
                return result['token']
            else:  # wrong
                raise Exception(result['messeage'])
        except Exception as e:
            raise Exception(f"OneStCaptcha ....{e}")

    @staticmethod
    def reCAPTCHA2(url: str, key: str, invisible: bool = False) -> str:
        try:
            result = client.recaptcha_v2_task_proxyless(site_url=url, site_key=key, invisible=invisible)
            if result["code"] == 0:  # success:
                return result["token"]
            else:  # wrong
                raise Exception(result["messeage"])
        except Exception as e:
            raise Exception(f"OneStCaptcha Error ....{e}")

    @staticmethod
    def reCAPTCHA3(url, key, action='check'):
        try:
            result = client.recaptcha_v3_task_proxyless(site_url=url, site_key=key, page_action=action)
            if result["code"] == 0:  # success:
                return result["token"]
            else:  # wrong
                raise Exception(result["messeage"])
        except Exception as e:
            raise Exception(f"OneStCaptcha Error ....{e}")

    @staticmethod
    def reCAPTCHA3_Enterprise(url: str, key: str, action='check'):
        try:
            result = client.recaptcha_v3_enterprise_task_proxyless(site_url=url, site_key=key, page_action=action)
            if result["code"] == 0:  # success:
                return result["token"]
            else:  # wrong
                raise Exception(result["messeage"])
        except Exception as e:
            raise Exception(f"OneStCaptcha Error ....{e}")
