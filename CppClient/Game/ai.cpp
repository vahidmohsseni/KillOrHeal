#include "ai.h"

#include <ctime>
#include <vector>
#include <iostream>

using namespace std;
using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): RealtimeAI<World*>(world)
{
    srand(time(0));
}

void AI::decide()
{
    for (int i = 0; i < this->world->ref_medics()[this->mySide].size(); i++)
    {
        int rand = getRandInt(0, 2);
        if (rand == 0)
        {
            Turn cmd;
            cmd.id(this->world->ref_medics()[this->mySide][i].id());
            cmd.clockwise((bool) getRandInt(0, 1));
            cmd.angle(((float) getRandInt(0, 360)) / 360.0f);
            this->sendCommand(&cmd);
        }
        else if (rand == 1)
        {
            Move cmd;
            cmd.id(this->world->ref_medics()[this->mySide][i].id());
            cmd.distance(0.6f);
            this->sendCommand(&cmd);
        }
        else
        {
            Fire cmd;
            cmd.id(this->world->ref_medics()[this->mySide][i].id());
            this->sendCommand(&cmd);
        }
    }
}

int AI::getRandInt(int start, int end)
{
    return (random() % (end - start + 1)) + start;
}
