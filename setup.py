from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyamplitude',
    version='1.0.0',
    description='A Python connector for Amplitude Analytics',
    long_description=long_description,
    url='https://github.com/marmurar/pyamplitude',
    author='Marcos Manuel Muraro',
    author_email='mmmuraro@gmail.com',
    license='MIT',
    install_requires=[
        'simplejson',
        'cachetools',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Data Analysis Amplitude Rest Api Amplitude Redshift',
    packages=find_packages(exclude=['tutorial', 'tests'])
)
