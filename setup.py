from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='filthypasswordgenerator',
    version='1.4',
    description='The filthiest passwords imaginable',
    long_description=long_description,
    author='Mark',
    author_email='banreaxe@gmail.com',
    url='https://github.com/banreaxe/filthy-password-generator-py',
    license='MIT',
    packages=['filthypasswordgenerator', 'filthypasswordgenerator.data'],
    package_dir={'filthypasswordgenerator': 'src'},
    install_requires=['argparse'],  # external dependencies
    entry_points={
        'console_scripts': [
            'filthypasswordgenerator = filthypasswordgenerator.pwgenerator:main',
        ],
    },
    classifiers=[  # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        #  'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
    ],
)
