from distutils.core import setup

setup(name='ScrapyCouchDB',
      version='0.2',
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allow you to store scrapy items in CouchDB database.',
      author='Julien Duponchelle',
      author_email='julien@duponchelle.info',
      url='http://github.com/noplay/scrapy-couchdb',
      keywords="scrapy couchdb",
      py_modules=['scrapycouchdb'],
      platforms = ['Any'],
      install_requires = ['scrapy', 'couchdb'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
