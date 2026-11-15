def test_captcha_classes_import(cb_env):
    from close_bullet.captcha import Nopecha, Recaptcha3Pypass, TowCaptcha

    assert Nopecha.__name__ == "Nopecha"
    assert Recaptcha3Pypass.__name__ == "Recaptcha3Pypass"
    assert TowCaptcha.__name__ == "TowCaptcha"