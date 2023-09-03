import setuptools
setuptools.setup(
    name='close_bullet',
    version='0.1',
    author='NoBody_cp',
    install_requires=[
        'requests',
        'WMI',
        'pycountry',
        'phonenumbers',
        'nopecha',
	'pysocks',
        'names',
        'phone_iso3166',
        '1stcaptcha',
	'pyinstaller',
    ],
    description='Privet Library For 01 Team',
    packages=setuptools.find_packages(),
)
