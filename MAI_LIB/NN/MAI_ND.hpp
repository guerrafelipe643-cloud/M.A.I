#ifndef MAI_ND_HPP
#define MAI_ND_HPP
#include <unordered_map>
class MAI_ND{
public:
    std::unordered_map<int,int> mem;
    
    double ta = 0.1;
    double vn = 0;
    double ent = 0;
    double err = ent - vn;
    double vna = err * ta;
    bool novo = false;
    bool comp(int ent);
    int calc(int ent);
    void memorize(int ent);
    void ajust_TA(int new_ta);
};
#endif