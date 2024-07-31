#pragma once
#include "ObstacleParameters.h"

class ImplicitObstacle {
public:
	ImplicitObstacle();
	~ImplicitObstacle(); //destructor
	void init(const ObstacleParameters&); //function cannot modify these arguments
	
	// returns true
	bool isObstacle() { return true; }
	// returns the position of the obstacle
	Vector2D position() const { return _position; }
	// return x width of the obstacle
	float xw() const { return _xw; }
	// return y width of the obstacle
	float yw() const { return _yw; }
	// return the global id
	int getGlobalId() const { return _gid; }


protected:
	// the position of the box
	Vector2D _position;
	// the x width of the box
	float _xw;
	// the y width of the box
	float _yw;
	// id of the obstacle
	int _id;
	// group id
	int _gid;
};