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