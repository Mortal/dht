from __future__ import division
import sys
import matplotlib.pyplot as plt
import numpy


def main(filename, outfilename):
    data = numpy.genfromtxt(filename)

    # plot the graph and save it
    if filename == 'figure-1-data.txt':
        plt.suptitle('Memory allocated (log/log plot)')
        plt.ylabel('bytes of memory allocated')
    elif filename == 'figure-2-data.txt':
        plt.suptitle('Memory written (log/log plot)')
        plt.ylabel('bytes of memory written')
    plt.xlabel('number of entries')

    index = data[:,0]
    series1 = data[:,1]
    series2 = data[:,2]
    series3 = data[:,3]
    plt.loglog(index, series1, '-', color='#cccccc', label='dense_hash_map (open addressing)')
    plt.loglog(index, series2, 'b-', label='open addressing')
    plt.loglog(index, series3, 'r-', label='Close table')
    plt.legend(loc='upper left')
    plt.savefig(outfilename, format='png')

    # compute and print summary information about which is bigger
    r1 = []
    r2 = []
    for i, _, s1, s2 in data:
        if s1 > s2:
            r1.append(s1/s2)
        else:
            r2.append(s2/s1)

    r1avg = sum(r1)/len(r1) - 1 if len(r1) else 0
    r2avg = sum(r2)/len(r2) - 1 if len(r2) else 0
    r1f = len(r1)/len(data)
    r2f = len(r2)/len(data)
    print("Implementation 1 takes up more space {:.1%} of the time, by {:.1%}".format(r1f, r1avg))
    print("Implementation 2 takes up more space {:.1%} of the time, by {:.1%}".format(r2f, r2avg))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
