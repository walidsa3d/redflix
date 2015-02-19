try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='redflix', version='0.1',
    description='Stream videos from popular Reddit subs',
    long_description=('Stream videos from popular Reddit subs'),
    author='walidsa3d'
    author_email='walid.sa3d@gmail.com',
    url='https://github.com/walidsa3d/redflix',
    license='GPL V2',
    install_requires=[
        'inquirer', 
        'termcolor',
	'praw',
	'subprocess'
    ]

)
