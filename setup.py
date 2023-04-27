from setuptools import setup, find_packages

setup(
    name='Django_Person_API',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Simple REST API built with Python, using the Django framework, MongoDB Atlas, JavaScript, HTML, CSS.',
    long_description='The CRUD operations (HTTP: POST, GET, DELETE, PUT) are contemplated.',
    author='Marcelo A. Paciulli',
    author_email='marcelopaciulli@gmail.com',
    install_requires=[
        'Django>=3.2',
        'djangorestframework>=3.14.0',
        'djongo>=1.3.6',
        'mongoengine>=0.27.0',
        'pymongo>=3.12.1',
        'pytz>=2023.3'
    ],
)
