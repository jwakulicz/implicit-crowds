#pragma once
#include <Eigen/Dense>
using namespace Eigen;
typedef Eigen::Matrix<double, 2, 1, Eigen::DontAlign> Vector2D; // do this to avoid alignment issues

/**
  * @brief The parameters for a single obstacle.
  */
struct ObstacleParameters {
	Vector2D position;
	double xw;
	double yw;
	int gid;
};

