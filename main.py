import math
import matplotlib.pyplot as plt
from adjustText import adjust_text


class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)


def astar(start, end):
    # 开始时，除了起始节点外，所有节点的已知距离是无穷大
    for node in nodes:
        node.distance = float("inf")

    # 起始节点的已知距离是 0
    start.distance = 0

    # 创建一个字典，用于存储每个节点的父节点，以便后面回溯路径
    parents = {}

    # 将起始节点加入开放列表中
    open_list = [start]

    while open_list:

        # 从开放列表中找到 f(n) 最小的节点
        current = min(open_list, key=lambda node: node.distance + node.h)

        # 如果该节点是终点，返回路径
        if current == end:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            return path[::-1]

        # 遍历当前节点的相邻节点
        for neighbor in current.neighbors:
            # 计算新的实际距离
            new_distance = current.distance + dist(current, neighbor)
            if new_distance < neighbor.distance:
                # 更新节点的实际距离
                neighbor.distance = new_distance

                # 将当前节点设置为其相邻节点的父节点
                parents[neighbor] = current

                # 如果节点尚未加入开放列表，将其加入
                if neighbor not in open_list:
                    open_list.append(neighbor)

        # 将当前节点从开放列表中移除
        open_list.remove(current)

    # 如果开放列表已空，但仍未找到终点，则返回 None
    return None


# 构造测试数据
node1 = Node('1', 71, 846)
node2 = Node('2', 93, 846)
node3 = Node('3', 106, 846)
node4 = Node('4', 126, 846)
node5 = Node('5', 146, 846)
node6 = Node('6', 166, 846)
node7 = Node('7', 186, 846)
node8 = Node('8', 210, 846)
node9 = Node('9', 234, 846)
node10 = Node('10', 259, 846)
node11 = Node('11', 363, 872)
node12 = Node('12', 383, 872)
node13 = Node('13', 403, 872)
node14 = Node('14', 423, 872)
node15 = Node('15', 443, 872)
node16 = Node('16', 466, 903)
node17 = Node('17', 536, 903)
node18 = Node('18', 913, 919)
node19 = Node('19', 913, 900)
node20 = Node('20', 1051, 919)
node21 = Node('21', 1051, 900)
node22 = Node('22', 1200, 950)
node23 = Node('23', 1200, 960)
node24 = Node('24', 1625, 967)
node25 = Node('25', 1625, 926)
node26 = Node('26', 1625, 885)
node27 = Node('27', 71, 794)
node28 = Node('28', 94, 794)
node29 = Node('29', 117, 794)
node30 = Node('30', 137, 794)
node31 = Node('31', 165, 794)
node32 = Node('32', 186, 794)
node33 = Node('33', 186, 846)
node34 = Node('34', 198, 794)
node35 = Node('35', 211, 794)
node36 = Node('36', 235, 794)
node37 = Node('37', 258, 794)
node38 = Node('38', 281, 846)
node39 = Node('39', 281, 794)
node40 = Node('40', 303, 794)
node41 = Node('41', 323, 794)
node42 = Node('42', 343, 794)
node43 = Node('43', 363, 794)
node44 = Node('44', 383, 794)
node45 = Node('45', 403, 794)
node46 = Node('46', 423, 794)
node47 = Node('47', 466, 794)
node48 = Node('48', 466, 846)
node49 = Node('49', 466, 850)
node50 = Node('50', 466, 862)
node51 = Node('51', 466, 872)
node52 = Node('52', 536, 862)
node53 = Node('53', 536, 831)
node54 = Node('54', 571, 831)
node55 = Node('55', 584, 831)
node56 = Node('56', 611, 831)
node57 = Node('57', 638, 831)
node58 = Node('58', 648, 831)
node59 = Node('59', 665, 831)
node60 = Node('60', 679, 831)
node61 = Node('61', 700, 831)
node62 = Node('62', 723, 831)
node63 = Node('63', 771, 831)
node64 = Node('64', 784, 831)
node65 = Node('65', 793, 831)
node66 = Node('66', 793, 844)
node67 = Node('67', 811, 844)
node68 = Node('68', 850, 844)
node69 = Node('69', 913, 844)
node70 = Node('70', 968, 844)
node71 = Node('71', 990, 844)
node72 = Node('72', 1051, 844)
node73 = Node('73', 1122, 844)
node74 = Node('74', 1161, 844)
node75 = Node('75', 1200, 844)
node76 = Node('76', 1200, 864)
node77 = Node('77', 1200, 884)
node78 = Node('78', 1200, 904)
node79 = Node('79', 1200, 924)
node80 = Node('80', 1200, 944)
node81 = Node('81', 1200, 908)
node82 = Node('82', 1200, 928)
node83 = Node('83', 545, 794)
node84 = Node('84', 611, 794)
node85 = Node('85', 724, 794)
node86 = Node('86', 793, 794)
node87 = Node('87', 913, 794)
node88 = Node('88', 1051, 794)
node89 = Node('89', 1090, 794)
node90 = Node('90', 1161, 794)
node91 = Node('91', 1200, 794)
node92 = Node('92', 1271, 794)
node93 = Node('93', 1285, 794)
node94 = Node('94', 1326, 794)
node95 = Node('95', 1370, 794)
node96 = Node('96', 1397, 794)
node97 = Node('97', 1419, 794)
node98 = Node('98', 1437, 794)
node99 = Node('99', 1463, 794)
node100 = Node('100', 1484, 794)
node101 = Node('101', 1509, 794)
node102 = Node('102', 1537, 794)
node103 = Node('103', 1571, 794)
node104 = Node('104', 1625, 794)
node105 = Node('105', 198, 715)
node106 = Node('106', 466, 715)
node107 = Node('107', 697, 715)
node108 = Node('108', 870, 715)
node109 = Node('109', 950, 715)
node110 = Node('110', 1127, 715)
node111 = Node('111', 1397, 715)
node112 = Node('112', 1571, 715)
node113 = Node('113', 612, 715)
node114 = Node('114', 800, 715)
node115 = Node('115', 1020, 715)
node116 = Node('116', 1200, 715)
node117 = Node('117', 1463, 715)
node118 = Node('118', 1571, 715)
node119 = Node('119', 51, 624)
node120 = Node('120', 198, 624)
node121 = Node('121', 414, 624)
node122 = Node('122', 598, 624)
node123 = Node('123', 775, 624)
node124 = Node('124', 1039, 624)
node125 = Node('125', 1222, 624)
node126 = Node('126', 1404, 624)
node127 = Node('127', 1605, 624)
node128 = Node('128', 1758, 624)
node129 = Node('129', 51, 552)
node130 = Node('130', 198, 552)
node131 = Node('131', 414, 552)
node132 = Node('132', 743, 552)
node133 = Node('133', 910, 552)
node134 = Node('134', 1073, 552)
node135 = Node('135', 466, 552)
node136 = Node('136', 1605, 552)
node137 = Node('137', 1758, 552)
node138 = Node('138', 198, 624)
node139 = Node('139', 477, 624)
node140 = Node('140', 660, 624)
node141 = Node('141', 1168, 624)
node142 = Node('142', 1352, 624)
node143 = Node('143', 1467, 624)
node144 = Node('144', 1625, 624)

