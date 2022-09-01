from setuptools import setup, find_packages

setup(
    name= 'webx',
    description= 'a package to monitor web sites and report their availability',

    version= '0.0.1' ,
    author= 'Sara' ,

    author_email= 'maryamhanifpour@gmail.com',
    url= 'https://github.com/maryamhanifpour/webx',

    packages=find_packages(where= 'src' ),
    package_dir={ '' : 'src' },
)