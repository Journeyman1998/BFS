#ifndef NODE
#define NODE
#include <vector>
#include <unordered_map>
#include <vector>
using namespace std;

class Node{
private:
    bool hospital;
    int id;
    vector<int> neighbors;
    unordered_map<int, int> path; //(hospital h node id: child in path to h)
    vector<pair<int,int>> distance; //(distance to h, hospital h node_id)
public:
    Node(){};
    Node(int);
    ~Node();
    int getId() const;
    void vectorHospital(bool);
    bool isHospital() const;
    void addNeighbors(int);
    vector<int>& getNeighbors();
    void vectorDistance(int, int);
    void vectorPath(int, int);
    vector<pair<int, int>>& getDistances();
    unordered_map<int, int>& getPaths();
    void printInfo();
};

#endif
