#ifndef _KS_MODELS_H_
#define _KS_MODELS_H_

#include <string>
#include <vector>
#include <map>
#include <array>


namespace ks
{

#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{
public:
	static inline const std::string nameStatic() { return ""; }
	virtual inline const std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
};

#endif // _KS_OBJECT_


namespace models
{

class Position : public KSObject
{

protected:

	float __x;
	float __y;

	bool __has_x;
	bool __has_y;


public: // getters

	inline float x() const
	{
		return __x;
	}
	
	inline float y() const
	{
		return __y;
	}
	

public: // reference getters

	inline float &ref_x() const
	{
		return (float&) __x;
	}
	
	inline float &ref_y() const
	{
		return (float&) __y;
	}
	

public: // setters

	inline void x(const float &x)
	{
		__x = x;
		has_x(true);
	}
	
	inline void y(const float &y)
	{
		__y = y;
		has_y(true);
	}
	

public: // has_attribute getters

	inline bool has_x() const
	{
		return __has_x;
	}
	
	inline bool has_y() const
	{
		return __has_y;
	}
	

public: // has_attribute setters

	inline void has_x(const bool &has_x)
	{
		__has_x = has_x;
	}
	
	inline void has_y(const bool &has_y)
	{
		__has_y = has_y;
	}
	

public:

	Position()
	{
		has_x(false);
		has_y(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Position";
	}
	
	virtual inline const std::string name() const
	{
		return "Position";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize x
		s += __has_x;
		if (__has_x)
		{
			float tmp1 = __x;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(float));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			float tmp4 = __y;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(float));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize x
		__has_x = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_x)
		{
			__x = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize y
		__has_y = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_y)
		{
			__y = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		return offset;
	}
};


enum class PowerUpType
{
	LASER = 0,
	HEAL_PACK = 1,
};


class PowerUp : public KSObject
{

protected:

	PowerUpType __type;
	Position __position;
	int __appearance_time;
	int __value;

	bool __has_type;
	bool __has_position;
	bool __has_appearance_time;
	bool __has_value;


public: // getters

	inline PowerUpType type() const
	{
		return __type;
	}
	
	inline Position position() const
	{
		return __position;
	}
	
	inline int appearance_time() const
	{
		return __appearance_time;
	}
	
	inline int value() const
	{
		return __value;
	}
	

public: // reference getters

	inline PowerUpType &ref_type() const
	{
		return (PowerUpType&) __type;
	}
	
	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline int &ref_appearance_time() const
	{
		return (int&) __appearance_time;
	}
	
	inline int &ref_value() const
	{
		return (int&) __value;
	}
	

public: // setters

	inline void type(const PowerUpType &type)
	{
		__type = type;
		has_type(true);
	}
	
	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void appearance_time(const int &appearance_time)
	{
		__appearance_time = appearance_time;
		has_appearance_time(true);
	}
	
	inline void value(const int &value)
	{
		__value = value;
		has_value(true);
	}
	

public: // has_attribute getters

	inline bool has_type() const
	{
		return __has_type;
	}
	
	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_appearance_time() const
	{
		return __has_appearance_time;
	}
	
	inline bool has_value() const
	{
		return __has_value;
	}
	

public: // has_attribute setters

	inline void has_type(const bool &has_type)
	{
		__has_type = has_type;
	}
	
	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_appearance_time(const bool &has_appearance_time)
	{
		__has_appearance_time = has_appearance_time;
	}
	
	inline void has_value(const bool &has_value)
	{
		__has_value = has_value;
	}
	

public:

