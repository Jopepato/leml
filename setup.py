from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='leml',
      version='0.1',
      description='Python version of the LEML algorithm',
      long_description=readme(),
      url='https://github.com/AnthonyMRios/pyleml',
      author='Anthony Rios',
      author_email='anthonymrios@gmail.com',
      classifiers=[
          'Intended Audience :: Science/Research'
      ],
      packages=['pyleml'],
      zip_safe=False)