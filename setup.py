from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='crisnet.skin',
      version=version,
      description="Crisnet skin",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='crisnet skin theme affinitic',
      author='Affinitic Sprl',
      author_email='info@affinitic.be',
      url='http://www.crisnet.be',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['crisnet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
