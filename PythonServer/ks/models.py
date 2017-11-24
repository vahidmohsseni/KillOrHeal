# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Position(object):

	@staticmethod
	def name():
		return 'Position'


	def __init__(self, x=None, y=None):
		self.initialize(x, y)
	

	def initialize(self, x=None, y=None):
		self.x = x
		self.y = y
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('f', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('f', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.x = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.y = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		return offset


class PowerUpType(Enum):
	LASER = 0
	HEAL_PACK = 1


class PowerUp(object):

	@staticmethod
	def name():
		return 'PowerUp'


	def __init__(self, type=None, position=None, appearance_time=None, value=None):
		self.initialize(type, position, appearance_time, value)
	

	def initialize(self, type=None, position=None, appearance_time=None, value=None):
		self.type = type
		self.position = position
		self.appearance_time = appearance_time
		self.value = value
	

	def serialize(self):
		s = b''
		
		# serialize self.type
		s += b'\x00' if self.type is None else b'\x01'
		if self.type is not None:
			s += struct.pack('b', self.type.value)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.appearance_time
		s += b'\x00' if self.appearance_time is None else b'\x01'
		if self.appearance_time is not None:
			s += struct.pack('i', self.appearance_time)
		
		# serialize self.value
		s += b'\x00' if self.value is None else b'\x01'
		if self.value is not None:
			s += struct.pack('i', self.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.type
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			tmp3 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.type = PowerUpType(tmp3)
		else:
			self.type = None
		
		# deserialize self.position
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.appearance_time
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.appearance_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.appearance_time = None
		
		# deserialize self.value
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.value = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.value = None
		
		return offset


class Medic(object):

	@staticmethod
	def name():
		return 'Medic'


	def __init__(self, id=None, side_name=None, position=None, radius=None, max_move_distance=None, angle=None, max_turn_angle=None, max_fire_angle=None, health=None, max_health=None, laser_count=None, laser_damage=None, laser_range=None, laser_max_count=None, healing_remaining_time=None, time_to_reload=None, reload_time=None, death_score=None):
		self.initialize(id, side_name, position, radius, max_move_distance, angle, max_turn_angle, max_fire_angle, health, max_health, laser_count, laser_damage, laser_range, laser_max_count, healing_remaining_time, time_to_reload, reload_time, death_score)
	

	def initialize(self, id=None, side_name=None, position=None, radius=None, max_move_distance=None, angle=None, max_turn_angle=None, max_fire_angle=None, health=None, max_health=None, laser_count=None, laser_damage=None, laser_range=None, laser_max_count=None, healing_remaining_time=None, time_to_reload=None, reload_time=None, death_score=None):
		self.id = id
		self.side_name = side_name
		self.position = position
		self.radius = radius
		self.max_move_distance = max_move_distance
		self.angle = angle
		self.max_turn_angle = max_turn_angle
		self.max_fire_angle = max_fire_angle
		self.health = health
		self.max_health = max_health
		self.laser_count = laser_count
		self.laser_damage = laser_damage
		self.laser_range = laser_range
		self.laser_max_count = laser_max_count
		self.healing_remaining_time = healing_remaining_time
		self.time_to_reload = time_to_reload
		self.reload_time = reload_time
		self.death_score = death_score
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.side_name
		s += b'\x00' if self.side_name is None else b'\x01'
		if self.side_name is not None:
			tmp7 = b''
			tmp7 += struct.pack('I', len(self.side_name))
			while len(tmp7) and tmp7[-1] == b'\x00'[0]:
				tmp7 = tmp7[:-1]
			s += struct.pack('B', len(tmp7))
			s += tmp7
			
			s += self.side_name.encode('ISO-8859-1') if PY3 else self.side_name
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.radius
		s += b'\x00' if self.radius is None else b'\x01'
		if self.radius is not None:
			s += struct.pack('f', self.radius)
		
		# serialize self.max_move_distance
		s += b'\x00' if self.max_move_distance is None else b'\x01'
		if self.max_move_distance is not None:
			s += struct.pack('f', self.max_move_distance)
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.max_turn_angle
		s += b'\x00' if self.max_turn_angle is None else b'\x01'
		if self.max_turn_angle is not None:
			s += struct.pack('f', self.max_turn_angle)
		
		# serialize self.max_fire_angle
		s += b'\x00' if self.max_fire_angle is None else b'\x01'
		if self.max_fire_angle is not None:
			s += struct.pack('f', self.max_fire_angle)
		
		# serialize self.health
		s += b'\x00' if self.health is None else b'\x01'
		if self.health is not None:
			s += struct.pack('i', self.health)
		
		# serialize self.max_health
		s += b'\x00' if self.max_health is None else b'\x01'
		if self.max_health is not None:
			s += struct.pack('i', self.max_health)
		
		# serialize self.laser_count
		s += b'\x00' if self.laser_count is None else b'\x01'
		if self.laser_count is not None:
			s += struct.pack('i', self.laser_count)
		
		# serialize self.laser_damage
		s += b'\x00' if self.laser_damage is None else b'\x01'
		if self.laser_damage is not None:
			s += struct.pack('i', self.laser_damage)
		
		# serialize self.laser_range
		s += b'\x00' if self.laser_range is None else b'\x01'
		if self.laser_range is not None:
			s += struct.pack('f', self.laser_range)
		
		# serialize self.laser_max_count
		s += b'\x00' if self.laser_max_count is None else b'\x01'
		if self.laser_max_count is not None:
			s += struct.pack('i', self.laser_max_count)
		
		# serialize self.healing_remaining_time
		s += b'\x00' if self.healing_remaining_time is None else b'\x01'
		if self.healing_remaining_time is not None:
			s += struct.pack('i', self.healing_remaining_time)
		
		# serialize self.time_to_reload
		s += b'\x00' if self.time_to_reload is None else b'\x01'
		if self.time_to_reload is not None:
			s += struct.pack('i', self.time_to_reload)
		
		# serialize self.reload_time
		s += b'\x00' if self.reload_time is None else b'\x01'
		if self.reload_time is not None:
			s += struct.pack('i', self.reload_time)
		
		# serialize self.death_score
		s += b'\x00' if self.death_score is None else b'\x01'
		if self.death_score is not None:
			s += struct.pack('i', self.death_score)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.side_name
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp11 = s[offset:offset + tmp10]
			offset += tmp10
			tmp11 += b'\x00' * (4 - tmp10)
			tmp12 = struct.unpack('I', tmp11)[0]
			
			self.side_name = s[offset:offset + tmp12].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp12]
			offset += tmp12
		else:
			self.side_name = None
		
		# deserialize self.position
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.radius
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.radius = None
		
		# deserialize self.max_move_distance
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.max_move_distance = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_move_distance = None
		
		# deserialize self.angle
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.max_turn_angle
		tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp17:
			self.max_turn_angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_turn_angle = None
		
		# deserialize self.max_fire_angle
		tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp18:
			self.max_fire_angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_fire_angle = None
		
		# deserialize self.health
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			self.health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.health = None
		
		# deserialize self.max_health
		tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp20:
			self.max_health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_health = None
		
		# deserialize self.laser_count
		tmp21 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp21:
			self.laser_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_count = None
		
		# deserialize self.laser_damage
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			self.laser_damage = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_damage = None
		
		# deserialize self.laser_range
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			self.laser_range = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_range = None
		
		# deserialize self.laser_max_count
		tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp24:
			self.laser_max_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_max_count = None
		
		# deserialize self.healing_remaining_time
		tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp25:
			self.healing_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.healing_remaining_time = None
		
		# deserialize self.time_to_reload
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			self.time_to_reload = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.time_to_reload = None
		
		# deserialize self.reload_time
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.reload_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.reload_time = None
		
		# deserialize self.death_score
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.death_score = None
		
		return offset


class Patient(object):

	@staticmethod
	def name():
		return 'Patient'


	def __init__(self, position=None, radius=None, healing_duration=None, capturable=None, heal_score=None):
		self.initialize(position, radius, healing_duration, capturable, heal_score)
	

	def initialize(self, position=None, radius=None, healing_duration=None, capturable=None, heal_score=None):
		self.position = position
		self.radius = radius
		self.healing_duration = healing_duration
		self.capturable = capturable
		self.heal_score = heal_score
	

	def serialize(self):
		s = b''
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.radius
		s += b'\x00' if self.radius is None else b'\x01'
		if self.radius is not None:
			s += struct.pack('f', self.radius)
		
		# serialize self.healing_duration
		s += b'\x00' if self.healing_duration is None else b'\x01'
		if self.healing_duration is not None:
			s += struct.pack('i', self.healing_duration)
		
		# serialize self.capturable
		s += b'\x00' if self.capturable is None else b'\x01'
		if self.capturable is not None:
			s += struct.pack('?', self.capturable)
		
		# serialize self.heal_score
		s += b'\x00' if self.heal_score is None else b'\x01'
		if self.heal_score is not None:
			s += struct.pack('i', self.heal_score)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.position
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.radius
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.radius = None
		
		# deserialize self.healing_duration
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.healing_duration = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.healing_duration = None
		
		# deserialize self.capturable
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
			self.capturable = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.capturable = None
		
		# deserialize self.heal_score
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
			self.heal_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.heal_score = None
		
		return offset


class Wall(object):

	@staticmethod
	def name():
		return 'Wall'


	def __init__(self, start_pos=None, end_pos=None):
		self.initialize(start_pos, end_pos)
	

	def initialize(self, start_pos=None, end_pos=None):
		self.start_pos = start_pos
		self.end_pos = end_pos
	

	def serialize(self):
		s = b''
		
		# serialize self.start_pos
		s += b'\x00' if self.start_pos is None else b'\x01'
		if self.start_pos is not None:
			s += self.start_pos.serialize()
		
		# serialize self.end_pos
		s += b'\x00' if self.end_pos is None else b'\x01'
		if self.end_pos is not None:
			s += self.end_pos.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.start_pos
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			self.start_pos = Position()
			offset = self.start_pos.deserialize(s, offset)
		else:
			self.start_pos = None
		
		# deserialize self.end_pos
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			self.end_pos = Position()
			offset = self.end_pos.deserialize(s, offset)
		else:
			self.end_pos = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, width=None, height=None, scores=None, medics=None, walls=None, patients=None, powerups=None):
		self.initialize(width, height, scores, medics, walls, patients, powerups)
	

	def initialize(self, width=None, height=None, scores=None, medics=None, walls=None, patients=None, powerups=None):
		self.width = width
		self.height = height
		self.scores = scores
		self.medics = medics
		self.walls = walls
		self.patients = patients
		self.powerups = powerups
	

	def serialize(self):
		s = b''
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('f', self.width)
		
		# serialize self.height
		s += b'\x00' if self.height is None else b'\x01'
		if self.height is not None:
			s += struct.pack('f', self.height)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp36 = b''
			tmp36 += struct.pack('I', len(self.scores))
			while len(tmp36) and tmp36[-1] == b'\x00'[0]:
				tmp36 = tmp36[:-1]
			s += struct.pack('B', len(tmp36))
			s += tmp36
			
			for tmp37 in self.scores:
				s += b'\x00' if tmp37 is None else b'\x01'
				if tmp37 is not None:
					tmp38 = b''
					tmp38 += struct.pack('I', len(tmp37))
					while len(tmp38) and tmp38[-1] == b'\x00'[0]:
						tmp38 = tmp38[:-1]
					s += struct.pack('B', len(tmp38))
					s += tmp38
					
					s += tmp37.encode('ISO-8859-1') if PY3 else tmp37
				s += b'\x00' if self.scores[tmp37] is None else b'\x01'
				if self.scores[tmp37] is not None:
					s += struct.pack('i', self.scores[tmp37])
		
		# serialize self.medics
		s += b'\x00' if self.medics is None else b'\x01'
		if self.medics is not None:
			tmp39 = b''
			tmp39 += struct.pack('I', len(self.medics))
			while len(tmp39) and tmp39[-1] == b'\x00'[0]:
				tmp39 = tmp39[:-1]
			s += struct.pack('B', len(tmp39))
			s += tmp39
			
			for tmp40 in self.medics:
				s += b'\x00' if tmp40 is None else b'\x01'
				if tmp40 is not None:
					tmp41 = b''
					tmp41 += struct.pack('I', len(tmp40))
					while len(tmp41) and tmp41[-1] == b'\x00'[0]:
						tmp41 = tmp41[:-1]
					s += struct.pack('B', len(tmp41))
					s += tmp41
					
					s += tmp40.encode('ISO-8859-1') if PY3 else tmp40
				s += b'\x00' if self.medics[tmp40] is None else b'\x01'
				if self.medics[tmp40] is not None:
					tmp42 = b''
					tmp42 += struct.pack('I', len(self.medics[tmp40]))
					while len(tmp42) and tmp42[-1] == b'\x00'[0]:
						tmp42 = tmp42[:-1]
					s += struct.pack('B', len(tmp42))
					s += tmp42
					
					for tmp43 in self.medics[tmp40]:
						s += b'\x00' if tmp43 is None else b'\x01'
						if tmp43 is not None:
							s += tmp43.serialize()
		
		# serialize self.walls
		s += b'\x00' if self.walls is None else b'\x01'
		if self.walls is not None:
			tmp44 = b''
			tmp44 += struct.pack('I', len(self.walls))
			while len(tmp44) and tmp44[-1] == b'\x00'[0]:
				tmp44 = tmp44[:-1]
			s += struct.pack('B', len(tmp44))
			s += tmp44
			
			for tmp45 in self.walls:
				s += b'\x00' if tmp45 is None else b'\x01'
				if tmp45 is not None:
					s += tmp45.serialize()
		
		# serialize self.patients
		s += b'\x00' if self.patients is None else b'\x01'
		if self.patients is not None:
			tmp46 = b''
			tmp46 += struct.pack('I', len(self.patients))
			while len(tmp46) and tmp46[-1] == b'\x00'[0]:
				tmp46 = tmp46[:-1]
			s += struct.pack('B', len(tmp46))
			s += tmp46
			
			for tmp47 in self.patients:
				s += b'\x00' if tmp47 is None else b'\x01'
				if tmp47 is not None:
					s += tmp47.serialize()
		
		# serialize self.powerups
		s += b'\x00' if self.powerups is None else b'\x01'
		if self.powerups is not None:
			tmp48 = b''
			tmp48 += struct.pack('I', len(self.powerups))
			while len(tmp48) and tmp48[-1] == b'\x00'[0]:
				tmp48 = tmp48[:-1]
			s += struct.pack('B', len(tmp48))
			s += tmp48
			
			for tmp49 in self.powerups:
				s += b'\x00' if tmp49 is None else b'\x01'
				if tmp49 is not None:
					s += tmp49.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			self.width = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.height = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.scores
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp54 = s[offset:offset + tmp53]
			offset += tmp53
			tmp54 += b'\x00' * (4 - tmp53)
			tmp55 = struct.unpack('I', tmp54)[0]
			
			self.scores = {}
			for tmp56 in range(tmp55):
				tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp59:
					tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp61 = s[offset:offset + tmp60]
					offset += tmp60
					tmp61 += b'\x00' * (4 - tmp60)
					tmp62 = struct.unpack('I', tmp61)[0]
					
					tmp57 = s[offset:offset + tmp62].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp62]
					offset += tmp62
				else:
					tmp57 = None
				tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp63:
					tmp58 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp58 = None
				self.scores[tmp57] = tmp58
		else:
			self.scores = None
		
		# deserialize self.medics
		tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp64:
			tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp66 = s[offset:offset + tmp65]
			offset += tmp65
			tmp66 += b'\x00' * (4 - tmp65)
			tmp67 = struct.unpack('I', tmp66)[0]
			
			self.medics = {}
			for tmp68 in range(tmp67):
				tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp71:
					tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp73 = s[offset:offset + tmp72]
					offset += tmp72
					tmp73 += b'\x00' * (4 - tmp72)
					tmp74 = struct.unpack('I', tmp73)[0]
					
					tmp69 = s[offset:offset + tmp74].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp74]
					offset += tmp74
				else:
					tmp69 = None
				tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp75:
					tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp77 = s[offset:offset + tmp76]
					offset += tmp76
					tmp77 += b'\x00' * (4 - tmp76)
					tmp78 = struct.unpack('I', tmp77)[0]
					
					tmp70 = []
					for tmp79 in range(tmp78):
						tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp81:
							tmp80 = Medic()
							offset = tmp80.deserialize(s, offset)
						else:
							tmp80 = None
						tmp70.append(tmp80)
				else:
					tmp70 = None
				self.medics[tmp69] = tmp70
		else:
			self.medics = None
		
		# deserialize self.walls
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp84 = s[offset:offset + tmp83]
			offset += tmp83
			tmp84 += b'\x00' * (4 - tmp83)
			tmp85 = struct.unpack('I', tmp84)[0]
			
			self.walls = []
			for tmp86 in range(tmp85):
				tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp88:
					tmp87 = Wall()
					offset = tmp87.deserialize(s, offset)
				else:
					tmp87 = None
				self.walls.append(tmp87)
		else:
			self.walls = None
		
		# deserialize self.patients
		tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp89:
			tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp91 = s[offset:offset + tmp90]
			offset += tmp90
			tmp91 += b'\x00' * (4 - tmp90)
			tmp92 = struct.unpack('I', tmp91)[0]
			
			self.patients = []
			for tmp93 in range(tmp92):
				tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp95:
					tmp94 = Patient()
					offset = tmp94.deserialize(s, offset)
				else:
					tmp94 = None
				self.patients.append(tmp94)
		else:
			self.patients = None
		
		# deserialize self.powerups
		tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp96:
			tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp98 = s[offset:offset + tmp97]
			offset += tmp97
			tmp98 += b'\x00' * (4 - tmp97)
			tmp99 = struct.unpack('I', tmp98)[0]
			
			self.powerups = []
			for tmp100 in range(tmp99):
				tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp102:
					tmp101 = PowerUp()
					offset = tmp101.deserialize(s, offset)
				else:
					tmp101 = None
				self.powerups.append(tmp101)
		else:
			self.powerups = None
		
		return offset
