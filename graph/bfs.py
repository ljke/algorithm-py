# coding=utf-8
from collections import deque

# 使用队列实现广度优先算法，基于图的最短路径求解方法

# 使用字典（散列表）存储图
graph = {}
graph["you"] = ["alice", "bob", "claire", "amy"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()  # 双端队列存储未遍历顶点
    searched = []  # 存储已遍历顶点，不重复查找
    prev = {}  # 记录搜索路径
    search_queue.append(name)
    searched.append(name)
    while search_queue:
        person = search_queue.popleft()
        # 检查邻居
        if graph.get(person):  # 检查对应键是否存在，不存在键表示是边界顶点
            for neighbour in graph.get(person):
                if neighbour not in searched:  # 只检查未检查过的邻居
                    prev[neighbour] = person  # 记录前驱顶点
                    if person_is_seller(neighbour):
                        print neighbour + ' is a mango seller!'
                        print_path(name, neighbour, prev)
                        return
                    else:
                        search_queue.append(neighbour)
                        searched.append(neighbour)
    print "No found"


# 打印搜索路径
def print_path(start, end, prev):
    if prev[end] and start != end:  # 递归结束条件
        print_path(start, prev.get(end), prev)
    print " -> ", str(end),


if __name__ == '__main__':
    search("you")
