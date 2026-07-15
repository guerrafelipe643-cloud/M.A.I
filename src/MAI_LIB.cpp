#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cctype>
#include <fstream>
#include "MAI_LIB/NN/MAI.hpp"
using namespace std;
void MAI::create(int qnd, int qnp, int numndnpe){
    for (int i = 0; i < qnd; i++){
        a += 1;
        nds.push_back(MAI_ND());
    }
    cout << "ND's criados! \n";
    for (int i = 0; i < qnp; i++){
        h += 1;
        nps.push_back(MAI_NP());
    }
    cout << "NP's criados! \n";
    numnd = a;
    numndnp = numndnpe;
}
void MAI::add_ND(int qnd){
    for (int i = 0; i < qnd; i++){
        a += 1;
        nds.push_back(MAI_ND());
    };
    cout << "ND's adicionados! \n";
    numnd = a;
}
void MAI::add_NP(int qnp, int numndnpe){
    for (int i = 0; i < qnp; i++){
        h += 1;
        nps.push_back(MAI_NP());
    };
    cout << "NP's adicionados! \n";
}
void MAI::process_and_memorize(string text){
    for (int i = 0; i < text.size(); i++) {
        char c = text[i];
        if (isdigit(c)) {
            ent = c;
        }
        else {
            ent = (int)c;
        }
        bool novo = nds[i].comp(ent);
        if (novo){
            vn = nds[i].calc(ent);
            nds[i].memorize(ent);
            saida[vn] = vn;
            grupo.push_back(vn);
        }
        if ((i + 1) % numndnp == 0){
            long long chave = 0;
            for(auto x : grupo){
                chave = chave * 1000 + x;
            }
            if(b < nps.size())
            {
                nps[b].comp(chave);
                b++;
            }
            else{
                bool saidanpt = nps[b].comp(chave);
                nps[b].compmemorize(chave);
                grupo.clear();
                b++;
            }
        }
    }
    b = 0;
}
void MAI::process(string text){
    for (int i = 0; i < text.size(); i++) {
        xz += 1;
        char c = text[i];
        if (isdigit(c)) {
            ent = c;
        }
        else {
            ent = (int)c;
        }
        bool novo = nds[i].comp(ent);
        if (novo){
            vn = nds[i].calc(ent);
            saida[vn] = vn;
            grupo.push_back(vn);
        }
        if ((i + 1) % numndnp == 0){
            xw += 1;
            long long chave = 0;
            for(auto x : grupo){
                chave = chave * 1000 + x;
            }
            if(b < nps.size())
            {
                nps[b].comp(chave);
                b++;
            }
        }
        xz = 0;
        xw = 0;
    }
    b = 0;
}
void MAI::map(){
    cout << a << "\n";
    cout << h << "\n";
    cout << "Quantidade de nd por np: " << numndnp << "\n";
}
void MAI::ajust_TA(int new_ta){
    for (int i = 0; i < nds.size(); i++){
        nds[i].ajust_TA(new_ta);
    }
    cout << "você ajustou a taxa de aprendizado com sucesso!";
}