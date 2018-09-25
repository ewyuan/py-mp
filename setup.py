from setuptools import setup

setup(
    name='py-mp',
    packages=['pymp'],
    author='EddyMaric, ewyuan',
    author_email='eddy.maric98@gmail.com, eric.yuan@mail.utoronto.ca',
    description='A simple command-line music player',
    long_description='py-mp, short for python music player, uses command-line to take in inputs from the user and makes a search query on Youtube. py-mp will pull the most relevant video and will stream the audio to the computer.',
    license='MIT',
    url='http://github.com/ewyuan/py-mp',
    entry_points={
        'console_scripts': [
            'py-mp = pymp.__main__:main'
        ]
    },
    version='1.1',
    install_requires=['python-vlc', 'requests', 'beautifulsoup4', 'pafy', 'youtube-dl'],
)
