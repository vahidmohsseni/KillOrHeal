[Position]
_def = class
x = float
y = float


[PowerUpType]
_def = enum<byte>
	{
		LASER,
		HEAL_PACK
	}


[PowerUp]
_def = class
type = PowerUpType
position = Position
appearance_time = int
value = int


[Medic]
_def = class
id = int
side_name = string
position = Position
radius = float
max_move_distance = float
angle = float
max_turn_angle = float
health = int
max_health = int
laser_count = int
laser_damage = int
laser_range = float
laser_max_count = int
healing_remaining_time = int
death_score = int


[Patient]
_def = class
position = Position
radius = float
healing_duration = int
capturable = boolean
heal_score = int


[Wall]
_def = class
start_pos = Position
end_pos = Position



[World]
_def = class
width = float
height = float
scores = map<string, int>
medics = map<string, list<Medic>>
walls = list<Wall>
patients = list<Patient>
powerups = list<PowerUp>
