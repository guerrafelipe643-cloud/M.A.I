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
#ifndef MAI_NP_HPP
#define MAI_NP_HPP
#include <unordered_map>
class MAI_NP{
public:
    std::unordered_map<long long,long long> mem;
    bool novo = false;
    bool comp(long long ent);
    void compmemorize(long long ent);
};
#endif
