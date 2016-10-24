from setuptools import setup

setup(name='C2PAP-bibtex',
      author='Frederik Beaujean',
      py_modules=['c2pap_style'],
      entry_points = {
          'pybtex.style.formatting': 'C2PAP = c2pap_style:C2PAP',
          'pybtex.backends': 'typo3 = c2pap_style:Backend',
      },
      install_requires=['pybtex>=0.20'],
)
