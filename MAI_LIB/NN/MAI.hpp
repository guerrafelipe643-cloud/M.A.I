#ifndef MAI_HPP
#define MAI_HPP
#include <vector>
#include <iostream>
#include "MAI_ND.hpp"
#include "MAI_NP.hpp"
using namespace std;
class MAI{
private:
    vector<MAI_ND> nds;
    vector<MAI_NP> nps;
    vector<int> grupo;
    unordered_map<int,int> saida;   // acumulador
    string line;
    string ab;
    string text;
    int b = 0;
    int a = 0;
    int h = 0;
    int ent = 0;
    int vn = 0;
    int numndnp = 0;
    int numnd = 0;
    int xz = 0;
    int xw = 0;
public:
    void create(int qnd, int qnp, int numndnp);
    void add_ND(int qnd);
    void add_NP(int qnp, int numndnpe);
    void process_and_memorize(string text);
    void process(string text);
    void ajust_TA(int new_ta);
    void map();
};
#endif