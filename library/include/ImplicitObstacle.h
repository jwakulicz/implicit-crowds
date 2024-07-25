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
	Vector2D position() { return _position; }


protected:
	// the position of the box
	Vector2D _position;
	// the x width of the box
	double _xw;
	// the y width of the box
	double _yw;
	// id of the obstacle
	int _id;
	// group id
	int _gid;
};