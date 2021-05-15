from setuptools import setup, find_packages

setup(
    name='t3cpo',
    packages=find_packages(exclude=['tests', '.github']),
    version='0.1',
    license='MIT',
    description='Python wrapper for the several 3Commas api endpoints',
    author='mmeijden',
    author_email='me@mmeijden.nl',  # Type in your E-Mail
    url='https://github.com/mMeijden/three3cpo',
    keywords=['api', 'wrapper', '3c', '3Commas', 'crypto', 'bitcoin', 'altcoin', 'bots', 'exchange', 'trading'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
