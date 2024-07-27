
tasks = ["A", "B", "C", "D", "E", "F", "G", "H", "ARTI"]
duration = [6, 4, 3, 4, 3, 10, 3, 2, 0]
predecessors = [[], [], ["A"], ["B"], ["B"], [], ["E", "F"], ["C", "D"]]



from collections import deque

est = [None for _ in range(len(tasks))]
eft = [None for _ in range(len(tasks))]
lst = [None for _ in range(len(tasks))]
lft = [None for _ in range(len(tasks))]
successors = [[] for _ in range(len(tasks))]


def m(s):
    return tasks.index(s)


for pred_list_i in range(len(predecessors)):
    for pred in predecessors[pred_list_i]:
        if successors[m(pred)] is None:
            successors[m(pred)] = []
        successors[m(pred)].append(tasks[pred_list_i])


def forward_pass():
    queue = deque()
    for x in range(len(predecessors)):
        if x == "ARTI":
            continue
        if not predecessors[x]:
            queue.appendleft(tasks[x])
    while len(queue) != 0:
        x = queue.pop()
        predecessors_of_x = predecessors[m(x)]
        max_eft = 0
        for pred in predecessors_of_x:
            max_eft = max(max_eft, eft[m(pred)])
        est[m(x)] = max_eft
        eft[m(x)] = est[m(x)] + duration[m(x)]
        if not successors[m(x)]:
            continue
        for succ in successors[m(x)]:
            if succ == "ARTI":
                continue
            queue.appendleft(succ)


forward_pass("A")
max_eft = 0
for x in eft:
    if not x:
        continue
    if x > max_eft:
        max_eft = x


def backward_pass():
    queue = deque()
    temp_pred = []
    for x in range(len(successors)):
        if not successors[x]:
            eft[m(tasks[x])] = max_eft
            lft[m(tasks[x])] = max_eft
            lst[m(tasks[x])] = max_eft
            if(tasks[x] == "ARTI"):
                continue
            temp_pred.append(tasks[x])
    predecessors.append(temp_pred)
    successors.append([])
    queue.append('ARTI')
    while len(queue)!=0:
        x = queue.pop()
        successors_of_x = successors[m(x)]
        min_lst = lst[m('ARTI')]
        for succ in successors_of_x:
            min_lst = min(min_lst, lst[m(succ)])
        lft[m(x)] = min_lst
        lst[m(x)] = lft[m(x)] - duration[m(x)]
        if not predecessors[m(x)]:
            continue
        for pred in predecessors[m(x)]:
            queue.appendleft(pred)
        
backward_pass()


eft = eft[:-1]
lft = lft[:-1]
lst = lst[:-1]
est = est[:-1]


ans1 = max(eft[:-1])
ans2 = max(lft[:-1])

print(ans1)
print(ans2)


