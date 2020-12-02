#ifndef LOADER
#define LOADER

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

class Loader{
    public:
        Loader(){}
        ~Loader(){}
        void open(string);
        bool checkValid();
        void readGraph(vector<pair<int, int>>&);
        void readHospital(vector<int>&);
        void close();

    private:
        ifstream fin;
};

#endif
