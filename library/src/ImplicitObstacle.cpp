#include "ImplicitObstacle.h"

ImplicitObstacle::ImplicitObstacle()
{

}

ImplicitObstacle::~ImplicitObstacle()
{

}

void ImplicitObstacle::init(const ObstacleParameters& initParams)
{
	_position = initParams.position;
	_xw = initParams.xw;
	_yw = initParams.yw;
}