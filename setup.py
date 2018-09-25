from setuptools import setup

setup(
    name='songify',
    packages=['songify'],
    author='EddyMaric, ewyuan',
    author_email='eddy.maric98@gmail.com, eric.yuan@mail.utoronto.ca',
    description='A simple command-line music player',
    long_description='Songify uses command-line to take in inputs from the user and makes a search query on Youtube. Songify will pull the most relevant video and will stream the audio to the computer.',
    license='MIT',
    url='http://github.com/ewyuan/songify',
    entry_points={
        'console_scripts': [
            'songify = songify.__main__:main'
        ]
    },
    version='1.0',
    install_requires=['python-vlc', 'requests', 'beautifulsoup4', 'pafy', 'youtube-dl'],
)
