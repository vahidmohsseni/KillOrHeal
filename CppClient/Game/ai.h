#ifndef AI_H
#define AI_H

#include <ChillinClient>

#include "ks/models.h"
#include "ks/commands.h"


class AI : public koala::chillin::client::RealtimeAI<ks::models::World*>
{
private:
    int getRandInt(int start, int end);

public:
    AI(ks::models::World *world);

    void decide();
};

#endif // AI_H
