#ifndef _KS_COMMANDS_H_
#define _KS_COMMANDS_H_

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


namespace commands
{

class Move : public KSObject
{

protected:

	int __id;
	float __distance;

	bool __has_id;
	bool __has_distance;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline float distance() const
	{
		return __distance;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline float &ref_distance() const
	{
		return (float&) __distance;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void distance(const float &distance)
	{
		__distance = distance;
		has_distance(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_distance() const
	{
		return __has_distance;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_distance(const bool &has_distance)
	{
		__has_distance = has_distance;
	}
	

public:

	Move()
	{
		has_id(false);
		has_distance(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Move";
	}
	
	virtual inline const std::string name() const
	{
		return "Move";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp1 = __id;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize distance
		s += __has_distance;
		if (__has_distance)
		{
			float tmp4 = __distance;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(float));
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
		
		// deserialize distance
		__has_distance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_distance)
		{
			__distance = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		return offset;
	}
};


class Turn : public KSObject
{

protected:

	int __id;
	bool __clockwise;
	float __angle;

	bool __has_id;
	bool __has_clockwise;
	bool __has_angle;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline bool clockwise() const
	{
		return __clockwise;
	}
	
	inline float angle() const
	{
		return __angle;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline bool &ref_clockwise() const
	{
		return (bool&) __clockwise;
	}
	
	inline float &ref_angle() const
	{
		return (float&) __angle;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void clockwise(const bool &clockwise)
	{
		__clockwise = clockwise;
		has_clockwise(true);
	}
	
	inline void angle(const float &angle)
	{
		__angle = angle;
		has_angle(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_clockwise() const
	{
		return __has_clockwise;
	}
	
	inline bool has_angle() const
	{
		return __has_angle;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_clockwise(const bool &has_clockwise)
	{
		__has_clockwise = has_clockwise;
	}
	
	inline void has_angle(const bool &has_angle)
	{
		__has_angle = has_angle;
	}
	

public:

	Turn()
	{
		has_id(false);
		has_clockwise(false);
		has_angle(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Turn";
	}
	
	virtual inline const std::string name() const
	{
		return "Turn";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp7 = __id;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(int));
		}
		
		// serialize clockwise
		s += __has_clockwise;
		if (__has_clockwise)
		{
			bool tmp10 = __clockwise;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(bool));
		}
		
		// serialize angle
		s += __has_angle;
		if (__has_angle)
		{
			float tmp13 = __angle;
			auto tmp14 = reinterpret_cast<char*>(&tmp13);
			s += std::string(tmp14, sizeof(float));
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
		
		// deserialize clockwise
		__has_clockwise = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_clockwise)
		{
			__clockwise = *((bool*) (&s[offset]));
			offset += sizeof(bool);
		}
		
		// deserialize angle
		__has_angle = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_angle)
		{
			__angle = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		return offset;
	}
};


class Fire : public KSObject
{

protected:

	int __id;
	float __angle;

	bool __has_id;
	bool __has_angle;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline float angle() const
	{
		return __angle;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline float &ref_angle() const
	{
		return (float&) __angle;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void angle(const float &angle)
	{
		__angle = angle;
		has_angle(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_angle() const
	{
		return __has_angle;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_angle(const bool &has_angle)
	{
		__has_angle = has_angle;
	}
	

public:

	Fire()
	{
		has_id(false);
		has_angle(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Fire";
	}
	
	virtual inline const std::string name() const
	{
		return "Fire";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp16 = __id;
			auto tmp17 = reinterpret_cast<char*>(&tmp16);
			s += std::string(tmp17, sizeof(int));
		}
		
		// serialize angle
		s += __has_angle;
		if (__has_angle)
		{
			float tmp19 = __angle;
			auto tmp20 = reinterpret_cast<char*>(&tmp19);
			s += std::string(tmp20, sizeof(float));
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
		
		// deserialize angle
		__has_angle = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_angle)
		{
			__angle = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		return offset;
	}
};

} // namespace commands

} // namespace ks

#endif // _KS_COMMANDS_H_
