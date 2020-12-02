#include "Writer.hpp"

void Writer::open(string filename)
{
    fout.open(filename);
}
void Writer::output(unordered_map<int, Node*>& graph, vector<Node*>& node_dic)
{
    int id;
    for(auto it=graph.begin(); it != graph.end(); it++){
        string line = "";
        id = (*it).first;

        outputPath(line, node_dic, id);

        if(line.length() != 0)
            fout << line << endl;
    }
}

void Writer::outputPath(string& ret, vector<Node*>& graph, int n_id)
{
    vector<pair<int, int>>& distances = graph[n_id]->getDistances();
    if(distances.empty()){
        ret += to_string(n_id) + " is not connected to any hospital.\n";
        return;
    }

    unordered_map<int, int>& childDic = graph[n_id]->getPaths();
    int ranking = 1;
    int h_id, dist, child;

    ret += "For node " + to_string(n_id) + ": \n";

    for(auto it = distances.begin(); it != distances.end(); it++)
    {
        h_id = (*it).second;
        dist = (*it).first;

        ret += "The No. " + to_string(ranking) + " nearest hospital's ID: " + to_string(h_id) + "\n";
        ret += "Distance: " + to_string(dist) + "\n";
        ret += "Path: ";
        child = childDic[h_id];
        ret += to_string(n_id) + "-";

        while(child != h_id)
        {
            ret += to_string(child) + "-";
            child = graph[child]->getPaths()[h_id];
        }

        ret += to_string(child);
        ret += "\n";
        ranking++;
    }
}


void Writer::close()
{
    fout.close();
}
