from setuptools import setup, find_packages

setup(
    name='django_generate_code',
    version='0.1.4',
    author='Nikita Hismatov',
    author_email='me@ns-keip.ru',
    url = 'http://github.com/nskeip/django-generate-code/',
    description = 'django-generate-code lets you generate code '
                'in your django projects straight from the '
                'command line',
    packages=find_packages(),
    zip_safe=False,
)