	PowerUp()
	{
		has_type(false);
		has_position(false);
		has_appearance_time(false);
		has_value(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "PowerUp";
	}
	
	virtual inline const std::string name() const
	{
		return "PowerUp";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize type
		s += __has_type;
		if (__has_type)
		{
			char tmp7 = (char) __type;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(char));
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize appearance_time
		s += __has_appearance_time;
		if (__has_appearance_time)
		{
			int tmp10 = __appearance_time;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(int));
		}
		
		// serialize value
		s += __has_value;
		if (__has_value)
		{
			int tmp13 = __value;
			auto tmp14 = reinterpret_cast<char*>(&tmp13);
			s += std::string(tmp14, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize type
		__has_type = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_type)
		{
			char tmp15;
			tmp15 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__type = (PowerUpType) tmp15;
		}
		
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize appearance_time
		__has_appearance_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_appearance_time)
		{
			__appearance_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize value
		__has_value = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_value)
		{
			__value = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Medic : public KSObject
{

protected:

	int __id;
	std::string __side_name;
	Position __position;
	float __radius;
	float __max_move_distance;
	float __angle;
	float __max_turn_angle;
	float __max_fire_angle;
	int __health;
	int __max_health;
	int __laser_count;
	int __laser_damage;
	float __laser_range;
	int __laser_max_count;
	int __healing_remaining_time;
	int __time_to_reload;
	int __reload_time;
	int __death_score;

	bool __has_id;
	bool __has_side_name;
	bool __has_position;
	bool __has_radius;
	bool __has_max_move_distance;
	bool __has_angle;
	bool __has_max_turn_angle;
	bool __has_max_fire_angle;
	bool __has_health;
	bool __has_max_health;
	bool __has_laser_count;
	bool __has_laser_damage;
	bool __has_laser_range;
	bool __has_laser_max_count;
	bool __has_healing_remaining_time;
	bool __has_time_to_reload;
	bool __has_reload_time;
	bool __has_death_score;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline std::string side_name() const
	{
		return __side_name;
	}
	
	inline Position position() const
	{
		return __position;
	}
	
	inline float radius() const
	{
		return __radius;
	}
	
	inline float max_move_distance() const
	{
		return __max_move_distance;
	}
	
	inline float angle() const
	{
		return __angle;
	}
	
	inline float max_turn_angle() const
	{
		return __max_turn_angle;
	}
	
	inline float max_fire_angle() const
	{
		return __max_fire_angle;
	}
	
	inline int health() const
	{
		return __health;
	}
	
	inline int max_health() const
	{
		return __max_health;
	}
	
	inline int laser_count() const
	{
		return __laser_count;
	}
	
	inline int laser_damage() const
	{
		return __laser_damage;
	}
	
	inline float laser_range() const
	{
		return __laser_range;
	}
	
	inline int laser_max_count() const
	{
		return __laser_max_count;
	}
	
	inline int healing_remaining_time() const
	{
		return __healing_remaining_time;
	}
	
	inline int time_to_reload() const
	{
		return __time_to_reload;
	}
	
	inline int reload_time() const
	{
		return __reload_time;
	}
	
	inline int death_score() const
	{
		return __death_score;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline std::string &ref_side_name() const
	{
		return (std::string&) __side_name;
	}
	
	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline float &ref_radius() const
	{
		return (float&) __radius;
	}
	
	inline float &ref_max_move_distance() const
	{
		return (float&) __max_move_distance;
	}
	
	inline float &ref_angle() const
	{
		return (float&) __angle;
	}
	
	inline float &ref_max_turn_angle() const
	{
		return (float&) __max_turn_angle;
	}
	
	inline float &ref_max_fire_angle() const
	{
		return (float&) __max_fire_angle;
	}
	
	inline int &ref_health() const
	{
		return (int&) __health;
	}
	
	inline int &ref_max_health() const
	{
		return (int&) __max_health;
	}
	
	inline int &ref_laser_count() const
	{
		return (int&) __laser_count;
	}
	
	inline int &ref_laser_damage() const
	{
		return (int&) __laser_damage;
	}
	
	inline float &ref_laser_range() const
	{
		return (float&) __laser_range;
	}
	
	inline int &ref_laser_max_count() const
	{
		return (int&) __laser_max_count;
	}
	
	inline int &ref_healing_remaining_time() const
	{
		return (int&) __healing_remaining_time;
	}
	
	inline int &ref_time_to_reload() const
	{
		return (int&) __time_to_reload;
	}
	
	inline int &ref_reload_time() const
	{
		return (int&) __reload_time;
	}
	
	inline int &ref_death_score() const
	{
		return (int&) __death_score;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void side_name(const std::string &side_name)
	{
		__side_name = side_name;
		has_side_name(true);
	}
	
	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void radius(const float &radius)
	{
		__radius = radius;
		has_radius(true);
	}
	
	inline void max_move_distance(const float &max_move_distance)
	{
		__max_move_distance = max_move_distance;
		has_max_move_distance(true);
	}
	
	inline void angle(const float &angle)
	{
		__angle = angle;
		has_angle(true);
	}
	
	inline void max_turn_angle(const float &max_turn_angle)
	{
		__max_turn_angle = max_turn_angle;
		has_max_turn_angle(true);
	}
	
	inline void max_fire_angle(const float &max_fire_angle)
	{
		__max_fire_angle = max_fire_angle;
		has_max_fire_angle(true);
	}
	
	inline void health(const int &health)
	{
		__health = health;
		has_health(true);
	}
	
	inline void max_health(const int &max_health)
	{
		__max_health = max_health;
		has_max_health(true);
	}
	
	inline void laser_count(const int &laser_count)
	{
		__laser_count = laser_count;
		has_laser_count(true);
	}
	
	inline void laser_damage(const int &laser_damage)
	{
		__laser_damage = laser_damage;
		has_laser_damage(true);
	}
	
	inline void laser_range(const float &laser_range)
	{
		__laser_range = laser_range;
		has_laser_range(true);
	}
	
	inline void laser_max_count(const int &laser_max_count)
	{
		__laser_max_count = laser_max_count;
		has_laser_max_count(true);
	}
	
	inline void healing_remaining_time(const int &healing_remaining_time)
	{
		__healing_remaining_time = healing_remaining_time;
		has_healing_remaining_time(true);
	}
	
	inline void time_to_reload(const int &time_to_reload)
	{
		__time_to_reload = time_to_reload;
		has_time_to_reload(true);
	}
	
	inline void reload_time(const int &reload_time)
	{
		__reload_time = reload_time;
		has_reload_time(true);
	}
	
	inline void death_score(const int &death_score)
	{
		__death_score = death_score;
		has_death_score(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_side_name() const
	{
		return __has_side_name;
	}
	
	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_radius() const
	{
		return __has_radius;
	}
	
	inline bool has_max_move_distance() const
	{
		return __has_max_move_distance;
	}
	
	inline bool has_angle() const
	{
		return __has_angle;
	}
	
	inline bool has_max_turn_angle() const
	{
		return __has_max_turn_angle;
	}
	
	inline bool has_max_fire_angle() const
	{
		return __has_max_fire_angle;
	}
	
	inline bool has_health() const
	{
		return __has_health;
	}
	
	inline bool has_max_health() const
	{
		return __has_max_health;
	}
	
	inline bool has_laser_count() const
	{
		return __has_laser_count;
	}
	
	inline bool has_laser_damage() const
	{
		return __has_laser_damage;
	}
	
	inline bool has_laser_range() const
	{
		return __has_laser_range;
	}
	
	inline bool has_laser_max_count() const
	{
		return __has_laser_max_count;
	}
	
	inline bool has_healing_remaining_time() const
	{
		return __has_healing_remaining_time;
	}
	
	inline bool has_time_to_reload() const
	{
		return __has_time_to_reload;
	}
	
	inline bool has_reload_time() const
	{
		return __has_reload_time;
	}
	
	inline bool has_death_score() const
	{
		return __has_death_score;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_side_name(const bool &has_side_name)
	{
		__has_side_name = has_side_name;
	}
	
	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_radius(const bool &has_radius)
	{
		__has_radius = has_radius;
	}
	
	inline void has_max_move_distance(const bool &has_max_move_distance)
	{
		__has_max_move_distance = has_max_move_distance;
	}
	
	inline void has_angle(const bool &has_angle)
	{
		__has_angle = has_angle;
	}
	
	inline void has_max_turn_angle(const bool &has_max_turn_angle)
	{
		__has_max_turn_angle = has_max_turn_angle;
	}
	
	inline void has_max_fire_angle(const bool &has_max_fire_angle)
	{
		__has_max_fire_angle = has_max_fire_angle;
	}
	
	inline void has_health(const bool &has_health)
	{
		__has_health = has_health;
	}
	
	inline void has_max_health(const bool &has_max_health)
	{
		__has_max_health = has_max_health;
	}
	
	inline void has_laser_count(const bool &has_laser_count)
	{
		__has_laser_count = has_laser_count;
	}
	
	inline void has_laser_damage(const bool &has_laser_damage)
	{
		__has_laser_damage = has_laser_damage;
	}
	
	inline void has_laser_range(const bool &has_laser_range)
	{
		__has_laser_range = has_laser_range;
	}
	
	inline void has_laser_max_count(const bool &has_laser_max_count)
	{
		__has_laser_max_count = has_laser_max_count;
	}
	
	inline void has_healing_remaining_time(const bool &has_healing_remaining_time)
	{
		__has_healing_remaining_time = has_healing_remaining_time;
	}
	
	inline void has_time_to_reload(const bool &has_time_to_reload)
	{
		__has_time_to_reload = has_time_to_reload;
	}
	
	inline void has_reload_time(const bool &has_reload_time)
	{
		__has_reload_time = has_reload_time;
	}
	
	inline void has_death_score(const bool &has_death_score)
	{
		__has_death_score = has_death_score;
	}
	

public:

	Medic()
	{
		has_id(false);
		has_side_name(false);
		has_position(false);
		has_radius(false);
		has_max_move_distance(false);
		has_angle(false);
		has_max_turn_angle(false);
		has_max_fire_angle(false);
		has_health(false);
		has_max_health(false);
		has_laser_count(false);
		has_laser_damage(false);
		has_laser_range(false);
		has_laser_max_count(false);
		has_healing_remaining_time(false);
		has_time_to_reload(false);
		has_reload_time(false);
		has_death_score(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Medic";
	}
	
	virtual inline const std::string name() const
	{
		return "Medic";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp17 = __id;
			auto tmp18 = reinterpret_cast<char*>(&tmp17);
			s += std::string(tmp18, sizeof(int));
		}
		
		// serialize side_name
		s += __has_side_name;
		if (__has_side_name)
		{
			std::string tmp19 = "";
			unsigned int tmp21 = __side_name.size();
			auto tmp22 = reinterpret_cast<char*>(&tmp21);
			tmp19 += std::string(tmp22, sizeof(unsigned int));
			while (tmp19.size() && tmp19.back() == 0)
				tmp19.pop_back();
			unsigned char tmp24 = tmp19.size();
			auto tmp25 = reinterpret_cast<char*>(&tmp24);
			s += std::string(tmp25, sizeof(unsigned char));
			s += tmp19;
			
			s += __side_name;
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize radius
		s += __has_radius;
		if (__has_radius)
		{
			float tmp27 = __radius;
			auto tmp28 = reinterpret_cast<char*>(&tmp27);
			s += std::string(tmp28, sizeof(float));
		}
		
		// serialize max_move_distance
		s += __has_max_move_distance;
		if (__has_max_move_distance)
		{
			float tmp30 = __max_move_distance;
			auto tmp31 = reinterpret_cast<char*>(&tmp30);
			s += std::string(tmp31, sizeof(float));
		}
		
		// serialize angle
		s += __has_angle;
		if (__has_angle)
		{
			float tmp33 = __angle;
			auto tmp34 = reinterpret_cast<char*>(&tmp33);
			s += std::string(tmp34, sizeof(float));
		}
		
		// serialize max_turn_angle
		s += __has_max_turn_angle;
		if (__has_max_turn_angle)
		{
			float tmp36 = __max_turn_angle;
			auto tmp37 = reinterpret_cast<char*>(&tmp36);
			s += std::string(tmp37, sizeof(float));
		}
		
		// serialize max_fire_angle
		s += __has_max_fire_angle;
		if (__has_max_fire_angle)
		{
			float tmp39 = __max_fire_angle;
			auto tmp40 = reinterpret_cast<char*>(&tmp39);
			s += std::string(tmp40, sizeof(float));
		}
		
		// serialize health
		s += __has_health;
		if (__has_health)
		{
			int tmp42 = __health;
			auto tmp43 = reinterpret_cast<char*>(&tmp42);
			s += std::string(tmp43, sizeof(int));
		}
		
		// serialize max_health
		s += __has_max_health;
		if (__has_max_health)
		{
			int tmp45 = __max_health;
			auto tmp46 = reinterpret_cast<char*>(&tmp45);
			s += std::string(tmp46, sizeof(int));
		}
		
		// serialize laser_count
		s += __has_laser_count;
		if (__has_laser_count)
		{
			int tmp48 = __laser_count;
			auto tmp49 = reinterpret_cast<char*>(&tmp48);
			s += std::string(tmp49, sizeof(int));
		}
		
		// serialize laser_damage
		s += __has_laser_damage;
		if (__has_laser_damage)
		{
			int tmp51 = __laser_damage;
			auto tmp52 = reinterpret_cast<char*>(&tmp51);
			s += std::string(tmp52, sizeof(int));
		}
		
		// serialize laser_range
		s += __has_laser_range;
		if (__has_laser_range)
		{
			float tmp54 = __laser_range;
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			s += std::string(tmp55, sizeof(float));
		}
		
		// serialize laser_max_count
		s += __has_laser_max_count;
		if (__has_laser_max_count)
		{
			int tmp57 = __laser_max_count;
			auto tmp58 = reinterpret_cast<char*>(&tmp57);
			s += std::string(tmp58, sizeof(int));
		}
		
		// serialize healing_remaining_time
		s += __has_healing_remaining_time;
		if (__has_healing_remaining_time)
		{
			int tmp60 = __healing_remaining_time;
			auto tmp61 = reinterpret_cast<char*>(&tmp60);
			s += std::string(tmp61, sizeof(int));
		}
		
		// serialize time_to_reload
		s += __has_time_to_reload;
		if (__has_time_to_reload)
		{
			int tmp63 = __time_to_reload;
			auto tmp64 = reinterpret_cast<char*>(&tmp63);
			s += std::string(tmp64, sizeof(int));
		}
		
		// serialize reload_time
		s += __has_reload_time;
		if (__has_reload_time)
		{
			int tmp66 = __reload_time;
			auto tmp67 = reinterpret_cast<char*>(&tmp66);
			s += std::string(tmp67, sizeof(int));
		}
		
		// serialize death_score
		s += __has_death_score;
		if (__has_death_score)
		{
			int tmp69 = __death_score;
			auto tmp70 = reinterpret_cast<char*>(&tmp69);
			s += std::string(tmp70, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize side_name
		__has_side_name = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_side_name)
		{
			unsigned char tmp71;
			tmp71 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp72 = std::string(&s[offset], tmp71);
			offset += tmp71;
			while (tmp72.size() < sizeof(unsigned int))
				tmp72 += '\x00';
			unsigned int tmp73;
			tmp73 = *((unsigned int*) (&tmp72[0]));
			
			__side_name = s.substr(offset, tmp73);
			offset += tmp73;
		}
		
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize radius
		__has_radius = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_radius)
		{
			__radius = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize max_move_distance
		__has_max_move_distance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_move_distance)
		{
			__max_move_distance = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize angle
		__has_angle = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_angle)
		{
			__angle = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize max_turn_angle
		__has_max_turn_angle = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_turn_angle)
		{
			__max_turn_angle = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize max_fire_angle
		__has_max_fire_angle = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_fire_angle)
		{
			__max_fire_angle = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize health
		__has_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_health)
		{
			__health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize max_health
		__has_max_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_health)
		{
			__max_health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize laser_count
		__has_laser_count = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_count)
		{
			__laser_count = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize laser_damage
		__has_laser_damage = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_damage)
		{
			__laser_damage = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize laser_range
		__has_laser_range = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_range)
		{
			__laser_range = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize laser_max_count
		__has_laser_max_count = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_laser_max_count)
		{
			__laser_max_count = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize healing_remaining_time
		__has_healing_remaining_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_healing_remaining_time)
		{
			__healing_remaining_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize time_to_reload
		__has_time_to_reload = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_time_to_reload)
		{
			__time_to_reload = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize reload_time
		__has_reload_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_reload_time)
		{
			__reload_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize death_score
		__has_death_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_death_score)
		{
			__death_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Patient : public KSObject
{

protected:

	Position __position;
	float __radius;
	int __healing_duration;
	bool __capturable;
	int __heal_score;

	bool __has_position;
	bool __has_radius;
	bool __has_healing_duration;
	bool __has_capturable;
	bool __has_heal_score;


public: // getters

	inline Position position() const
	{
		return __position;
	}
	
	inline float radius() const
	{
		return __radius;
	}
	
	inline int healing_duration() const
	{
		return __healing_duration;
	}
	
	inline bool capturable() const
	{
		return __capturable;
	}
	
	inline int heal_score() const
	{
		return __heal_score;
	}
	

public: // reference getters

	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline float &ref_radius() const
	{
		return (float&) __radius;
	}
	
	inline int &ref_healing_duration() const
	{
		return (int&) __healing_duration;
	}
	
	inline bool &ref_capturable() const
	{
		return (bool&) __capturable;
	}
	
	inline int &ref_heal_score() const
	{
		return (int&) __heal_score;
	}
	

public: // setters

	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void radius(const float &radius)
	{
		__radius = radius;
		has_radius(true);
	}
	
	inline void healing_duration(const int &healing_duration)
	{
		__healing_duration = healing_duration;
		has_healing_duration(true);
	}
	
	inline void capturable(const bool &capturable)
	{
		__capturable = capturable;
		has_capturable(true);
	}
	
	inline void heal_score(const int &heal_score)
	{
		__heal_score = heal_score;
		has_heal_score(true);
	}
	

public: // has_attribute getters

	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_radius() const
	{
		return __has_radius;
	}
	
	inline bool has_healing_duration() const
	{
		return __has_healing_duration;
	}
	
	inline bool has_capturable() const
	{
		return __has_capturable;
	}
	
	inline bool has_heal_score() const
	{
		return __has_heal_score;
	}
	

public: // has_attribute setters

	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_radius(const bool &has_radius)
	{
		__has_radius = has_radius;
	}
	
	inline void has_healing_duration(const bool &has_healing_duration)
	{
		__has_healing_duration = has_healing_duration;
	}
	
	inline void has_capturable(const bool &has_capturable)
	{
		__has_capturable = has_capturable;
	}
	
	inline void has_heal_score(const bool &has_heal_score)
	{
		__has_heal_score = has_heal_score;
	}
	

public:

	Patient()
	{
		has_position(false);
		has_radius(false);
		has_healing_duration(false);
		has_capturable(false);
		has_heal_score(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Patient";
	}
	
	virtual inline const std::string name() const
	{
		return "Patient";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize radius
		s += __has_radius;
		if (__has_radius)
		{
			float tmp75 = __radius;
			auto tmp76 = reinterpret_cast<char*>(&tmp75);
			s += std::string(tmp76, sizeof(float));
		}
		
		// serialize healing_duration
		s += __has_healing_duration;
		if (__has_healing_duration)
		{
			int tmp78 = __healing_duration;
			auto tmp79 = reinterpret_cast<char*>(&tmp78);
			s += std::string(tmp79, sizeof(int));
		}
		
		// serialize capturable
		s += __has_capturable;
		if (__has_capturable)
		{
			bool tmp81 = __capturable;
			auto tmp82 = reinterpret_cast<char*>(&tmp81);
			s += std::string(tmp82, sizeof(bool));
		}
		
		// serialize heal_score
		s += __has_heal_score;
		if (__has_heal_score)
		{
			int tmp84 = __heal_score;
			auto tmp85 = reinterpret_cast<char*>(&tmp84);
			s += std::string(tmp85, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize radius
		__has_radius = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_radius)
		{
			__radius = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize healing_duration
		__has_healing_duration = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_healing_duration)
		{
			__healing_duration = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize capturable
		__has_capturable = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_capturable)
		{
			__capturable = *((bool*) (&s[offset]));
			offset += sizeof(bool);
		}
		
		// deserialize heal_score
		__has_heal_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_heal_score)
		{
			__heal_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Wall : public KSObject
{

protected:

	Position __start_pos;
	Position __end_pos;

	bool __has_start_pos;
	bool __has_end_pos;


public: // getters

	inline Position start_pos() const
	{
		return __start_pos;
	}
	
	inline Position end_pos() const
	{
		return __end_pos;
	}
	

public: // reference getters

	inline Position &ref_start_pos() const
	{
		return (Position&) __start_pos;
	}
	
	inline Position &ref_end_pos() const
	{
		return (Position&) __end_pos;
	}
	

public: // setters

	inline void start_pos(const Position &start_pos)
	{
		__start_pos = start_pos;
		has_start_pos(true);
	}
	
	inline void end_pos(const Position &end_pos)
	{
		__end_pos = end_pos;
		has_end_pos(true);
	}
	

public: // has_attribute getters

	inline bool has_start_pos() const
	{
		return __has_start_pos;
	}
	
	inline bool has_end_pos() const
	{
		return __has_end_pos;
	}
	

public: // has_attribute setters

	inline void has_start_pos(const bool &has_start_pos)
	{
		__has_start_pos = has_start_pos;
	}
	
	inline void has_end_pos(const bool &has_end_pos)
	{
		__has_end_pos = has_end_pos;
	}
	

public:

	Wall()
	{
		has_start_pos(false);
		has_end_pos(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Wall";
	}
	
	virtual inline const std::string name() const
	{
		return "Wall";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize start_pos
		s += __has_start_pos;
		if (__has_start_pos)
		{
			s += __start_pos.serialize();
		}
		
		// serialize end_pos
		s += __has_end_pos;
		if (__has_end_pos)
		{
			s += __end_pos.serialize();
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize start_pos
		__has_start_pos = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_start_pos)
		{
			offset = __start_pos.deserialize(s, offset);
		}
		
		// deserialize end_pos
		__has_end_pos = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_end_pos)
		{
			offset = __end_pos.deserialize(s, offset);
		}
		
		return offset;
	}
};


class World : public KSObject
{

protected:

	float __width;
	float __height;
	std::map<std::string, int> __scores;
	std::map<std::string, std::vector<Medic>> __medics;
	std::vector<Wall> __walls;
	std::vector<Patient> __patients;
	std::vector<PowerUp> __powerups;

	bool __has_width;
	bool __has_height;
	bool __has_scores;
	bool __has_medics;
	bool __has_walls;
	bool __has_patients;
	bool __has_powerups;


public: // getters

	inline float width() const
	{
		return __width;
	}
	
	inline float height() const
	{
		return __height;
	}
	
	inline std::map<std::string, int> scores() const
	{
		return __scores;
	}
	
	inline std::map<std::string, std::vector<Medic>> medics() const
	{
		return __medics;
	}
	
	inline std::vector<Wall> walls() const
	{
		return __walls;
	}
	
	inline std::vector<Patient> patients() const
	{
		return __patients;
	}
	
	inline std::vector<PowerUp> powerups() const
	{
		return __powerups;
	}
	

public: // reference getters

	inline float &ref_width() const
	{
		return (float&) __width;
	}
	
	inline float &ref_height() const
	{
		return (float&) __height;
	}
	
	inline std::map<std::string, int> &ref_scores() const
	{
		return (std::map<std::string, int>&) __scores;
	}
	
	inline std::map<std::string, std::vector<Medic>> &ref_medics() const
	{
		return (std::map<std::string, std::vector<Medic>>&) __medics;
	}
	
	inline std::vector<Wall> &ref_walls() const
	{
		return (std::vector<Wall>&) __walls;
	}
	
	inline std::vector<Patient> &ref_patients() const
	{
		return (std::vector<Patient>&) __patients;
	}
	
	inline std::vector<PowerUp> &ref_powerups() const
	{
		return (std::vector<PowerUp>&) __powerups;
	}
	

public: // setters

	inline void width(const float &width)
	{
		__width = width;
		has_width(true);
	}
	
	inline void height(const float &height)
	{
		__height = height;
		has_height(true);
	}
	
	inline void scores(const std::map<std::string, int> &scores)
	{
		__scores = scores;
		has_scores(true);
	}
	
	inline void medics(const std::map<std::string, std::vector<Medic>> &medics)
	{
		__medics = medics;
		has_medics(true);
	}
	
	inline void walls(const std::vector<Wall> &walls)
	{
		__walls = walls;
		has_walls(true);
	}
	
	inline void patients(const std::vector<Patient> &patients)
	{
		__patients = patients;
		has_patients(true);
	}
	
	inline void powerups(const std::vector<PowerUp> &powerups)
	{
		__powerups = powerups;
		has_powerups(true);
	}
	

public: // has_attribute getters

	inline bool has_width() const
	{
		return __has_width;
	}
	
	inline bool has_height() const
	{
		return __has_height;
	}
	
	inline bool has_scores() const
	{
		return __has_scores;
	}
	
	inline bool has_medics() const
	{
		return __has_medics;
	}
	
	inline bool has_walls() const
	{
		return __has_walls;
	}
	
	inline bool has_patients() const
	{
		return __has_patients;
	}
	
	inline bool has_powerups() const
	{
		return __has_powerups;
	}
	

public: // has_attribute setters

	inline void has_width(const bool &has_width)
	{
		__has_width = has_width;
	}
	
	inline void has_height(const bool &has_height)
	{
		__has_height = has_height;
	}
	
	inline void has_scores(const bool &has_scores)
	{
		__has_scores = has_scores;
	}
	
	inline void has_medics(const bool &has_medics)
	{
		__has_medics = has_medics;
	}
	
	inline void has_walls(const bool &has_walls)
	{
		__has_walls = has_walls;
	}
	
	inline void has_patients(const bool &has_patients)
	{
		__has_patients = has_patients;
	}
	
	inline void has_powerups(const bool &has_powerups)
	{
		__has_powerups = has_powerups;
	}
	

public:

	World()
	{
		has_width(false);
		has_height(false);
		has_scores(false);
		has_medics(false);
		has_walls(false);
		has_patients(false);
		has_powerups(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "World";
	}
	
	virtual inline const std::string name() const
	{
		return "World";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize width
		s += __has_width;
		if (__has_width)
		{
			float tmp87 = __width;
			auto tmp88 = reinterpret_cast<char*>(&tmp87);
			s += std::string(tmp88, sizeof(float));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			float tmp90 = __height;
			auto tmp91 = reinterpret_cast<char*>(&tmp90);
			s += std::string(tmp91, sizeof(float));
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp92 = "";
			unsigned int tmp94 = __scores.size();
			auto tmp95 = reinterpret_cast<char*>(&tmp94);
			tmp92 += std::string(tmp95, sizeof(unsigned int));
			while (tmp92.size() && tmp92.back() == 0)
				tmp92.pop_back();
			unsigned char tmp97 = tmp92.size();
			auto tmp98 = reinterpret_cast<char*>(&tmp97);
			s += std::string(tmp98, sizeof(unsigned char));
			s += tmp92;
			
			for (auto &tmp99 : __scores)
			{
				s += '\x01';
				std::string tmp100 = "";
				unsigned int tmp102 = tmp99.first.size();
				auto tmp103 = reinterpret_cast<char*>(&tmp102);
				tmp100 += std::string(tmp103, sizeof(unsigned int));
				while (tmp100.size() && tmp100.back() == 0)
					tmp100.pop_back();
				unsigned char tmp105 = tmp100.size();
				auto tmp106 = reinterpret_cast<char*>(&tmp105);
				s += std::string(tmp106, sizeof(unsigned char));
				s += tmp100;
				
				s += tmp99.first;
				
				s += '\x01';
				int tmp108 = tmp99.second;
				auto tmp109 = reinterpret_cast<char*>(&tmp108);
				s += std::string(tmp109, sizeof(int));
			}
		}
		
		// serialize medics
		s += __has_medics;
		if (__has_medics)
		{
			std::string tmp110 = "";
			unsigned int tmp112 = __medics.size();
			auto tmp113 = reinterpret_cast<char*>(&tmp112);
			tmp110 += std::string(tmp113, sizeof(unsigned int));
			while (tmp110.size() && tmp110.back() == 0)
				tmp110.pop_back();
			unsigned char tmp115 = tmp110.size();
			auto tmp116 = reinterpret_cast<char*>(&tmp115);
			s += std::string(tmp116, sizeof(unsigned char));
			s += tmp110;
			
			for (auto &tmp117 : __medics)
			{
				s += '\x01';
				std::string tmp118 = "";
				unsigned int tmp120 = tmp117.first.size();
				auto tmp121 = reinterpret_cast<char*>(&tmp120);
				tmp118 += std::string(tmp121, sizeof(unsigned int));
				while (tmp118.size() && tmp118.back() == 0)
					tmp118.pop_back();
				unsigned char tmp123 = tmp118.size();
				auto tmp124 = reinterpret_cast<char*>(&tmp123);
				s += std::string(tmp124, sizeof(unsigned char));
				s += tmp118;
				
				s += tmp117.first;
				
				s += '\x01';
				std::string tmp125 = "";
				unsigned int tmp127 = tmp117.second.size();
				auto tmp128 = reinterpret_cast<char*>(&tmp127);
				tmp125 += std::string(tmp128, sizeof(unsigned int));
				while (tmp125.size() && tmp125.back() == 0)
					tmp125.pop_back();
				unsigned char tmp130 = tmp125.size();
				auto tmp131 = reinterpret_cast<char*>(&tmp130);
				s += std::string(tmp131, sizeof(unsigned char));
				s += tmp125;
				
				for (auto &tmp132 : tmp117.second)
				{
					s += '\x01';
					s += tmp132.serialize();
				}
			}
		}
		
		// serialize walls
		s += __has_walls;
		if (__has_walls)
		{
			std::string tmp133 = "";
			unsigned int tmp135 = __walls.size();
			auto tmp136 = reinterpret_cast<char*>(&tmp135);
			tmp133 += std::string(tmp136, sizeof(unsigned int));
			while (tmp133.size() && tmp133.back() == 0)
				tmp133.pop_back();
			unsigned char tmp138 = tmp133.size();
			auto tmp139 = reinterpret_cast<char*>(&tmp138);
			s += std::string(tmp139, sizeof(unsigned char));
			s += tmp133;
			
			for (auto &tmp140 : __walls)
			{
				s += '\x01';
				s += tmp140.serialize();
			}
		}
		
		// serialize patients
		s += __has_patients;
		if (__has_patients)
		{
			std::string tmp141 = "";
			unsigned int tmp143 = __patients.size();
			auto tmp144 = reinterpret_cast<char*>(&tmp143);
			tmp141 += std::string(tmp144, sizeof(unsigned int));
			while (tmp141.size() && tmp141.back() == 0)
				tmp141.pop_back();
			unsigned char tmp146 = tmp141.size();
			auto tmp147 = reinterpret_cast<char*>(&tmp146);
			s += std::string(tmp147, sizeof(unsigned char));
			s += tmp141;
			
			for (auto &tmp148 : __patients)
			{
				s += '\x01';
				s += tmp148.serialize();
			}
		}
		
		// serialize powerups
		s += __has_powerups;
		if (__has_powerups)
		{
			std::string tmp149 = "";
			unsigned int tmp151 = __powerups.size();
			auto tmp152 = reinterpret_cast<char*>(&tmp151);
			tmp149 += std::string(tmp152, sizeof(unsigned int));
			while (tmp149.size() && tmp149.back() == 0)
				tmp149.pop_back();
			unsigned char tmp154 = tmp149.size();
			auto tmp155 = reinterpret_cast<char*>(&tmp154);
			s += std::string(tmp155, sizeof(unsigned char));
			s += tmp149;
			
			for (auto &tmp156 : __powerups)
			{
				s += '\x01';
				s += tmp156.serialize();
			}
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize width
		__has_width = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_width)
		{
			__width = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize height
		__has_height = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_height)
		{
			__height = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp157;
			tmp157 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp158 = std::string(&s[offset], tmp157);
			offset += tmp157;
			while (tmp158.size() < sizeof(unsigned int))
				tmp158 += '\x00';
			unsigned int tmp159;
			tmp159 = *((unsigned int*) (&tmp158[0]));
			
			__scores.clear();
			for (unsigned int tmp160 = 0; tmp160 < tmp159; tmp160++)
			{
				std::string tmp161;
				offset++;
				unsigned char tmp163;
				tmp163 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp164 = std::string(&s[offset], tmp163);
				offset += tmp163;
				while (tmp164.size() < sizeof(unsigned int))
					tmp164 += '\x00';
				unsigned int tmp165;
				tmp165 = *((unsigned int*) (&tmp164[0]));
				
				tmp161 = s.substr(offset, tmp165);
				offset += tmp165;
				
				int tmp162;
				offset++;
				tmp162 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__scores[tmp161] = tmp162;
			}
		}
		
		// deserialize medics
		__has_medics = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_medics)
		{
			unsigned char tmp166;
			tmp166 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp167 = std::string(&s[offset], tmp166);
			offset += tmp166;
			while (tmp167.size() < sizeof(unsigned int))
				tmp167 += '\x00';
			unsigned int tmp168;
			tmp168 = *((unsigned int*) (&tmp167[0]));
			
			__medics.clear();
			for (unsigned int tmp169 = 0; tmp169 < tmp168; tmp169++)
			{
				std::string tmp170;
				offset++;
				unsigned char tmp172;
				tmp172 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp173 = std::string(&s[offset], tmp172);
				offset += tmp172;
				while (tmp173.size() < sizeof(unsigned int))
					tmp173 += '\x00';
				unsigned int tmp174;
				tmp174 = *((unsigned int*) (&tmp173[0]));
				
				tmp170 = s.substr(offset, tmp174);
				offset += tmp174;
				
				std::vector<Medic> tmp171;
				offset++;
				unsigned char tmp175;
				tmp175 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp176 = std::string(&s[offset], tmp175);
				offset += tmp175;
				while (tmp176.size() < sizeof(unsigned int))
					tmp176 += '\x00';
				unsigned int tmp177;
				tmp177 = *((unsigned int*) (&tmp176[0]));
				
				tmp171.clear();
				for (unsigned int tmp178 = 0; tmp178 < tmp177; tmp178++)
				{
					Medic tmp179;
					offset++;
					offset = tmp179.deserialize(s, offset);
					tmp171.push_back(tmp179);
				}
				
				__medics[tmp170] = tmp171;
			}
		}
		
		// deserialize walls
		__has_walls = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_walls)
		{
			unsigned char tmp180;
			tmp180 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp181 = std::string(&s[offset], tmp180);
			offset += tmp180;
			while (tmp181.size() < sizeof(unsigned int))
				tmp181 += '\x00';
			unsigned int tmp182;
			tmp182 = *((unsigned int*) (&tmp181[0]));
			
			__walls.clear();
			for (unsigned int tmp183 = 0; tmp183 < tmp182; tmp183++)
			{
				Wall tmp184;
				offset++;
				offset = tmp184.deserialize(s, offset);
				__walls.push_back(tmp184);
			}
		}
		
		// deserialize patients
		__has_patients = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_patients)
		{
			unsigned char tmp185;
			tmp185 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp186 = std::string(&s[offset], tmp185);
			offset += tmp185;
			while (tmp186.size() < sizeof(unsigned int))
				tmp186 += '\x00';
			unsigned int tmp187;
			tmp187 = *((unsigned int*) (&tmp186[0]));
			
			__patients.clear();
			for (unsigned int tmp188 = 0; tmp188 < tmp187; tmp188++)
			{
				Patient tmp189;
				offset++;
				offset = tmp189.deserialize(s, offset);
				__patients.push_back(tmp189);
			}
		}
		
		// deserialize powerups
		__has_powerups = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_powerups)
		{
			unsigned char tmp190;
			tmp190 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp191 = std::string(&s[offset], tmp190);
			offset += tmp190;
			while (tmp191.size() < sizeof(unsigned int))
				tmp191 += '\x00';
			unsigned int tmp192;
			tmp192 = *((unsigned int*) (&tmp191[0]));
			
			__powerups.clear();
			for (unsigned int tmp193 = 0; tmp193 < tmp192; tmp193++)
			{
				PowerUp tmp194;
				offset++;
				offset = tmp194.deserialize(s, offset);
				__powerups.push_back(tmp194);
			}
		}
		
		return offset;
	}
};

} // namespace models

} // namespace ks

#endif // _KS_MODELS_H_
