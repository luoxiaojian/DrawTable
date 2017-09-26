from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import sys
import seaborn

def DrawALine(x0, y0, x1, y1, w, c, ax):
    line = [(x0, y0), (x1, y1)]
    (line_xs, line_ys) = zip(*line)
    ax.add_line(Line2D(line_xs, line_ys, linewidth=w, color=c))

if __name__ == '__main__':
#    fin = open('./twitter-sssp-1.step_detail', 'r')
#    fin = open('5506215.step_detail', 'r')
#    fin = open('./tmp/twitter-sssp-1.step_detail', 'r')
#    fin = open('./cf-aap-async-ttl_1/5506215.step_detail', 'r')
    fin = open(sys.argv[1], 'r')

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

    span = very_end - very_begin
#    mult = 100.0 / span
    mult = 1

    figure, ax = plt.subplots()
    ax.set_xlim(left = 0, right = fnum+1)
#    ax.set_ylim(bottom = 0, top = 100)
    ax.set_ylim(bottom = 0, top = span)

    colors = []
    allcolors = seaborn.xkcd_rgb.keys()
    for i in range(fnum):
        colors.append(seaborn.xkcd_rgb[allcolors[i]])

    for i in range(fnum):
        stepnum = len(begin[i])
        for j in range(stepnum):
            y0 = mult * (begin[i][j] - very_begin)
            y1 = mult * (end[i][j] - very_begin)
            DrawALine(i+1, y0, i+1, y1, 5, colors[i], ax)

    plt.plot()
    plt.show()

