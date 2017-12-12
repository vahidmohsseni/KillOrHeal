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

void AI::initialize()
{
}

void AI::decide()
{
    for (int i = 0; i < this->world->ref_medics()[this->mySide].size(); i++)
    {
        Medic medic = this->world->ref_medics()[this->mySide][i];
        int rand = getRandInt(0, 2);

        if (rand == 0)
        {
            this->move(
                medic.id(),
                getRandFloat(0, medic.max_move_distance())
            );
        }
        else if (rand == 1)
        {
            this->turn(
                medic.id(),
                (bool) getRandInt(0, 1),
                getRandFloat(0, medic.max_turn_angle())
            );
        }
        else
        {
            this->fire(
                medic.id(),
                (bool) getRandInt(0, 1),
                getRandFloat(0, medic.max_fire_angle())
            );
        }
    }
}

int AI::getRandInt(int start, int end)
{
    return (rand() % (end - start + 1)) + start;
}

float AI::getRandFloat(float start, float end)
{
    float n = ((float) rand()) / ((float) RAND_MAX);
    return n * (end - start) + start;
}


void AI::move(int medicId, float distance)
{
    Move cmd;
    cmd.id(medicId);
    cmd.distance(distance);
    this->sendCommand(&cmd);
}

void AI::turn(int medicId, bool clockwise, float angle)
{
    Turn cmd;
    cmd.id(medicId);
    cmd.clockwise(clockwise);
    cmd.angle(angle);
    this->sendCommand(&cmd);
}

void AI::fire(int medicId, bool clockwise, float angle)
{
    Fire cmd;
    cmd.id(medicId);
    cmd.clockwise(clockwise);
    cmd.angle(angle);
    this->sendCommand(&cmd);
}
