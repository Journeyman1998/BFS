#include "loader.hpp"
#include "node.hpp"
#include "Writer.hpp"
#include <unordered_map>
#include <queue>
#include <chrono>
#include <cstdlib>
using namespace std;
using namespace std::chrono;

int initialiseGraph(vector<pair<int, int>>&, unordered_map<int, Node*>&);

void bfs_k(vector<int>&, vector<Node*>&, int, int);

int main(){
    Loader loader;
    //loader.open("data/test_graph.txt");
    loader.open("data/road.txt");
    vector<pair<int, int>> lines;
    vector<int> listOfHospitals;


    auto start = high_resolution_clock::now();
    loader.readGraph(lines);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    loader.close();

    cout << "Done loading graph" << endl;
    cout << "Time taken by function: " << duration.count() << " milliseconds" << endl;

    //construct the graph using a map
    unordered_map<int, Node*> graph;
    int maxId = initialiseGraph(lines, graph);


    //loader.open("data/test_hospital.txt");
    loader.open("data/test_hospital2.txt");
    loader.readHospital(listOfHospitals);

    vector<Node*> dic(maxId+1);

    for(auto it=graph.begin(); it != graph.end(); it++)
    {
        dic[(*it).first] = (*it).second;
    }

    start = high_resolution_clock::now();
    bfs_k(listOfHospitals, dic, 2, maxId);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    cout << "Done" << endl;
    cout << "Time taken by function: " << duration.count() << " milliseconds" << endl;

    Writer writer;
    writer.open("data/out.txt");

    start = high_resolution_clock::now();
    writer.output(graph, dic);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    cout << "Done" << endl;
    cout << "Time taken by function: " << duration.count() << " milliseconds" << endl;

    writer.close();

    return 0;
}


int initialiseGraph(vector<pair<int, int>>& lines, unordered_map<int, Node*>& graph){
    int id_1, id_2;
    int largest = 0;

    for(auto it = lines.begin(); it != lines.end(); it++){
        id_1 = it->first;
        id_2 = it->second;

        largest = max(max(id_1, id_2), largest);

        Node *n1, *n2;

        if(graph.find(id_1) == graph.end()){
            n1 = new Node(id_1);
            graph.insert(make_pair(id_1, n1));
        }
        else
            n1 = graph.find(id_1)->second;

        if(graph.find(id_2) == graph.end()){
            n2 = new Node(id_2);
            graph.insert(make_pair(id_2, n2));
        }
        else
            n2 = graph.find(id_2)->second;

        n1->addNeighbors(id_2);
        n2->addNeighbors(id_1);
    }
    return largest;
}


void bfs_k(vector<int>& hospitals, vector<Node*>& node_dic, int k, int largest)
{
    queue<pair<int, int>> q1;
    queue<pair<int, int>> q2;
    int h_id, n_id, neighbor_id;


    vector<int> visited(largest+1, 0);

    //mark the initial hospital node and initialise the bfs queues
    for(auto it=hospitals.begin(); it!=hospitals.end(); it++)
    {
        h_id = *it;
        visited[h_id] = 1;
        node_dic[h_id]->vectorDistance(h_id, 0);
        node_dic[h_id]->vectorPath(h_id, h_id);
        q1.push(make_pair(h_id, h_id));
    }

    int distance = 1;

    while(!q1.empty())
    {
        pair<int,int>& temp = q1.front();
        n_id = temp.first;
        h_id = temp.second;

        q1.pop();

        vector<int>& neigh = node_dic[n_id]->getNeighbors();

        for(auto it=neigh.begin(); it!=neigh.end(); it++)
        {
            neighbor_id = *it;
            unordered_map<int, int>& path = node_dic[neighbor_id]->getPaths();
            if(visited[neighbor_id] != k && path.find(h_id) == path.end())
            {
                visited[neighbor_id]++;
                node_dic[neighbor_id]->vectorDistance(h_id, distance);
                node_dic[neighbor_id]->vectorPath(h_id, n_id);
                q2.push(make_pair(neighbor_id, h_id));
            }
        }

        if(q1.empty())
        {
            distance++;
            q1.swap(q2);
        }
    }




}
