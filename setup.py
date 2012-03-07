from setuptools import setup

package = 'pyprofile'
version = '0.1'

entry_points = {
    'console_entry_points' : [
        'pyprofile: pyprof.cmdline:main'
    ]
}

# TODO: add authoring info
setup(name=package,
      version=version,
      description="analyze the results of the python profiler")
