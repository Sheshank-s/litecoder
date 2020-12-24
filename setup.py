from distutils.core import setup


setup(
  name = 'litecoder',         # How you named your package folder (MyLib)
  packages = ['litecoder'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'US city + state geocoding, without a heavy webservice.',   # Give a short description about your library
  author = 'Laboratory for Social Machines, MIT Media Lab',                   # Type in your name
  author_email = 'wesc@media.mit.edu',      # Type in your E-Mail
  url = 'https://github.com/davidmcclure/litecoder',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Sheshank-s/litecoder/archive/v1.0.tar.gz',    # I explain this later on
  keywords = ['state', 'country', 'geocoding'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'marisa-trie>=0.7.5',
          'ujson',
          'tqdm',
          'cached_property',
          'sqlalchemy',
          'download'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
