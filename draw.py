#!/usr/bin/python2

from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import sys
import getopt
import seaborn

def DrawALine(x0, y0, x1, y1, w, c, ax):
    line = [(x0, y0), (x1, y1)]
    (line_xs, line_ys) = zip(*line)
    ax.add_line(Line2D(line_xs, line_ys, linewidth=w, color=c))

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:w:h:s:")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    finpath = None
    foutpath = None
    width = 10
    height = 5
    span = None

    for o, a in opts:
        if o == "-i":
            finpath = a
        elif o == "-o":
            foutpath = a
        elif o == "-w":
            width = float(a)
        elif o == "-h":
            height = float(a)
        elif o == "-s":
            span = float(a)
        else:
            assert False, "unhandled option"

    if finpath is None:
        print "usage: ./draw.py -i <input_filename>" 
        print "                 -o <output_filename>"
        print "                 -w <figure_width>"
        print "                 -h <figure_height>"
        print "                 -s <horizontal span>"
        assert False

    fin = open(finpath, 'r')

    fnum = int(fin.readline().strip())
    begin = []
    end = []

    very_begin = sys.float_info.max
    very_end = -sys.float_info.max

    for i in range(fnum):
        curb = []
        cure = []
        stepnum = int(fin.readline().strip())
        for j in range(stepnum):
            data = fin.readline().strip().split()
            bstamp = float(data[0])
            estamp = float(data[1])
            curb.append(bstamp)
            cure.append(estamp)
            if bstamp < very_begin:
                very_begin= bstamp
            if estamp > very_end:
                very_end = estamp
        begin.append(curb)
        end.append(cure)

    if span is None:
        span = very_end - very_begin

    plt.figure(figsize=(width, height))
    plt.grid(False)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim(0, span)
    plt.ylim(0, fnum+1)

    colors = []
    allcolors = seaborn.xkcd_rgb.keys()
    for i in range(fnum):
        colors.append(seaborn.xkcd_rgb[allcolors[i]])

    for i in range(fnum):
        stepnum = len(begin[i])
        for j in range(stepnum):
            y0 = (begin[i][j] - very_begin)
            y1 = (end[i][j] - very_begin)
            DrawALine(y0, i+1, y1, i+1, 5, colors[i], ax)

    plt.plot()
    if foutpath is None:
        plt.show()
    else:
        plt.savefig(foutpath)
