#!/usr/bin/env python

from distutils.core import setup

if __name__=='__main__':
    setup(name='wubwubwub',
          description='Twisted Web Server',
           long_description="""

The necessary configuration files and harness to use the Twisted asynchronous
network framework to serve HTTP. Supports named virtual hosting, CGI
and serving user content, including a secure way for users to handle dynamic
web pages in their personal directory.

""".strip(),
	  author="Tommi Virtanen",
	  author_email="tv@debian.org",
	  url="http://www.inoi.fi/open/wubwubwub/",
	  license="GNU LGPL",

          packages=['wubwubwub',
                    ],
          )
