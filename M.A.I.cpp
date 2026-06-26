// =============================================================================
//   MAI - Memory Architecture for AI (Arquitetura de memória para IA)
//   Copyright (C) 2026  Felipe Guerra Rodrigues Athaydes
//
//   Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo
//   sob os termos da Licença Pública Geral GNU conforme publicada pela
//   Free Software Foundation, tanto a versão 3 da Licença, ou (a seu critério)
//   qualquer versão posterior.
//
//   Este programa é distribuído na expectativa de que seja útil, mas
//   SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de
//   COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja a
//   Licença Pública Geral GNU para mais detalhes.
//
//  Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com
//   este programa. Se não, veja <https://gnu.org>.
// ==============================================================================
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cctype>
#include <random>
using namespace std;
class ND{
public:
    unordered_map<int,int> mem;
    double ta = 0.1;
    double vn = 0;
    double vna = 0;
    int saida = 0;
    int fim = 0;
    bool novo = false;
    bool comp(int ent){
        if (mem.count(ent)){
            saida = ent;
            novo = false;
            return novo;
            
        }
        else{
            novo = true;
            cout << "Desconhecido";
            return novo;
        }
    }
    int calc(int ent){
        double err = ent - vn;
        if (novo == true){
            while (abs(err) >= 1e-1){
                err = ent - vn;
                vna = err * ta;
                vn += vna;
            }
            vn = round(vn);
            if (vn == ent){
                mem[vn] = vn;
            }
        }
        return vn;
    }
};
class NP{
public:
    int ent = 0;
    bool novo = false;
    unordered_map<int,int> mem;
    bool comparar(int ent){
        if (mem.count(ent)){
            novo = false;
            cout << "Conhecido \n";
            return novo;
        }
        else{
            mem[ent] = ent;
            novo = true;
            cout << "Desconhecido \n";
            return novo;
        }
    }
};
int b = 0;
int ciclo = 0;
int qnd = 0;
int numnp = 0;
int numnd = 0;
int a = 0;
int ent = 0;
int vn = 0;
int inicio = 0;
int fim = 0;
string dado = "";
unordered_map<int,int> saida;
unordered_map<bool,int> saidanp;
string txt = "";
vector<int> grupo;
vector<ND> nds;
vector<NP> nps;
int main(){
        cout << "Digite a quantidade de nds: ";
        cin >> qnd;
        cout << "Digite quantos ND cada NP deve agrupar: ";
        cin >> numnd;
        for (int i = 0; i < qnd; i++){
            a += 1;
            nds.push_back(ND());
        }
        numnp = a / numnd;
        for (int i = 0; i < numnp; i++){
            nps.push_back(NP());
        }
        while (1){
            cout << "Digite uma entrada: ";
            cin >> txt;
            if (txt.size() > nds.size()){
                cout << "Digite novamente \n";
                continue;
            }
            for (int i = 0; i < txt.size(); i++) {
                char c = txt[i];
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
                if ((i + 1) % numnd == 0){
                    int chave = 0;
                    for(auto x : grupo){
                        chave = chave * 1000 + x;
                    }
                    bool saidanpt =
                        nps[b].comparar(chave);
                    grupo.clear();
                    b++;
                }
            }
            b = 0;
        }
    return 0;
}
