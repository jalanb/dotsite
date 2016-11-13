"""Set up the dotsite project"""


from setuptools import setup


import dotsite
from pip.req import parse_requirements


setup(
    name=dotsite.__name__,
    packages=[dotsite.__name__],
    version=dotsite.__version__,
    url='https://github.com/jalanb/%s' % dotsite.__name__,
    download_url='https://github.com/jalanb/%s/tarball/v%s' % (
        dotsite.__name__, dotsite.__version__),
    license='MIT License',
    author='J Alan Brogan',
    author_email='github@al-got-rhythm.net',
    description=dotsite.__doc__,
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
    ],
    install_requires=[str(_.req) for _ in parse_requirements(
        dotsite.paths.path(__file__).parent / 'requirements.txt')],
    test_suite='nose.collector',
    tests_require=['nose'],
    extras_require={
        'testing': ['nose'],
    }
)
