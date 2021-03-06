from __future__ import division
import sys
import matplotlib.pyplot as plt
import numpy
import json


def main(filename):
    with open(filename) as f:
        data = json.load(f)

    # plot the graph and save it
    for testname, results in data.items():
        fig = plt.figure()
        fig.suptitle(testname)
        axes = fig.gca()
        axes.set_ylabel('throughput (million operations/second)')
        hi = max(max(x/y/1e6 for x, y in series) for series in results.values())
        axes.set_ylim(bottom=0, top=hi * 1.2)
        axes.set_xlabel('number of operations (millions)')

        def show(data, *args, **kwargs):
            xs = [x/1e6 for x, y in data]
            ys = [x/y/1e6 for x, y in data]
            axes.plot(xs, ys, *args, **kwargs)

        if 'DenseTable' in results:
            show(results['DenseTable'], '-o', color='#cccccc', label='dense_hash_map (open addressing)')
        show(results['OpenTable'], 'b-o', label='open addressing')
        show(results['CloseTable'], 'r-o', label='Close table')
        axes.legend(loc='best')
        fig.savefig(testname + "-speed.png", format='png')


if __name__ == "__main__":
    main(sys.argv[1])
