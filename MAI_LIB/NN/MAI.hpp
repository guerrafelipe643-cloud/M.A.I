// ===============================================================================
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
