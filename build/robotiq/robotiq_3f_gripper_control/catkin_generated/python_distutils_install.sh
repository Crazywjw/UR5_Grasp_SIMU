#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_3f_gripper_control"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/jerry/ros_projects/Study/ur5_robot/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/jerry/ros_projects/Study/ur5_robot/install/lib/python3/dist-packages:/home/jerry/ros_projects/Study/ur5_robot/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/jerry/ros_projects/Study/ur5_robot/build" \
    "/usr/bin/python3" \
    "/home/jerry/ros_projects/Study/ur5_robot/src/robotiq/robotiq_3f_gripper_control/setup.py" \
     \
    build --build-base "/home/jerry/ros_projects/Study/ur5_robot/build/robotiq/robotiq_3f_gripper_control" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/jerry/ros_projects/Study/ur5_robot/install" --install-scripts="/home/jerry/ros_projects/Study/ur5_robot/install/bin"
