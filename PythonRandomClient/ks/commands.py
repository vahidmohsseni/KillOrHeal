# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class Move(object):

	@staticmethod
	def name():
		return 'Move'


	def __init__(self, id=None, distance=None):
		self.initialize(id, distance)
	

	def initialize(self, id=None, distance=None):
		self.id = id
		self.distance = distance
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.distance
		s += b'\x00' if self.distance is None else b'\x01'
		if self.distance is not None:
			s += struct.pack('f', self.distance)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.distance
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			self.distance = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.distance = None
		
		return offset


class Turn(object):

	@staticmethod
	def name():
		return 'Turn'


	def __init__(self, id=None, clockwise=None, angle=None):
		self.initialize(id, clockwise, angle)
	

	def initialize(self, id=None, clockwise=None, angle=None):
		self.id = id
		self.clockwise = clockwise
		self.angle = angle
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.clockwise
		s += b'\x00' if self.clockwise is None else b'\x01'
		if self.clockwise is not None:
			s += struct.pack('?', self.clockwise)
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.clockwise
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.clockwise = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.clockwise = None
		
		# deserialize self.angle
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		return offset


class Fire(object):

	@staticmethod
	def name():
		return 'Fire'


	def __init__(self, id=None, clockwise=None, angle=None):
		self.initialize(id, clockwise, angle)
	

	def initialize(self, id=None, clockwise=None, angle=None):
		self.id = id
		self.clockwise = clockwise
		self.angle = angle
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.clockwise
		s += b'\x00' if self.clockwise is None else b'\x01'
		if self.clockwise is not None:
			s += struct.pack('?', self.clockwise)
		
		# serialize self.angle
		s += b'\x00' if self.angle is None else b'\x01'
		if self.angle is not None:
			s += struct.pack('f', self.angle)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.clockwise
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.clockwise = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.clockwise = None
		
		# deserialize self.angle
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.angle = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.angle = None
		
		return offset
