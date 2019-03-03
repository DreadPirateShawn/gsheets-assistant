from setuptools import setup, find_packages

def read_version():
    return open('VERSION').read().strip()

setup(
    name='gsheets-assistant',
    version=read_version(),
    description='GSheets API assistant, with formatter and cell navigation tools',
    url='https://github.com/dreadpirateshawn/gsheets-assistant',
    author='Shawn Falkner-Horine',
    author_email='dreadpirateshawn@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'oauth2client',
    ],
    zip_safe=False,
)
