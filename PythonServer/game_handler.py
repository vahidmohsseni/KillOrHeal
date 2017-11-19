# -*- coding: utf-8 -*-

# python imports
import random
# chillin imports
from chillin_server import RealtimeGameHandler
from chillin_server.gui.canvas_elements import ScaleType
# project imports
from ks.models import World, Medic, Patient, Position, Wall, PowerUp, PowerUpType
from ks.commands import Move, Turn, Fire
# json for map
import json
# math for draw walls
import math


class GameHandler(RealtimeGameHandler):
    def on_recv_command(self, side_name, agent_name, command_type, command):
        # print('command: %s %s %s' % (side_name, command_type, command))
        if command.name() == Fire().name():
            self.commands[(side_name, command.id)] = ((side_name, command), 1)
        else:
            self.commands[(side_name, command.id)] = ((side_name, command), 2)

    def on_initialize(self):
        print('initialize')
        self.commands = {}
        self.world = World()
        # fix sides into right list
        self.sides = self.sides.keys()

        world_map_file = open(self.config["map"], "r")
        self.world_map = world_map = json.loads(world_map_file.read())
        world_map_file.close()
        # set world height and width
        self.world.height, self.world.width = (world_map["height"], world_map["width"])
        # add medics and patients to world
        self.world.medics = {self.sides[0]: [], self.sides[1]: []}
        self.world.patients = []
        for i in range(world_map["medics"]["number"]):
            p1 = Position(self.get_random_float(world_map["medics"]["radius"],
                                                self.world.width - 2 * world_map["medics"]["radius"]),
                          float(random.randint(0, self.world.height)))
            # p1 = [Position(8.4, 16.7), Position(14.3, 9.9)][i]
            angle1 = self.get_random_float(0, 360)
            # angle1 = 45.0
            p2 = Position(self.get_random_float(world_map["medics"]["radius"],
                                                self.world.width - 2 * world_map["medics"]["radius"]),
                          float(random.randint(0, self.world.height)))
            angle2 = self.get_random_float(0, 360)
            # p2 = [Position(9.0, 18.7), Position(14.3, 9.9)][i]
            # angle2 = 90.0
            medic = self.create_medics(i, self.sides[0], p1, angle1, world_map)
            # medic.max_move_distance = self.calc_medic_max_move(medic)
            self.world.medics[self.sides[0]].append(medic)

            medic = self.create_medics(i + world_map["medics"]["number"], self.sides[1], p2, angle2, world_map)
            # medic.max_move_distance = self.calc_medic_max_move(medic)
            self.world.medics[self.sides[1]].append(medic)

        for i in range(world_map["patients"]["number"]):
            p = Position(self.get_random_float(world_map["patients"]["radius"],
                                               self.world.width - 2 * world_map["patients"]["radius"]),
                         float(random.randint(0, self.world.height)))
            self.world.patients.append(self.create_patients(p, world_map))
        self.world.patients.append(self.create_patients(Position(2.0, 18.0), world_map, True))

        # end add medics and patients

        # set world scores
        self.world.scores = {}
        for side in self.sides:
            self.world.scores[side] = 0
        # end set world scores

        # set walls into world
        self.walls_line_equation = []  # ax + by + c = 0
        self.world.walls = []
        for wall in world_map["walls"]:
            start_pos = Position(wall[0]["x"], wall[0]["y"])
            end_pos = Position(wall[1]["x"], wall[1]["y"])
            self.world.walls.append(Wall(start_pos, end_pos))
            line_equation = (end_pos.y - start_pos.y, start_pos.x - end_pos.x,
                             ((start_pos.y - end_pos.y) * start_pos.x) + ((end_pos.x - start_pos.x) * start_pos.y))
            self.walls_line_equation.append(line_equation)

            # end set walls into world

        # set powerups positions
        self.power_ups = []
        self.world.powerups = []
        for powerup in self.world_map["powerups"]["positions"]:
            self.power_ups.append([Position(powerup["x"], powerup["y"]), 0])
        # end set powerups

        # list for medics should be deleted after laser
        self.down_medics = []

    def on_initialize_gui(self):
        print('initialize gui')
        self.gui_config = gui_config = self.config["gui"]
        # set coefficient of gui height and width
        # from chillin_server.gui.canvas import Canvas
        # self.canvas = Canvas()
        width_coefficient = self.canvas.width / self.world.width
        height_coefficient = self.canvas.height / self.world.height

        self.medics_ref = {}
        for side in self.world.medics:
            for medic in self.world.medics[side]:
                index = self.sides.index(side)
                x = int(medic.position.x * width_coefficient)
                y = int(medic.position.y * height_coefficient)
                # print medic.position.x, medic.position.y
                rx = int(2 * medic.radius * width_coefficient)
                ry = int(medic.radius * height_coefficient)
                # print "medics", x, y, rx, ry
                self.medics_ref[(side, medic.id)] = ref = self.canvas.create_image(self.sides[index], x, y,
                                                                                   scale_type=ScaleType.ScaleToWidth,
                                                                                   scale_value=rx,
                                                                                   angle=medic.angle,
                                                                                   center_origin=True)
        self.patients_ref = []
        self.modifying_patients_and_medics = []  # tuple(patient_index, new Medic if exists)

        for patient in self.world.patients:
            x = int(patient.position.x * width_coefficient)
            y = int(patient.position.y * height_coefficient)
            rx = int(patient.radius * width_coefficient)
            ry = int(patient.radius * height_coefficient)
            # print "patient", x, y, rx, ry
            self.patients_ref.append(self.canvas.create_image("Patient", x, y, scale_type=ScaleType.ScaleToWidth,
                                                              scale_value=rx,
                                                              center_origin=True))

        for wall in self.world.walls:
            x1 = int(wall.start_pos.x * width_coefficient)
            y1 = int(wall.start_pos.y * height_coefficient)
            x2 = int(wall.end_pos.x * width_coefficient)
            y2 = int(wall.end_pos.y * height_coefficient)
            wall_color = self.canvas.make_rgba(96, 9, 184, 255)
            self.canvas.create_line(x1, y1, x2, y2, wall_color)

        self.power_ups_ref = {}  # key = (x, y)
        self.modifying_power_ups = []  # [bool create or delete, id]

        self.delete_fire_ref = []
        self.create_fire_ref = []

        self.down_medics_ref = []
        self.canvas.apply_actions()

    def on_process_cycle(self):
        print('process: %s' % self.current_cycle)
        fire_cmds = [c[0] for c in self.commands.values() if c[1] == 1]
        other_cmds = [c[0] for c in self.commands.values() if c[1] == 2]
        for side, command in fire_cmds:
            for medic in self.world.medics[side]:
                if medic.id == command.id:
                    self._handle_command(side, medic, command)
        # should damaged medics be removed
        for medic in self.down_medics:
            if medic in self.world.medics[medic.side_name]:
                self.world.medics[medic.side_name].remove(medic)
        self.down_medics = []
        for side, command in other_cmds:
            for medic in self.world.medics[side]:
                if medic.id == command.id:
                    self._handle_command(side, medic, command)
                self._healing(side, medic)
                self._crush_powerup_and_medic(medic)

        self._create_power_ups_randomly()
        self._remove_powerups_end_time()
        # empty commands dict
        self.commands = {}

    def on_update_clients(self):
        print('update clients')
        self.send_snapshot(self.world)

    def on_update_gui(self):
        print('update gui')
        width_coefficient = self.canvas.width / self.world.width
        height_coefficient = self.canvas.height / self.world.height
        # update medics positions
        for side in self.world.medics:
            for medic in self.world.medics[side]:
                x = medic.position.x * width_coefficient
                y = medic.position.y * height_coefficient
                tmp = self.medics_ref.get((side, medic.id), None)
                if tmp >= 0:
                    self.canvas.edit_image(self.medics_ref[side, medic.id], x, y, angle=medic.angle)
                else:
                    continue
        # end update medics positions

        # update patients if remove and create new medics if needed
        for item in self.modifying_patients_and_medics:
            self.canvas.delete_element(self.patients_ref[item[0]])
            if item[1] != -1:
                medic = item[1]
                x = medic.position.x * width_coefficient
                y = medic.position.y * height_coefficient
                rx = int(2 * medic.radius * width_coefficient)
                self.medics_ref[(medic.side_name, medic.id)] = self.canvas.create_image(medic.side_name, x, y,
                                                                                        scale_type=ScaleType.ScaleToWidth,
                                                                                        scale_value=rx,
                                                                                        angle=medic.angle,
                                                                                        center_origin=True)
        self.modifying_patients_and_medics = []  # should be empty after everything done
        # end update patients if remove and create new medics if needed

        # update powerups
        for powerup in self.modifying_power_ups:
            pup = powerup[1]
            if powerup[0] == 0:  # delete
                ref = self.power_ups_ref.pop((pup.position.x, pup.position.y))
                self.canvas.delete_element(ref)
            else:  # create
                if PowerUpType.LASER == pup.type:
                    img = "Laser"
                else:
                    img = "Healpack"
                x = pup.position.x * width_coefficient
                y = pup.position.y * height_coefficient
                rx = int(2 * 0.5 * width_coefficient)
                ref = self.canvas.create_image(img, x, y, scale_type=ScaleType.ScaleToWidth, scale_value=rx,
                                               center_origin=True)
                self.power_ups_ref[(pup.position.x, pup.position.y)] = ref

        self.modifying_power_ups = []
        # end update powerups

        # draw fire and remove
        for i in self.delete_fire_ref:
            self.canvas.delete_element(i)
        self.delete_fire_ref = []

        for i in self.create_fire_ref:
            x1 = int(i[0] * width_coefficient)
            y1 = int(i[1] * height_coefficient)
            x2 = int(i[2] * width_coefficient)
            y2 = int(i[3] * height_coefficient)
            wall_color = self.canvas.make_rgba(203, 96, 1, 255)
            ref = self.canvas.create_line(x1, y1, x2, y2, wall_color)
            self.delete_fire_ref.append(ref)
        self.create_fire_ref = []
        # end draw fire and remove

        # delete medics whose health is 0
        for medic in self.down_medics_ref:
            for ref in self.medics_ref[medic.side_name]:
                self.canvas.delete_element(ref)
        self.down_medics_ref = []
        # end delete medics whose health is 0
        self.canvas.apply_actions()

    @staticmethod
    def get_random_float(start, end):
        return random.uniform(start, end)

    @staticmethod
    def create_medics(mid, side_name, position, angle, world_map):
        return Medic(mid,
                     side_name,
                     position,
                     world_map["medics"]["radius"],
                     world_map["medics"]['max_move_distance'],
                     angle,
                     world_map["medics"]['max_turn_angle'],
                     world_map["medics"]["max_fire_angle"],
                     world_map["medics"]['health'],
                     world_map["medics"]['max_health'],
                     world_map["medics"]["laser_damage"],
                     world_map["medics"]["laser_count"],
                     world_map["medics"]["laser_range"],
                     world_map["medics"]["laser_max_count"],
                     world_map["medics"]["healing_remaining_time"],
                     world_map["medics"]["death_score"])

    @staticmethod
    def create_patients(position, world_map, capturable=None):
        if capturable:
            return Patient(position,
                           world_map["patients"]["radius"],
                           world_map["patients"]["healing_duration"],
                           capturable,
                           world_map["patients"]["heal_score"])
        return Patient(position,
                       world_map["patients"]["radius"],
                       world_map["patients"]["healing_duration"],
                       world_map["patients"]["capturable"],
                       world_map["patients"]["heal_score"])

    def _handle_command(self, side, medic, cmd):
        handlers = {
            Move.name(): self._handle_move,
            Turn.name(): self._handle_turn,
            Fire.name(): self._handle_fire
        }
        handlers[cmd.name()](side, medic, cmd)

    def _healing(self, side, medic):

        for i in range(len(self.world.patients)):
            patient = self.world.patients[i]
            patient_medic_dist = self.get_2_points_distance(medic.position.x, medic.position.y,
                                                            patient.position.x, patient.position.y)

            if patient_medic_dist <= patient.radius + medic.radius:
                if medic.healing_remaining_time == 0:
                    medic.healing_remaining_time = patient.healing_duration
                    break  # not to check other patients
                else:
                    medic.healing_remaining_time -= 1
                    if medic.healing_remaining_time == 0:
                        if patient.capturable:
                            if self.world.medics:
                                mid = sorted(self.world.medics[side], key=lambda x: x.id)[-1].id
                                mid += 1
                            else:
                                mid = 1
                            medic_temp = self.create_medics(mid, side, patient.position, medic.angle
                                                            , self.world_map)
                            self.world.medics[side].append(medic_temp)
                            self.world.scores[side] += patient.heal_score
                            self.world.patients.remove(patient)
                            self.modifying_patients_and_medics.append((i, medic_temp))

                        else:
                            self.world.scores[side] += patient.heal_score
                            self.world.patients.remove(patient)
                            self.modifying_patients_and_medics.append((i, -1))

                        break  # not to check other patients
            else:
                continue

    def _handle_move(self, side, medic, cmd):
        dist = cmd.distance
        if dist < 1.0:
            medic.healing_remaining_time = 0
            x = medic.position.x + dist * math.cos(math.radians(medic.angle))
            y = medic.position.y - dist * math.sin(math.radians(medic.angle))
            res = self.check_medic_crush_the_wall(medic, x, y)
            if res:
                pass
            else:
                medic.position.x = x
                medic.position.y = y


    def calc_medic_max_move(self, medic):
        pass

    def check_medic_crush_the_wall(self, medic, x, y):
        result = []
        for i in range(len(self.world.walls)):
            a = self.walls_line_equation[i][0]
            b = self.walls_line_equation[i][1]
            c = self.walls_line_equation[i][2]
            if (a * x) + (b * y) + c == 0:
                a1 = -b
                b1 = a
                c1 = (-1.0 * a * self.world.walls[i].start_pos.y) + (b * self.world.walls[i].start_pos.x)
                a2 = -b
                b2 = a
                c2 = (-1.0 * a * self.world.walls[i].end_pos.y) + (b * self.world.walls[i].end_pos.x)
                r1 = abs(((a1 * x) + (b1 * y) + c1) / (a1 ** 2 + b1 ** 2) ** 0.5)
                r2 = abs(((a2 * x) + (b2 * y) + c2) / (a2 ** 2 + b2 ** 2) ** 0.5)
                if r1 < medic.radius:
                    result.append((i, r1 - medic.radius))
                    break
                elif r2 < medic.radius:
                    result.append((i, r2 - medic.radius))
                    break
                else:
                    continue
            elif abs(((a * x) + (b * y) + c) / (a ** 2 + b ** 2) ** 0.5) < medic.radius \
                    and (self.world.walls[i].start_pos.x < x < self.world.walls[i].end_pos.x
                         or self.world.walls[i].start_pos.y < y < self.world.walls[i].end_pos.y):
                result.append(i)
                break
            else:
                continue

        return result if result else False

    def _handle_turn(self, side, medic, cmd):
        clockwise = cmd.clockwise
        angle = cmd.angle
        if abs(angle) <= self.world_map["medics"]["max_turn_angle"]:
            medic.healing_remaining_time = 0
            if clockwise:
                medic.angle -= angle
                medic.angle %= 360
            else:
                medic.angle += angle
                medic.angle %= 360

    def _handle_fire(self, side, medic, cmd):
        angle = cmd.angle
        if abs(angle) <= self.world_map["medics"]["max_fire_angle"]:
            angle += medic.angle
            if medic.laser_count != 0:
                medic.healing_remaining_time = 0
                medic.laser_count -= 1
                x2, y2, line_eq = self.check_fire_crush_the_wall(medic.position.x, medic.position.y, angle)
                x1, y1 = medic.position.x, medic.position.y

                x2, y2, o_medic = self.check_fire_crush_the_medics(x1, y1, x2, y2, line_eq, medic)

                if o_medic:
                    o_medic.health -= medic.laser_damage
                    if o_medic.health <= 0:
                        self.down_medics.append(o_medic)
                        self.down_medics_ref.append(o_medic)
                        self.world.scores[side] += o_medic.death_score

                self.create_fire_ref.append([x2, y2, x1, y1])

    def _create_power_ups_randomly(self):
        chance = random.randint(0, 100)
        if chance > 70 and len(self.power_ups) >= 2:
            chance = random.randint(0, len(self.power_ups) - 1)
            if self.power_ups[chance][1] == 0:
                self.power_ups[chance][1] = 1

                power_up_type = random.choice([(PowerUpType.LASER, 0),
                                               (PowerUpType.HEAL_PACK, self.world_map["healpack"]["max_healing"])])
                pup = PowerUp(power_up_type[0], self.power_ups[chance][0],
                              self.world_map["powerups"]["appearance_time"], power_up_type[1])
                self.world.powerups.append(pup)
                self.modifying_power_ups.append([1, pup])
                self.power_ups.remove(self.power_ups[chance])

    def _remove_powerups_end_time(self):
        result = []
        for i in range(len(self.world.powerups)):
            pup = self.world.powerups[i]
            if pup.appearance_time == 0:
                result.append(i)
                self.modifying_power_ups.append([0, pup])
                if pup.type == PowerUpType.LASER:
                    t = 0
                else:
                    t = 1

                self.power_ups.append([pup.position, t, 0])
            else:
                pup.appearance_time -= 1
        for i in result:
            self.world.powerups.pop(i)

    def _crush_powerup_and_medic(self, medic):
        result = []
        for i in range(len(self.world.powerups)):
            pup = self.world.powerups[i]
            dist = self.get_2_points_distance(medic.position.x, medic.position.y, pup.position.x, pup.position.y)

            if dist <= 0.5 + medic.radius:
                if pup.type == PowerUpType.LASER:
                    if medic.laser_count == medic.laser_max_count:
                        continue
                    else:
                        medic.laser_count += 1
                        result.append(i)
                        self.modifying_power_ups.append([0, pup])
                        self.power_ups.append([pup.position, 0, 0])
                else:
                    if medic.health == medic.max_health:
                        continue
                    else:
                        medic.health += pup.value
                        medic.health = medic.max_health if medic.health > medic.max_health else medic.health
                        result.append(i)
                        self.modifying_power_ups.append([0, pup])
                        self.power_ups.append([pup.position, 1, 0])
            else:
                continue
        for i in result:
            self.world.powerups.pop(i)

    def check_fire_crush_the_wall(self, x, y, angle):
        # consider 3 lines equation
        result = []
        x_max = x + self.world_map["medics"]["laser_range"] * math.cos(math.radians(angle))
        y_max = y - self.world_map["medics"]["laser_range"] * math.sin(math.radians(angle))
        fire_line_eq = ((y - y_max), (x_max - x), ((y * (x - x_max)) + (x * (y_max - y))))
        for i in range(len(self.world.walls)):
            wall = self.world.walls[i]
            angle1 = self.get_line_degree_with_2_points(x, y, wall.start_pos.x, wall.start_pos.y)
            angle2 = self.get_line_degree_with_2_points(x, y, wall.end_pos.x, wall.end_pos.y)
            if angle1 < angle < angle2 or angle1 > angle > angle2:
                a, b, c = self.walls_line_equation[i]
                h = (a * x) + (b * y) + c
                if h != 0:
                    x2 = x + self.world_map["medics"]["laser_range"] * math.cos(math.radians(angle))
                    y2 = y - self.world_map["medics"]["laser_range"] * math.sin(math.radians(angle))
                    fire_line_eq = ((y - y2), (x2 - x), ((y * (x - x2)) + (x * (y2 - y))))
                    a, b = self.get_lines_meet_point(fire_line_eq, self.walls_line_equation[i])
                    if ((x-a)**2 + (y - b)**2)**0.5 <= ((x-x_max)**2 + (y - y_max)**2)**0.5:
                        x_max, y_max = a, b
                    result.append(self.get_lines_meet_point(fire_line_eq, self.walls_line_equation[i]))
        return x_max, y_max, fire_line_eq

    def check_fire_crush_the_medics(self, x_src, y_src, x_dst, y_dst, line_eq, medic):
        res_medic = None
        for side in self.world.medics:
            if side != medic.side_name:
                for i in range(len(self.world.medics[side])):
                    a, b, c = line_eq
                    o_medic = self.world.medics[side][i]
                    dist = o_medic.position.x * a + o_medic.position.y * b + c
                    if dist <= o_medic.radius:
                        a1, b1 = -b, a
                        c1 = -(o_medic.position.x * a1 + o_medic.position.y * b1)
                        crush_line_eq = [a1, b1, c1]
                        x2, y2 = self.get_lines_meet_point(line_eq, crush_line_eq)
                        if ((x2 - x_src)**2 + (y2 - y_src)**2)**0.5 <= ((x_dst - x_src)**2 + (y_dst - y_src)**2)**0.5:
                            x_dst, y_dst = x2, y2
                            res_medic = o_medic

        return x_dst, y_dst, res_medic



    def _get_fire_max_point(self, x1, y1, angle):
        x = x1 + math.cos(math.radians(angle)) * self.world_map["medics"]["laser_range"]
        y = y1 + math.sin(math.radians(angle)) * self.world_map["medics"]["laser_range"]
        return x, y

    @staticmethod
    def get_line_degree_with_2_points(x1, y1, x2, y2):

        if x2 - x1 == 0.0:
            return 90.0 if y2 - y1 > 0 else 270.0
        else:
            if x2 - x1 > 0 and y2 - y1 > 0:
                return math.degrees(math.atan((y2 - y1) / (x2 - x1)))
            elif x2 - x1 < 0 < y2 - y1 > 0:
                return math.degrees(math.atan((y2 - y1) / (x2 - x1))) + 180.0
            elif x2 - x1 < 0 and y2 - y1 < 0:
                return math.degrees(math.atan((y2 - y1) / (x2 - x1))) + 180.0
            else:
                return (math.degrees(math.atan((y2 - y1) / (x2 - x1)) + 360.0)) % 360

    @staticmethod
    def get_lines_meet_point(line_eq1, line_eq2):
        # also may use to solve 2in2 matrix
        # lines equation: ax + by + c = 0
        a1 = line_eq1[0]
        b1 = line_eq1[1]
        c1 = line_eq1[2]

        a2 = line_eq2[0]
        b2 = line_eq2[1]
        c2 = line_eq2[2]

        det = a1 * b2 - b1 * a2
        if det == 0.0:
            return
        else:
            x = (b2 * (-c1) + ((-b1) * (-c2))) / det
            y = ((-a2) * (-c1) + (a1 * (-c2))) / det
            return x, y

    @staticmethod
    def get_line_and_circle_meet_point(r, center_pos, start_pos):
        pass

    @staticmethod
    def get_point_and_circle_tangent_point(r, center_pos, start_pos):
        pass

    def check_crush_line_and_circle(self, r, circle_pos, line_eq, x, y):
        pass

    @staticmethod
    def get_line_formula_by_angle_and_point(x, y, angle):
        if angle == 90.0 or angle == 270.0:
            return [1.0, 0.0, x]  # ax + by + c = 0
        else:
            return [-1 * math.tan(math.radians(angle)), 1, math.tan(math.radians(angle)) * x - y]

    @staticmethod
    def get_2_points_distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
