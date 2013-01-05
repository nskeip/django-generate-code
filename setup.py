from setuptools import setup, find_packages

setup(
    name='django-generate-code',
    version='0.1.2',
    author='Nikita Hismatov',
    author_email='me@ns-keip.ru',
    url = 'http://github.com/nskeip/django-generate-code/',
    description = 'django-generate-code lets you generate code '
                'in your django projects straight from the '
                'command line',
    packages=find_packages(),
)
