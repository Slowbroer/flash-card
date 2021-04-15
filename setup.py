from setuptools import find_packages, setup

setup(
    name='flash_card',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'Flask-Cache',
        'Flask-JSON',
        'Flask-JWT',
        'Flask-Login',
        'Flask-Migrate',
        'flask-redis',
        'Flask-Script',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'flask-zookeeper',
    ],
)