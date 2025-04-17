# slam-project

to run the ORB SLAM node:

ros2 run orbslam3 mono /home/pepper_nano/colcon_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt /home/pepper_nano/colcon_ws/src/orbslam3_ros2/config/monocular/RealSense_D435i.yaml


to run the data publishing node:


ros2 run aims_slam data_pub
