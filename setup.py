from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

#with open('LICENSE') as license_file:
    #license = license_file.read()

setup(name='junk-email-collector',
      version='0.1.1',
      description='Download raw Junk/Spam emails using IMAP.',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/wesinator/junk-email-collector',
      author='wesinator',
      keywords='spam',
      packages=find_packages(exclude=('tests', 'docs')),
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],
      zip_safe=True)
