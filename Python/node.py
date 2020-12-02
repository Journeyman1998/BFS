from heapq import heappush

class Node:

    def __init__(self, id: int):
        self.id = id
        self.adjacent = []  # list of adjacent Nodes
        self.hospital = False  # default not hospital
        self.hospital_path = {}  # {hospital h node id: child in path to h}
        self.hospital_distance = [] # [(distance to h, hospital h node_id)] maintained as minheap

    def addEdge(self, nodeID: int):
        self.adjacent.append(nodeID)

    def isHospital(self):
        return self.hospital

    def setHospital(self, set_value: bool):
        self.hospital = set_value

    def getAdjacentNodes(self):
        return self.adjacent

    def setDistance(self, hospital_id, distance):
        #heappush(self.hospital_distance, (distance, hospital_id))
        self.hospital_distance.append((distance, hospital_id))

    def setPath(self, hospital_id, child):
        self.hospital_path[hospital_id] = child

    def getDistance(self):
        return self.hospital_distance

    def getHospitalPath(self):
        return self.hospital_path
    
    def getID(self):
        return self.id