"""عقد استخدام App.py — استيراد وإنشاء كائنات دون تشغيل send."""


def test_app_import_pattern(cb_env):
    from close_bullet import Requests, Phone, Options, FakeInfo, Randoms, temp_folder
    from close_bullet.captcha import Recaptcha3Pypass

    Phone("972567108204")
    FakeInfo()
    Options.parse_text("a=1&b=2", "a=", "&")
    Randoms.device_id()
    assert Requests.proxy_session() is not None
    assert temp_folder
    # تهيئة الصنف فقط (لا استدعاء response بدون URLs)
    assert Recaptcha3Pypass.__name__ == "Recaptcha3Pypass"