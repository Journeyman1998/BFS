#include "loader.hpp"
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>

using namespace std;

void Loader::open(string filename){
    fin.open(filename);
}

bool Loader::checkValid(){
    return fin.good();
}

void Loader::readGraph(vector<pair<int, int>>& arr){
    if(!checkValid()){
        cerr << "Error in input stream" << endl;
        exit(1);
    }

    string line;

    //read the first 4 redundant lines
    getline(fin, line);
    getline(fin, line);
    getline(fin, line);
    getline(fin, line);

    while(getline(fin, line)){
        istringstream iss(line);
        vector<string> results((istream_iterator<string>(iss)), istream_iterator<string>());

        int id_1, id_2;
        id_1 = stoi(results[0]);
        id_2 = stoi(results[1]);

        arr.push_back(make_pair(id_1, id_2));
    }
}

void Loader::readHospital(vector<int>& listOfHospitals)
{
    if(!checkValid()){
        cerr << "Error in input stream" << endl;
        exit(1);
    }

    string line;
    getline(fin, line);
    int h;
    while(!fin.eof()){
        fin >> h;
        listOfHospitals.push_back(h);
    }
}

void Loader::close()
{
    fin.close();
}
