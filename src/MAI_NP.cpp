#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cctype>
#include <random>
#include <fstream>
#include <thread>
#include <chrono>
#include "MAI_LIB/NN/MAI_NP.hpp"
using namespace std;
bool MAI_NP::comp(long long ent){
    if (mem.count(ent)){
        novo = false;
        return novo;
    }
    novo = true;
    cout << "NP: Desconhecido na entrada: " << ent <<"\n";
    return novo;
}
void MAI_NP::compmemorize(long long ent){
    mem[ent] = ent;
}