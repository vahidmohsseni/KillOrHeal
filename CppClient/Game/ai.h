#ifndef AI_H
#define AI_H

#include <ChillinClient>

#include "ks/models.h"
#include "ks/commands.h"


class AI : public koala::chillin::client::RealtimeAI<ks::models::World*>
{
private:
    int getRandInt(int start, int end);
    float getRandFloat(float start, float end);

public:
    AI(ks::models::World *world);

    void initialize();
    void decide();

protected:
    void move(int medicId, float distance);
    void turn(int medicId, bool clockwise, float angle);
    void fire(int medicId, bool clockwise, float angle);
};

#endif // AI_H
