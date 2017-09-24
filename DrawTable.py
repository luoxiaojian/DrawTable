from prettytable import PrettyTable

def ATable(roots, lbs, data):
#    root_list = [782658, 1752217, 1956543, 3391590, 5506215]
    root_list = []
    for r in roots:
        if r not in root_list:
            root_list.append(r)
    root_list.sort()
    lb_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    #lb_list = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', 'inf']
    dnum = len(data)
    rnum = len(root_list)
    lnum = len(lb_list)
    mat = [[0 for _ in range(rnum)] for _ in range(lnum)]
    for i in range(dnum):
        x = root_list.index(roots[i])
        y = lb_list.index(lbs[i])
        mat[y][x] = data[i]
    avg = []
    for i in range(lnum):
        s = sum(mat[i])
        avg.append(float(s)/float(len(mat[i])))
    head = ['lower_bound'] + root_list + ['average']
    table = PrettyTable(head)
    for i in range(lnum):
        table.add_row([lb_list[i]] + mat[i] + [avg[i]])
    return table

def BTable(roots, lbs, data):
    root_list = []
    lb_list = []
    item_num = len(data)
    item_name = data.keys()
    dnum = len(data[item_name[0]])
    for r in roots:
        if r not in root_list:
            root_list.append(r)
    root_list.sort()
    rnum = len(root_list)
    lb_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#    for l in lbs:
#        if l not in lb_list:
#            lb_list.append(l)
    lnum = len(lb_list)
    assert dnum == rnum*lnum
    avgs = []
    for iname in item_name:
        datum = data[iname]
        curavg = []
        mat = [[0 for _ in range(rnum)] for _ in range(lnum)]
        for i in range(dnum):
            x = root_list.index(roots[i])
            y = lb_list.index(lbs[i])
            mat[y][x] = datum[i]
        for i in range(lnum):
            curavg.append(float(sum(mat[i]))/float(len(mat[i])))
        avgs.append(curavg)
    head = ['lower_bound'] + item_name
    table = PrettyTable(head)
    for i in range(lnum):
        table.add_row([lb_list[i]] + [avgs[j][i] for j in range(item_num)])
    return table

if __name__ == "__main__":

    roots = []
    lbs = []
    times = []
    sizes = []
    lens = []
    fin = open('all.dat', 'r')
    data = {}
    data['total-time'] = []
    data['message-number'] = []
    data['message-size'] = []
    data['aggregated-msg-size'] = []
    data['avg-cpu-time'] = []
    data['max-cpu-time'] = []
    for line in fin.readlines():
        ldata = line.strip().split()
        roots.append(int(ldata[0]))
        lbs.append(ldata[1])
        data['total-time'].append(float(ldata[2]))
        data['message-number'].append(int(ldata[3]))
        data['message-size'].append(int(ldata[4]))
        data['aggregated-msg-size'].append(int(ldata[5]))
        data['avg-cpu-time'].append(float(ldata[6]))
        data['max-cpu-time'].append(float(ldata[7]))
    tab1 = ATable(roots, lbs, data['total-time'])
    print tab1
#    tab2 = ATable(roots, lbs, data['message-number'])
#    print tab2
#    tab3 = ATable(roots, lbs, data['message-size'])
#    print tab3
    tab5 = ATable(roots, lbs, data['aggregated-msg-size'])
    print tab5
    tab4 = BTable(roots, lbs, data)
    print tab4

