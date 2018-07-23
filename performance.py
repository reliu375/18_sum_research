import focaltrack
import cProfile
import pstats
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()
cProfile.run(focaltrack.multithreading_test())
pr.disable()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()