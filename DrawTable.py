from prettytable import PrettyTable


class Item:

    def __init__(self, key_, func_):
        self.key = key_
        self.func = func_
        self.records = []

    def process_a_line(self, line_):
        if line_.find(self.key) != -1:
            self.records.append(self.func(line_))


def get_root(line_):
    return int(line_.strip().split('/')[-1].split('.')[0])


def get_lbs(line_):
    return int(line_.strip().split('/')[-1].split('.')[1])


def last_float_space(line_):
    return float(line_.strip().split(' ')[-1])


class Items:

    items = {}

    def __init__(self):
        pass

    def register(self, name, key, func):
        self.items[name] = Item(key, func)

    def parse(self, fname):
        fin_ = open(fname, 'r')
        keys = self.items.keys()
        for line_ in fin_.readlines():
            for key in keys:
                self.items[key].process_a_line(line_)


def ATable(roots, lbs, data):
    root_list = []
    for r in roots.records:
        if r not in root_list:
            root_list.append(r)
    root_list.sort()
    lb_list = []
    for lb in lbs.records:
        if lb not in lb_list:
            lb_list.append(lb)
    lb_list.sort()
    dnum = len(data.records)
    rnum = len(root_list)
    lnum = len(lb_list)
    mat = [[0 for _ in range(rnum)] for _ in range(lnum)]
    for i in range(dnum):
        x = root_list.index(roots.records[i])
        y = lb_list.index(lbs.records[i])
        mat[y][x] = data.records[i]
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
    for r in roots.records:
        if r not in root_list:
            root_list.append(r)
    root_list.sort()
    lb_list = []
    for lb in lbs.records:
        if lb not in lb_list:
            lb_list.append(lb)
    lb_list.sort()
    item_num = len(data)
    item_name = data.keys()
    dnum = len(data[item_name[0]].records)
    rnum = len(root_list)
    lnum = len(lb_list)
#    print dnum, "==", rnum, "*", lnum
    assert dnum == rnum*lnum
    avgs = []
    for iname in item_name:
        datum = data[iname]
        curavg = []
        mat = [[0 for _ in range(rnum)] for _ in range(lnum)]
        for i in range(dnum):
            x = root_list.index(roots.records[i])
            y = lb_list.index(lbs.records[i])
            mat[y][x] = datum.records[i]
        for i in range(lnum):
            curavg.append(float(sum(mat[i]))/float(len(mat[i])))
        avgs.append(curavg)
    head = ['lower_bound'] + item_name
    table = PrettyTable(head)
    for i in range(lnum):
        table.add_row([lb_list[i]] + [avgs[j][i] for j in range(item_num)])
    return table


if __name__ == "__main__":
    items = Items()
    items.register('roots', 'query_info=file', get_root)
    items.register('lbs', 'query_info=file', get_lbs)
    items.register('total-time', 'grape-total-time', last_float_space)
    items.register('message-num', 'metric.cc:264', last_float_space)
    items.register('message-len', 'metric.cc:217', last_float_space)
    items.register('avg-thread-time', 'avg-thread-time', last_float_space)
    items.register('max-thread-time', 'max-thread-time', last_float_space)
    items.register('aggregated-message-num', 'aggregated', last_float_space)
    items.register('iter-num', 'iter num', last_float_space)
    items.parse('./nohup.out')
    tab = BTable(items.items['roots'], items.items['lbs'], dict((k, items.items.get(k)) for k in ['total-time', 'avg-thread-time', 'aggregated-message-num', 'max-thread-time', 'iter-num', 'message-len']))
    print tab
 #   tab1 = ATable(items.items['roots'], items.items['lbs'], items.items['total-time'])
 #   print tab1