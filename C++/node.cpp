#include "node.hpp"
#include <iostream>
using namespace std;

Node::Node(int id) : id(id){}

Node::~Node(){}

int Node::getId() const{return id;}

void Node::vectorHospital(bool h){hospital = h;}

bool Node::isHospital() const {return hospital;}

void Node::addNeighbors(int n)
{
    neighbors.push_back(n);
}

vector<int>& Node::getNeighbors()
{
    return neighbors;
}

void Node::vectorDistance(int id, int dist)
{
    distance.push_back(make_pair(dist, id));
}

void Node::vectorPath(int id, int child)
{
    path.insert(make_pair(id, child));
}

vector<pair<int, int>>& Node::getDistances()
{
    return distance;
}

unordered_map<int, int>& Node::getPaths()
{
    return path;
}

void Node::printInfo()
{
    cout << id << endl;
    cout << "Distances: " << endl;
    for(auto it=distance.begin(); it != distance.end(); it++){
        pair<int, int> x = *it;
        cout << to_string(x.first) << "," <<  to_string(x.second) << " ";
    }
    cout << endl;
    cout << "Paths: " << endl;
    for(auto it=path.begin(); it != path.end(); it++){
        pair<int, int> x = *it;
        cout << to_string(x.first) << "," <<  to_string(x.second) << " ";
    }
    cout << endl;
}
