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


	def __init__(self, type=None, position=None, apearance_time=None, value=None):
		self.initialize(type, position, apearance_time, value)
	

	def initialize(self, type=None, position=None, apearance_time=None, value=None):
		self.type = type
		self.position = position
		self.apearance_time = apearance_time
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
		
		# serialize self.apearance_time
		s += b'\x00' if self.apearance_time is None else b'\x01'
		if self.apearance_time is not None:
			s += struct.pack('i', self.apearance_time)
		
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
		
		# deserialize self.apearance_time
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.apearance_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.apearance_time = None
		
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


	def __init__(self, id=None, side_name=None, position=None, radius=None, max_move_distance=None, angle=None, max_turn_angle=None, health=None, max_health=None, laser_count=None, laser_range=None, laser_max_count=None, death_score=None):
		self.initialize(id, side_name, position, radius, max_move_distance, angle, max_turn_angle, health, max_health, laser_count, laser_range, laser_max_count, death_score)
	

	def initialize(self, id=None, side_name=None, position=None, radius=None, max_move_distance=None, angle=None, max_turn_angle=None, health=None, max_health=None, laser_count=None, laser_range=None, laser_max_count=None, death_score=None):
		self.id = id
		self.side_name = side_name
		self.position = position
		self.radius = radius
		self.max_move_distance = max_move_distance
		self.angle = angle
		self.max_turn_angle = max_turn_angle
		self.health = health
		self.max_health = max_health
		self.laser_count = laser_count
		self.laser_range = laser_range
		self.laser_max_count = laser_max_count
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
		
		# serialize self.laser_range
		s += b'\x00' if self.laser_range is None else b'\x01'
		if self.laser_range is not None:
			s += struct.pack('f', self.laser_range)
		
		# serialize self.laser_max_count
		s += b'\x00' if self.laser_max_count is None else b'\x01'
		if self.laser_max_count is not None:
			s += struct.pack('i', self.laser_max_count)
		
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
		
		# deserialize self.health
		tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp18:
			self.health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.health = None
		
		# deserialize self.max_health
		tmp19 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp19:
			self.max_health = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_health = None
		
		# deserialize self.laser_count
		tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp20:
			self.laser_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_count = None
		
		# deserialize self.laser_range
		tmp21 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp21:
			self.laser_range = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_range = None
		
		# deserialize self.laser_max_count
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			self.laser_max_count = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.laser_max_count = None
		
		# deserialize self.death_score
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
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
		tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp24:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.radius
		tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp25:
			self.radius = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.radius = None
		
		# deserialize self.healing_duration
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			self.healing_duration = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.healing_duration = None
		
		# deserialize self.capturable
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.capturable = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.capturable = None
		
		# deserialize self.heal_score
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.heal_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.heal_score = None
		
		return offset


