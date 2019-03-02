from setuptools import setup

setup(
    name='gsheets-assistant',
    version='0.1',
    description='GSheets API assistant, with formatter and cell navigation tools',
    url='https://github.com/dreadpirateshawn/gsheets-assistant',
    author='Shawn Falkner-Horine',
    author_email='dreadpirateshawn@gmail.com',
    license='MIT',
    packages=[
        'gsheets_assistant',
    ],
    test_suite="tests",
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'oauth2client',
    ],
    entry_points={'console_scripts': [
        'gsheets-assistant-demo = gsheets_assistant.__demo__:main',
    ]},
    zip_safe=False,
)
