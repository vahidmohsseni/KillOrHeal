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


	def __init__(self, id=None, side_name=None, position=None, radius=None, max_move_distance=None, angle=None, max_turn_angle=None, max_fire_angle=None, health=None, max_health=None, laser_count=None, laser_damage=None, laser_range=None, laser_max_count=None, healing_remaining_time=None, death_score=None):
		self.initialize(id, side_name, position, radius, max_move_distance, angle, max_turn_angle, max_fire_angle, health, max_health, laser_count, laser_damage, laser_range, laser_max_count, healing_remaining_time, death_score)
	

	def initialize(self, id=None, side_name=None, position=None, radius=None, max_move_distance=None, angle=None, max_turn_angle=None, max_fire_angle=None, health=None, max_health=None, laser_count=None, laser_damage=None, laser_range=None, laser_max_count=None, healing_remaining_time=None, death_score=None):
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
		
		# deserialize self.death_score
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
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
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.radius
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.radius = None
		
		# deserialize self.healing_duration
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.healing_duration = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.healing_duration = None
		
		# deserialize self.capturable
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.capturable = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.capturable = None
		
		# deserialize self.heal_score
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
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
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
			self.start_pos = Position()
			offset = self.start_pos.deserialize(s, offset)
		else:
			self.start_pos = None
		
		# deserialize self.end_pos
		tmp33 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp33:
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
			tmp34 = b''
			tmp34 += struct.pack('I', len(self.scores))
			while len(tmp34) and tmp34[-1] == b'\x00'[0]:
				tmp34 = tmp34[:-1]
			s += struct.pack('B', len(tmp34))
			s += tmp34
			
			for tmp35 in self.scores:
				s += b'\x00' if tmp35 is None else b'\x01'
				if tmp35 is not None:
					tmp36 = b''
					tmp36 += struct.pack('I', len(tmp35))
					while len(tmp36) and tmp36[-1] == b'\x00'[0]:
						tmp36 = tmp36[:-1]
					s += struct.pack('B', len(tmp36))
					s += tmp36
					
					s += tmp35.encode('ISO-8859-1') if PY3 else tmp35
				s += b'\x00' if self.scores[tmp35] is None else b'\x01'
				if self.scores[tmp35] is not None:
					s += struct.pack('i', self.scores[tmp35])
		
		# serialize self.medics
		s += b'\x00' if self.medics is None else b'\x01'
		if self.medics is not None:
			tmp37 = b''
			tmp37 += struct.pack('I', len(self.medics))
			while len(tmp37) and tmp37[-1] == b'\x00'[0]:
				tmp37 = tmp37[:-1]
			s += struct.pack('B', len(tmp37))
			s += tmp37
			
			for tmp38 in self.medics:
				s += b'\x00' if tmp38 is None else b'\x01'
				if tmp38 is not None:
					tmp39 = b''
					tmp39 += struct.pack('I', len(tmp38))
					while len(tmp39) and tmp39[-1] == b'\x00'[0]:
						tmp39 = tmp39[:-1]
					s += struct.pack('B', len(tmp39))
					s += tmp39
					
					s += tmp38.encode('ISO-8859-1') if PY3 else tmp38
				s += b'\x00' if self.medics[tmp38] is None else b'\x01'
				if self.medics[tmp38] is not None:
					tmp40 = b''
					tmp40 += struct.pack('I', len(self.medics[tmp38]))
					while len(tmp40) and tmp40[-1] == b'\x00'[0]:
						tmp40 = tmp40[:-1]
					s += struct.pack('B', len(tmp40))
					s += tmp40
					
					for tmp41 in self.medics[tmp38]:
						s += b'\x00' if tmp41 is None else b'\x01'
						if tmp41 is not None:
							s += tmp41.serialize()
		
		# serialize self.walls
		s += b'\x00' if self.walls is None else b'\x01'
		if self.walls is not None:
			tmp42 = b''
			tmp42 += struct.pack('I', len(self.walls))
			while len(tmp42) and tmp42[-1] == b'\x00'[0]:
				tmp42 = tmp42[:-1]
			s += struct.pack('B', len(tmp42))
			s += tmp42
			
			for tmp43 in self.walls:
				s += b'\x00' if tmp43 is None else b'\x01'
				if tmp43 is not None:
					s += tmp43.serialize()
		
		# serialize self.patients
		s += b'\x00' if self.patients is None else b'\x01'
		if self.patients is not None:
			tmp44 = b''
			tmp44 += struct.pack('I', len(self.patients))
			while len(tmp44) and tmp44[-1] == b'\x00'[0]:
				tmp44 = tmp44[:-1]
			s += struct.pack('B', len(tmp44))
			s += tmp44
			
			for tmp45 in self.patients:
				s += b'\x00' if tmp45 is None else b'\x01'
				if tmp45 is not None:
					s += tmp45.serialize()
		
		# serialize self.powerups
		s += b'\x00' if self.powerups is None else b'\x01'
		if self.powerups is not None:
			tmp46 = b''
			tmp46 += struct.pack('I', len(self.powerups))
			while len(tmp46) and tmp46[-1] == b'\x00'[0]:
				tmp46 = tmp46[:-1]
			s += struct.pack('B', len(tmp46))
			s += tmp46
			
			for tmp47 in self.powerups:
				s += b'\x00' if tmp47 is None else b'\x01'
				if tmp47 is not None:
					s += tmp47.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			self.width = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp49:
			self.height = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.scores
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp52 = s[offset:offset + tmp51]
			offset += tmp51
			tmp52 += b'\x00' * (4 - tmp51)
			tmp53 = struct.unpack('I', tmp52)[0]
			
			self.scores = {}
			for tmp54 in range(tmp53):
				tmp57 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp57:
					tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp59 = s[offset:offset + tmp58]
					offset += tmp58
					tmp59 += b'\x00' * (4 - tmp58)
					tmp60 = struct.unpack('I', tmp59)[0]
					
					tmp55 = s[offset:offset + tmp60].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp60]
					offset += tmp60
				else:
					tmp55 = None
				tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp61:
					tmp56 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp56 = None
				self.scores[tmp55] = tmp56
		else:
			self.scores = None
		
		# deserialize self.medics
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp64 = s[offset:offset + tmp63]
			offset += tmp63
			tmp64 += b'\x00' * (4 - tmp63)
			tmp65 = struct.unpack('I', tmp64)[0]
			
			self.medics = {}
			for tmp66 in range(tmp65):
				tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp69:
					tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp71 = s[offset:offset + tmp70]
					offset += tmp70
					tmp71 += b'\x00' * (4 - tmp70)
					tmp72 = struct.unpack('I', tmp71)[0]
					
					tmp67 = s[offset:offset + tmp72].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp72]
					offset += tmp72
				else:
					tmp67 = None
				tmp73 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp73:
					tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp75 = s[offset:offset + tmp74]
					offset += tmp74
					tmp75 += b'\x00' * (4 - tmp74)
					tmp76 = struct.unpack('I', tmp75)[0]
					
					tmp68 = []
					for tmp77 in range(tmp76):
						tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp79:
							tmp78 = Medic()
							offset = tmp78.deserialize(s, offset)
						else:
							tmp78 = None
						tmp68.append(tmp78)
				else:
					tmp68 = None
				self.medics[tmp67] = tmp68
		else:
			self.medics = None
		
		# deserialize self.walls
		tmp80 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp80:
			tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp82 = s[offset:offset + tmp81]
			offset += tmp81
			tmp82 += b'\x00' * (4 - tmp81)
			tmp83 = struct.unpack('I', tmp82)[0]
			
			self.walls = []
			for tmp84 in range(tmp83):
				tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp86:
					tmp85 = Wall()
					offset = tmp85.deserialize(s, offset)
				else:
					tmp85 = None
				self.walls.append(tmp85)
		else:
			self.walls = None
		
		# deserialize self.patients
		tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp87:
			tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp89 = s[offset:offset + tmp88]
			offset += tmp88
			tmp89 += b'\x00' * (4 - tmp88)
			tmp90 = struct.unpack('I', tmp89)[0]
			
			self.patients = []
			for tmp91 in range(tmp90):
				tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp93:
					tmp92 = Patient()
					offset = tmp92.deserialize(s, offset)
				else:
					tmp92 = None
				self.patients.append(tmp92)
		else:
			self.patients = None
		
		# deserialize self.powerups
		tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp94:
			tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp96 = s[offset:offset + tmp95]
			offset += tmp95
			tmp96 += b'\x00' * (4 - tmp95)
			tmp97 = struct.unpack('I', tmp96)[0]
			
			self.powerups = []
			for tmp98 in range(tmp97):
				tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp100:
					tmp99 = PowerUp()
					offset = tmp99.deserialize(s, offset)
				else:
					tmp99 = None
				self.powerups.append(tmp99)
		else:
			self.powerups = None
		
		return offset
