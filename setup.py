import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-visitstat',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A django application allowing you to log all HTTP requests to your website.',
    long_description=README,
    url='https://fomalhaut.su/',
    author='Alexander Khlebushchev',
    author_email='mail@fomalhaut.su',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.13',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'geoip2==2.9.0',
        'django-crontab==0.7.1',
    ],
    package_dir={'visitstat': 'visitstat'},
    package_data={'visitstat': ['data/GeoLite2-City.mmdb']}
)
