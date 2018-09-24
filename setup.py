from setuptools import setup

setup(
    name='music-player',
    packages=['music-player'],
    author='EddyMaric, ewyuan',
    author_email='nishanpantha@gmail.com',
    description='A command-line music player',
    url='http://github.com/ewyuan/music-player',
    entry_points={
        'console_scripts': [
            'music-player = music-player.run:main'
        ]
    },
    version='1.0',
    install_requires=['python-vlc', 'requests', 'beautifulsoup4', 'pafy'],
)