# 加边
node1.add_neighbor(node2)
node1.add_neighbor(node27)

node2.add_neighbor(node3)
node2.add_neighbor(node28)

node3.add_neighbor(node4)
node3.add_neighbor(node29)

node4.add_neighbor(node5)
node4.add_neighbor(node30)

nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10,
         node11, node12, node13, node14, node15, node16, node17, node18, node19,
         node20, node21, node22, node23, node24, node25, node26, node27, node28,
         node29, node30, node31, node32, node33, node34, node35, node36, node37,
         node38, node39, node40, node41, node42, node43, node44, node45, node46,
         node47, node48, node49, node50, node51, node52, node53, node54, node55,
         node56, node57, node58, node59, node60, node61, node62, node63, node64,
         node65, node66, node67, node68, node69, node70, node71, node72, node73,
         node74, node75, node76, node77, node78, node79, node80, node81, node82,
         node83, node84, node85, node86, node87, node88, node89, node90, node91,
         node92, node93, node94, node95, node96, node97, node98, node99, node100,
         node101, node102, node103, node104, node105, node106, node107, node108,
         node109, node110, node111, node112, node113, node114, node115, node116,
         node117, node118, node119, node120, node121, node122, node123, node124,
         node125, node126, node127, node128, node129, node130, node131, node132,
         node133, node134, node135, node136, node137, node138, node139, node140,
         node141, node142, node143, node144]


# 计算两点之间的距离
def dist(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


# 开始搜索
start = node1
end = node30
for node in nodes:
    node.h = dist(node, end)

path = astar(start, end)

# 画出图形
fig, ax = plt.subplots(figsize=(20, 8), dpi=500)
for node in nodes:
    ax.plot(node.x, node.y, color="black", marker='.')

for node in nodes:
    ax.text(node.x, node.y, node.id, ha='center', va='bottom', color='green', size='5')
    for neighbor in node.neighbors:
        ax.plot([node.x, neighbor.x], [node.y, neighbor.y], color="black")

for i in range(len(path) - 1):
    ax.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], color="blue")

ax.set_xlim(left=-1, right=2000)
ax.set_ylim(bottom=500, top=1000)
ax.invert_yaxis()
plt.show()
