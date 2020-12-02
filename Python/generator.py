import random
from collections import deque

def chance(prob):
    if random.random() < prob:
        return True
    else:
        return False

def generate(file_name, num_of_node=10000, degree=3, numHospital=1):
    LENGTH = num_of_node
    PROB = 0.9
    DIMINISH = (1.0 - 1.0/degree + 0.0001)
    numOfHospital = numHospital

    newGraph = 1

    while newGraph:
        res = []

        for i in range(LENGTH):
            r = PROB
            x = int(random.random() * LENGTH)
            while x == i:
                x = int(random.random() * LENGTH)
            res.append((i, x))
            res.append((x, i))
            while (chance(r)):
                x = int(random.random() * LENGTH)
                while x == i:
                    x = int(random.random() * LENGTH)
                res.append((i, x))
                res.append((x, i))
                r *= DIMINISH

        # remove the isolated nodes
        node_dic = {}
        tuple_to_delete = []
        for t in res:
            if t[0] not in node_dic:
                node_dic[t[0]] = [t[1]]
            else:
                if t[1] not in node_dic[t[0]]:
                    node_dic[t[0]].append(t[1])
                else:
                    tuple_to_delete.append(t)
        for t in tuple_to_delete:
            res.remove(t)

        t = random.choice(res)
        L = deque([t[0]])
        visited = {}
        visited[t[0]] = 1
        while (len(L) != 0):
            node_in_L = L.popleft()
            for i in node_dic[node_in_L]:
                if i not in visited:
                    visited[i] = 1
                    L.append(i)
        if len(list(visited.keys())) > 0.85 * num_of_node:
            #print(len(list(visited.keys())) / num_of_node)
            node_to_delete = []
            for t in res:
                if t[0] not in visited:
                    node_to_delete.append(t[0])
                    res.remove(t)
            for node in node_to_delete:
                del node_dic[node]
            newGraph = 0




    hospital = {}
    num = 0
    while(num < numOfHospital):
        ans = random.choice(list(node_dic.keys()))
        if ans not in hospital:
            hospital[ans] = 1
            num += 1

    with open('graph/' + (file_name.strip('.txt') + '.txt'), "w") as f:

        f.write("# Generated undirected unweighted graph" + "\n")
        f.write("# For CZ2001 Project" + "\n")
        f.write("# Nodes: " + str(num_of_node) + " " + "Edges: " + str(len(res)) + "\n")
        f.write("# FromNodeId     ToNodeId" + "\n")

        for i in res:
            f.write(str(i[0])+ " " + str(i[1]))
            f.write('\n')

    with open('graph/' + (file_name.strip('.txt') + '_hospital.txt'), "w") as f:
        hospital_arr = list(hospital.keys())
        f.write("# " + str(len(hospital_arr)) + "\n")

        for h in hospital_arr:
            f.write(str(h) + '\n')


if __name__ == "__main__":
    generate("random_graph.txt")