try:
    import cProfile as profile
except ImportError:
    import profile

import logging
import pstats
import sys


NUM_EXPENSIVE = 20
DEFAULT_SORTING = 'cumulative'


class Profiler(object):
    """Code profiler
    """

    def __init__(self):
        self.tmp_prof = mktemp()
        self.tmp_stats = mktemp()

    def run_script(self, script):
        profile.run(script)

    def run(self, statement, globs, locs, progname):
        code = compile(statement, progname, 'exec')
        # writing to file
        logger.debug("writing to file %s" % self.tmp_prof)
        profile.runctx(code, globals=globs, locals=locs,
                       filename=self.tmp_prof)
        # print out the first 20 bad expensive things
        # self.prof.create_stats()

    def show_output(self, num=NUM_EXPENSIVE, sort=DEFAULT_SORTING):
        pt = pstats.Stats(self.tmp_prof)
        pt.sort_stats(sort)
        print(pt.print_stats(num))

    def dump_stats(self, filename):
        """Dump statistics out to file
        """
        pt = pstats.Stats(self.tmp_prof)
        logger.info("writing stats to file %s" % filename)
        pt.dump_stats(filename)


class StatsParser(object):
    def __init__(self, filename):
        self.filename = filename
        # handle possible problems in the parsing
        logger.debug("Analyzing stats from file %s" % filename)
        self.stats = pstats.Stats(filename)
        # initialize all the lines
        self.nodes = [StatNode.parse_node(x)
                      for x in self.stats.stats.iteritems()]

    @classmethod
    def to_callgraph(cls, stat, grouping):
        """Create a callgraph (just a dictionary) from the stats collected, linking
        together the lines.  There can be various ways to group things.
        - clusters (which have to be passed in?)
        - module
        - function
        - line
        """
        # should I group together the modules or just the functions
        for node in stat.nodes:
            pass

    @classmethod
    def to_org_mode(cls, callgraph):
        """Create an org-mode output for the statistic class
        """


class StatFunction(object):
    def __init__(self, func):
        self.file, self.line, self.func = func

    def __str__(self):
        return "%s:%d, %s" % (self.file, self.line, self.func)


#TODO: add some filtering and grouping features, and differences for example we can show
#the total performance change and where exactly it changed
class StatNode(object):
    """Line in the statistic, making clear what are all the fields
    Every line identifies one and only one element which might be connected with other elements, so
    it could be hashable and used as a key for further analysis
    """
    def __init__(self, fn, cc, nc, tt, ct, callers):
        """
        - fn: function
        - cc: cumulative call count (is this correct??)
        - nc: number of calls
        - tt: total time
        - ct: cumulative time
        - callers: list of callers
        """
        self.fn = StatFunction(fn)
        self.cc = cc
        self.nc = nc
        self.tt = tt
        self.ct = ct
        # callers are also functions in a way
        self.callers = callers

    @classmethod
    def parse_node(cls, item):
        fn, (cc, nc, tt, ct, callers) = item
        return StatNode(fn, cc, nc, tt, ct, callers)


class StatDiff(object):
    """Class type used to see the differences between different profiling graphs
    """
    pass
