from setuptools import setup, find_packages

package = 'pyprofile'
version = '0.1'

entry_points = {
    'console_scripts' : [
        'pyprofile = pyprof.cmdline:main'
    ]
}

# TODO: add authoring info
setup(author='Andrea Crotti',
      author_email='andrea.crotti.0@gmail.com',
      name=package,
      version=version,
      entry_points=entry_points,
      packages=find_packages(),
      description="analyze the results of the python profiler")
