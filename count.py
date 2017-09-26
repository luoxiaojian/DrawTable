if __name__ == '__main__':
#    fin = open('./twitter-sssp-1.step_detail', 'r')
    fin = open('5506215.step_detail', 'r')

    fnum = int(fin.readline().strip())
    stepnums = []

    for i in range(fnum):
        stepnum = int(fin.readline().strip())
        stepnums.append(stepnum)
        for j in range(stepnum):
            fin.readline()

    print stepnums
    print "max: " , max(stepnums)
    print "min: " , min(stepnums)


