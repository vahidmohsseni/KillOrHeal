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

    def decide(self):
        # print('decide')
        for medic in self.world.medics[self.my_side]:
            # here is stupid medic`s code!!!
            a = [
                Turn(medic.id, random.choice([True, False]), random.uniform(0, 30)),
                Move(medic.id, 0.6),
                Fire(medic.id)
            ]
            self.send_command(random.choice(a[0:3]))
