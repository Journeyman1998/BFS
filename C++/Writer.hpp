#ifndef WRITER_H
#define WRITER_H
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include "node.hpp"
using namespace std;

class Writer
{
    public:
        Writer(){}
        ~Writer(){}
        void open(string);
        void output(unordered_map<int, Node*>&, vector<Node*>&);
        void close();
        void outputPath(string&, vector<Node*>&, int);

    private:
        ofstream fout;
};

#endif // WRITER_H
