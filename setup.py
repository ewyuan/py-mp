from setuptools import setup

setup(
    name='songify',
    packages=['songify'],
    author='EddyMaric, ewyuan',
    author_email='eddy.maric98@gmail.com, eric.yuan@mail.utoronto.ca',
    description='A simple command-line music player',
    url='http://github.com/ewyuan/songify',
    entry_points={
        'console_scripts': [
            'songify = songify.__main__:main'
        ]
    },
    version='1.0',
    install_requires=['python-vlc', 'requests', 'beautifulsoup4', 'pafy'],
)