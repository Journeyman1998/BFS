from node import Node

def initialiseGraph(filename):
    f = open(filename, 'r')
    l = f.readline()
    l = f.readline()
    l = f.readline()
    
    token = l.split(' ')
    N = int(token[2]) # number of nodes
    E = int(token[4]) # number of edges

    l = f.readline()

    node_dic = {}  # Node objects can be accessed by their IDs

    l = f.readline()
    while (len(l) != 0):
        token = l.split()
        if int(token[0]) in node_dic:
            node_dic[int(token[0])].addEdge(int(token[1]))
        else:
            node_dic[int(token[0])] = Node(int(token[0]))
            node_dic[int(token[0])].addEdge(int(token[1]))
        l = f.readline()

    return node_dic


def initialiseHospital(filename, node_dic):
    with open(filename, 'r') as f:
        hospital = []

        l = f.readline()
        num_hospitals = int(l[1:])
        l = f.readlines()
        for i in range(num_hospitals):
            if int(l[i]) in node_dic:
                node_dic[int(l[i])].setHospital(True)
                hospital.append(int(l[i]))

    return hospital

def output_results(node_dic, filename, choice):
    
    f = open(filename, "w")
    isolated_nodes = []
    for node in node_dic:
        line = ""
        disList = node_dic[node].getDistance()  # [(distance to h, hospital id)]
        if len(disList) == 0:
            isolated_nodes.append(node)
            continue
        childDic = node_dic[node].getHospitalPath()  # {hospital id: child in path to h}
        ranking = 1
        f.write("\n" + "For node " + str(node) + "\n")
        for Tuple in disList:
            line = str(node) + "-"
            h_id = Tuple[1]
            f.write("The No. " + str(ranking) + " nearest hospital's ID: " + str(h_id) + "\n")
            f.write("Distance: " + str(Tuple[0]) + "\n")
            if choice == 1:
                child_node = childDic[h_id]
                while child_node != h_id:
                    line = line + str(child_node) + "-"
                    child_node = node_dic[child_node].getHospitalPath()[h_id]
                
                line = line + str(child_node)
                f.write("Path: " + "\n")
                f.write(line + "\n")
            ranking += 1

    # if len(isolated_nodes) != 0:
    #     f.write("\n" + "The following nodes are not connected to any hospital: \n")
    #     f.write(", ".join([str(int) for int in isolated_nodes]))
    #     print("\n" + "There are", len(isolated_nodes), "nodes which are not connected to any hospital")

    f.close()

def outputPath(node_dic, node):
    if node not in node_dic:
        print("Node", node, "does not exist")
        return

    isolated_nodes = []
    disList = node_dic[node].getDistance()  # [(distance to h, hospital id)]
    if len(disList) == 0:
        print("Node ", node, "is not connected to any hospital\n")
        return
    childDic = node_dic[node].getHospitalPath()  # {hospital id: child in path to h}
    ranking = 1
    print("\n" + "For node " + str(node) + "\n")
    for Tuple in disList:
        path = [node]
        h_id = Tuple[1]
        print("The No. " + str(ranking) + " nearest hospital's ID: " + str(h_id) + "\n")
        print("Distance: " + str(Tuple[0]) + "\n")
        child_node = childDic[h_id]
        while child_node != h_id:
            path.append(child_node)
            child_node = node_dic[child_node].getHospitalPath()[h_id]
        path.append(child_node)
        print("Path: " + "\n")
        path_str = "->".join(str(int) for int in path)
        print(path_str + "\n")
        ranking += 1



def outputAllPath(node_dic):
    isolated_nodes = []
    for node in node_dic:
        disList = node_dic[node].getDistance()  # [(distance to h, hospital id)]
        if len(disList) == 0:
            isolated_nodes.append(node)
            continue
        childDic = node_dic[node].getHospitalPath()  # {hospital id: child in path to h}
        ranking = 1
        print("\n" + "For node " + str(node) + "\n")
        for Tuple in disList:
            path = [node]
            h_id = Tuple[1]
            print("The No. " + str(ranking) + " nearest hospital's ID: " + str(h_id) + "\n")
            print("Distance: " + str(Tuple[0]) + "\n")
            child_node = childDic[h_id]
            while child_node != h_id:
                path.append(child_node)
                child_node = node_dic[child_node].getHospitalPath()[h_id]
            path.append(child_node)
            print("Path: " + "\n")
            path_str = "->".join(str(int) for int in path)
            print(path_str + "\n")
            ranking += 1

    if len(isolated_nodes) != 0:
        print("\n" + "The following nodes are not connected to any hospital: \n")
        print(", ".join([str(int) for int in isolated_nodes]))
        print("\n" + "There are", len(isolated_nodes), "nodes which are not connected to any hospital")
