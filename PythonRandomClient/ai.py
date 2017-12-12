# -*- coding: utf-8 -*-

# python imports
import random

# chillin imports
from chillin_client import RealtimeAI

# project imports
from ks.models import World
from ks.commands import Move, Turn, Fire
import random


class AI(RealtimeAI):

    def __init__(self, world):
        super(AI, self).__init__(world)


    def initialize(self):
        pass


    def decide(self):
        # print('decide')
        for medic in self.world.medics[self.my_side]:
            # here is stupid medic`s code!!!
            random_args = [
                (medic.id, random.uniform(0, medic.max_move_distance)),
                (medic.id, random.choice([True, False]), random.uniform(0, medic.max_turn_angle)),
                (medic.id, random.choice([True, False]), random.uniform(0, medic.max_turn_angle))
            ]
            commands = [self.move, self.turn, self.fire]
            random_command = random.randint(0, 2)
            commands[random_command](*random_args[random_command])


    def move(self, medic_id, distance):
        self.send_command(Move(medic_id, distance))


    def turn(self, medic_id, clockwise, angle):
        self.send_command(Turn(medic_id, clockwise, angle))


    def fire(self, medic_id, clockwise, angle):
        self.send_command(Fire(medic_id, clockwise, angle))
