from node import Node
from collections import deque
from time_measure import time
import graphio

def BFS_from_Hospitals(hospital_list, node_dic, k):
    arr = [(x, x) for x in hospital_list]  # (node_id, hospital_id where the bfs starts)
    queue = deque(arr)  # queue of nodes to be searched
    next_level = deque([])  # queue of all the adjacent nodes to be searched
    visited = {key: 0 for key in list(node_dic.keys())} # {node_id: num of visited hospitals}

    # mark the initial hospital node
    for h_id in hospital_list:
        visited[h_id] = 1
        node_dic[h_id].setDistance(h_id, 0)
        node_dic[h_id].setPath(h_id, h_id)

    distance = 1
    while (len(queue) != 0):
        node, hospital_id = queue.popleft()
        for i in node_dic[node].getAdjacentNodes():

            if visited[i] != k and hospital_id not in node_dic[i].getHospitalPath():
                visited[i] += 1
                node_dic[i].setDistance(hospital_id, distance)
                node_dic[i].setPath(hospital_id, node)
                next_level.append((i, hospital_id))

        if (len(queue) == 0):
            distance += 1
            queue.extend(next_level)
            next_level.clear()

# for testing runtime
if __name__ == "__main__":
    node_dic = graphio.initialiseGraph("random_graph.txt")
    hospital = graphio.initialiseHospital("random_graph_hospital.txt", node_dic)
    res, timeTaken = time(BFS_from_Hospitals, hospital, node_dic, 2)
    print(timeTaken)