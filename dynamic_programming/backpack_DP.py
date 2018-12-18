class Good(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return "[{}-{}]".format(self.weight, self.value)


def dynamic_programming(n, w, good_list):
    # type: (int, int, list) -> int
    """
    DC algorithm to solve backpack problem, store previous line and deduce current line,
    so it can not restore complete strategy,
    use two line to store result and selected respectively
    :param n: number of goods
    :param w: volume of package
    :param good_list: list of goods
    """
    # dummy head
    pre_result = [0] * (w + 1)  # store result
    pre_selected = [[] for i in range(w + 1)]  # store strategy
    result = pre_result[:]  # copy the list
    selected = [[] for i in range(w + 1)]  # new a list, it's important! prevent same object reference
    for i in range(0, n):  # row
        item_weight = good_list[i].weight
        for j in range(0, w + 1):  # column
            if j < item_weight:
                result[j] = pre_result[j]
                selected[j] = pre_selected[j][:]
            else:
                result[j] = max(good_list[i].value + pre_result[j - item_weight],
                                pre_result[j])  # max

                if result[j] != pre_result[j]:
                    selected[j].append(good_list[i])
                    selected[j].extend(pre_selected[j - item_weight])
                else:
                    selected[j] = pre_selected[j][:]
        print result
        # print the selected list
        for x in range(0, w + 1):
            for y in range(len(selected[x])):
                print str(selected[x][y]) + " ",
            print " | ",
        print ""
        pre_result = result[:]  # copy the list
        pre_selected = selected[:]  # copy the list
        selected = [[] for i in range(w + 1)]  # clear the list
    return result[w]


if __name__ == '__main__':
    good_list = [Good(1, 1000), Good(3, 2000), Good(2, 1500), Good(1, 1500)]
    print dynamic_programming(4, 4, good_list)
