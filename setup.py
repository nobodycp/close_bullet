import setuptools
setuptools.setup(
    name='close_bullet',
    version='0.1',
    author='NoBody_cp',
    install_requires=[
        'wexpect',
        'requests',
        'names',
        'phonenumbers',
        'pycountry',
        'phone_iso3166',
        'cloudscraper',
        'nopecha',
        '1stcaptcha',
        '2captcha-python',
        'pysocks',
        'pyinstaller',
    ],
    description='Privet Library For 01 Team',
    packages=setuptools.find_packages(),
)
