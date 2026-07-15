#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <fstream>
#include "MAI_LIB/NN/MAI_ND.hpp"
using namespace std;
bool MAI_ND::comp(int ent){
    if (mem.count(ent)){
        novo = false;
        return novo;      
    } 
    novo = true;
    cout << "ND: Desconhecido na entrada: " << ent << "\n";
    return novo;
    }
int MAI_ND::calc(int ent){
    double err = ent - vn;
    if (novo == true){
        while (abs(err) >= 1e-1){
            err = ent - vn;
            vna = err * ta;
            vn += vna;
        }
        vn = round(vn);
    }
    return vn;
}
void MAI_ND::memorize(int ent){
    if (vn == ent){
        mem[vn] = vn;
    }
}
void MAI_ND::ajust_TA(int new_ta){
    ta = new_ta;
    cout << "você ajustou a taxa de aprendizado com sucesso!";
}