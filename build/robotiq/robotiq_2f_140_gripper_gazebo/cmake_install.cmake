# Install script for directory: /home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_2f_140_gripper_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jerry/ros_projects/Study/ur5_robot/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jerry/ros_projects/Study/ur5_robot/build/robotiq/robotiq_2f_140_gripper_gazebo/catkin_generated/installspace/robotiq_2f_140_gripper_gazebo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotiq_2f_140_gripper_gazebo/cmake" TYPE FILE FILES
    "/home/jerry/ros_projects/Study/ur5_robot/build/robotiq/robotiq_2f_140_gripper_gazebo/catkin_generated/installspace/robotiq_2f_140_gripper_gazeboConfig.cmake"
    "/home/jerry/ros_projects/Study/ur5_robot/build/robotiq/robotiq_2f_140_gripper_gazebo/catkin_generated/installspace/robotiq_2f_140_gripper_gazeboConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotiq_2f_140_gripper_gazebo" TYPE FILE FILES "/home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_2f_140_gripper_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robotiq_2f_140_gripper_gazebo" TYPE DIRECTORY FILES
    "/home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_2f_140_gripper_gazebo/config"
    "/home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_2f_140_gripper_gazebo/launch"
    "/home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_2f_140_gripper_gazebo/urdf"
    )
endif()

