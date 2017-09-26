import sys

if __name__ == "__main__":
    fin = open(sys.argv[1], 'r')
    for line in fin.readlines():
        dst = [ int(x) for x in line.strip().split(':')[0].strip().split(' ') ]
        events = [ int(x) for x in line.strip().split(':')[1].strip().split(' ') ]
        buf = {}
        for i in dst:
            buf[i] = []
        cur = {}
        for i in dst:
            cur[i] = []
        enum = len(events)
        for i in range(enum):
            e = events[i]
            if e < 0:
                e = -events[i]
            if e in dst:
                buf[e].append(len(cur[e]))
                cur[e] = []
            else:
                for j in dst:
                    if e not in cur[j]:
                        cur[j].append(e)
        for i in dst:
            step_num = len(buf[i])
            print '[fragment-', i, ']: ', step_num, ' steps'
            for j in range(step_num):
                print '\tstep-', j, ': ', buf[i][j]
            print ' '