class Wall(object):

	@staticmethod
	def name():
		return 'Wall'


	def __init__(self, position=None, angle=None, length=None):
		self.initialize(position, angle, length)
	

	def initialize(self, position=None, angle=None, length=None):
		self.position = position
		self.angle = angle
		self.length = length
	

	def serialize(self):
		s = b''
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		# serialize self.length
		s += b'\x00' if self.length is None else b'\x01'
		if self.length is not None:
			s += struct.pack('f', self.length)
		
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
		
		# deserialize self.angle
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		# deserialize self.length
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.length = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.length = None
		
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
			tmp32 = b''
			tmp32 += struct.pack('I', len(self.scores))
			while len(tmp32) and tmp32[-1] == b'\x00'[0]:
				tmp32 = tmp32[:-1]
			s += struct.pack('B', len(tmp32))
			s += tmp32
			
			for tmp33 in self.scores:
				s += b'\x00' if tmp33 is None else b'\x01'
				if tmp33 is not None:
					tmp34 = b''
					tmp34 += struct.pack('I', len(tmp33))
					while len(tmp34) and tmp34[-1] == b'\x00'[0]:
						tmp34 = tmp34[:-1]
					s += struct.pack('B', len(tmp34))
					s += tmp34
					
					s += tmp33.encode('ISO-8859-1') if PY3 else tmp33
				s += b'\x00' if self.scores[tmp33] is None else b'\x01'
				if self.scores[tmp33] is not None:
					s += struct.pack('i', self.scores[tmp33])
		
		# serialize self.medics
		s += b'\x00' if self.medics is None else b'\x01'
		if self.medics is not None:
			tmp35 = b''
			tmp35 += struct.pack('I', len(self.medics))
			while len(tmp35) and tmp35[-1] == b'\x00'[0]:
				tmp35 = tmp35[:-1]
			s += struct.pack('B', len(tmp35))
			s += tmp35
			
			for tmp36 in self.medics:
				s += b'\x00' if tmp36 is None else b'\x01'
				if tmp36 is not None:
					tmp37 = b''
					tmp37 += struct.pack('I', len(tmp36))
					while len(tmp37) and tmp37[-1] == b'\x00'[0]:
						tmp37 = tmp37[:-1]
					s += struct.pack('B', len(tmp37))
					s += tmp37
					
					s += tmp36.encode('ISO-8859-1') if PY3 else tmp36
				s += b'\x00' if self.medics[tmp36] is None else b'\x01'
				if self.medics[tmp36] is not None:
					tmp38 = b''
					tmp38 += struct.pack('I', len(self.medics[tmp36]))
					while len(tmp38) and tmp38[-1] == b'\x00'[0]:
						tmp38 = tmp38[:-1]
					s += struct.pack('B', len(tmp38))
					s += tmp38
					
					for tmp39 in self.medics[tmp36]:
						s += b'\x00' if tmp39 is None else b'\x01'
						if tmp39 is not None:
							s += tmp39.serialize()
		
		# serialize self.walls
		s += b'\x00' if self.walls is None else b'\x01'
		if self.walls is not None:
			tmp40 = b''
			tmp40 += struct.pack('I', len(self.walls))
			while len(tmp40) and tmp40[-1] == b'\x00'[0]:
				tmp40 = tmp40[:-1]
			s += struct.pack('B', len(tmp40))
			s += tmp40
			
			for tmp41 in self.walls:
				s += b'\x00' if tmp41 is None else b'\x01'
				if tmp41 is not None:
					s += tmp41.serialize()
		
		# serialize self.patients
		s += b'\x00' if self.patients is None else b'\x01'
		if self.patients is not None:
			tmp42 = b''
			tmp42 += struct.pack('I', len(self.patients))
			while len(tmp42) and tmp42[-1] == b'\x00'[0]:
				tmp42 = tmp42[:-1]
			s += struct.pack('B', len(tmp42))
			s += tmp42
			
			for tmp43 in self.patients:
				s += b'\x00' if tmp43 is None else b'\x01'
				if tmp43 is not None:
					s += tmp43.serialize()
		
		# serialize self.powerups
		s += b'\x00' if self.powerups is None else b'\x01'
		if self.powerups is not None:
			tmp44 = b''
			tmp44 += struct.pack('I', len(self.powerups))
			while len(tmp44) and tmp44[-1] == b'\x00'[0]:
				tmp44 = tmp44[:-1]
			s += struct.pack('B', len(tmp44))
			s += tmp44
			
			for tmp45 in self.powerups:
				s += b'\x00' if tmp45 is None else b'\x01'
				if tmp45 is not None:
					s += tmp45.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			self.width = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp47:
			self.height = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.scores
		tmp48 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp48:
			tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp50 = s[offset:offset + tmp49]
			offset += tmp49
			tmp50 += b'\x00' * (4 - tmp49)
			tmp51 = struct.unpack('I', tmp50)[0]
			
			self.scores = {}
			for tmp52 in range(tmp51):
				tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp55:
					tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp57 = s[offset:offset + tmp56]
					offset += tmp56
					tmp57 += b'\x00' * (4 - tmp56)
					tmp58 = struct.unpack('I', tmp57)[0]
					
					tmp53 = s[offset:offset + tmp58].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp58]
					offset += tmp58
				else:
					tmp53 = None
				tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp59:
					tmp54 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp54 = None
				self.scores[tmp53] = tmp54
		else:
			self.scores = None
		
		# deserialize self.medics
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp62 = s[offset:offset + tmp61]
			offset += tmp61
			tmp62 += b'\x00' * (4 - tmp61)
			tmp63 = struct.unpack('I', tmp62)[0]
			
			self.medics = {}
			for tmp64 in range(tmp63):
				tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp67:
					tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp69 = s[offset:offset + tmp68]
					offset += tmp68
					tmp69 += b'\x00' * (4 - tmp68)
					tmp70 = struct.unpack('I', tmp69)[0]
					
					tmp65 = s[offset:offset + tmp70].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp70]
					offset += tmp70
				else:
					tmp65 = None
				tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp71:
					tmp72 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp73 = s[offset:offset + tmp72]
					offset += tmp72
					tmp73 += b'\x00' * (4 - tmp72)
					tmp74 = struct.unpack('I', tmp73)[0]
					
					tmp66 = []
					for tmp75 in range(tmp74):
						tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp77:
							tmp76 = Medic()
							offset = tmp76.deserialize(s, offset)
						else:
							tmp76 = None
						tmp66.append(tmp76)
				else:
					tmp66 = None
				self.medics[tmp65] = tmp66
		else:
			self.medics = None
		
		# deserialize self.walls
		tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp78:
			tmp79 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp80 = s[offset:offset + tmp79]
			offset += tmp79
			tmp80 += b'\x00' * (4 - tmp79)
			tmp81 = struct.unpack('I', tmp80)[0]
			
			self.walls = []
			for tmp82 in range(tmp81):
				tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp84:
					tmp83 = Wall()
					offset = tmp83.deserialize(s, offset)
				else:
					tmp83 = None
				self.walls.append(tmp83)
		else:
			self.walls = None
		
		# deserialize self.patients
		tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp85:
			tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp87 = s[offset:offset + tmp86]
			offset += tmp86
			tmp87 += b'\x00' * (4 - tmp86)
			tmp88 = struct.unpack('I', tmp87)[0]
			
			self.patients = []
			for tmp89 in range(tmp88):
				tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp91:
					tmp90 = Patient()
					offset = tmp90.deserialize(s, offset)
				else:
					tmp90 = None
				self.patients.append(tmp90)
		else:
			self.patients = None
		
		# deserialize self.powerups
		tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp92:
			tmp93 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp94 = s[offset:offset + tmp93]
			offset += tmp93
			tmp94 += b'\x00' * (4 - tmp93)
			tmp95 = struct.unpack('I', tmp94)[0]
			
			self.powerups = []
			for tmp96 in range(tmp95):
				tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp98:
					tmp97 = PowerUp()
					offset = tmp97.deserialize(s, offset)
				else:
					tmp97 = None
				self.powerups.append(tmp97)
		else:
			self.powerups = None
		
		return offset
