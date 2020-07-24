---
layout: post
title: Setting up Nimbro
excerpt: "Steps followed to bring Nimbro OP2X platform"
categories: nimbro
tags: [ study nimbro ]
modified: 2018-09-02T14:11:53-04:00
---

* Table of Contents
{:toc}

## Install Using Docker
Prerequisites : Install docker .
  1. From Existing binary

    docker run --name nimbro -it sachinsshetty/nimbro:latest /bin/bash

  2. Build docker image from DockerFile

    a. cd src

    b. docker build
---



---
## Install in RaspberryPi (UnderDevelopment)

---
## Install in Linux


1. Download Ubuntu 14.04 LTS
2. Kernel- Xenial Xerius -

    ```sudo apt-get install linux-generic-lts-xenial
    ```
3. ROS Indigo

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

sudo apt-get update

sudo apt-get install ros-indigo-desktop-full

sudo rosdep init

rosdep update

sudo apt-get install ros-indigo-rqt-rviz

sudo apt-get install ros-indigo-joy

```
4. The QGLViewer library:

    ```sudo apt-get install libqglviewer-dev
    ```
5. GNU Scientific Library (GSL):

    ```sudo apt-get install libgsl0-dev
    ```
6. Controllers for Gazebo
      ```
      sudo apt-get install ros-indigo-gazebo-ros-control
      sudo apt-get install ros-indigo-ros-controllers
      sudo apt-get install ros-indigo-controller-manager
      sudo apt-get install ros-indigo-rqt-controller-manager
      ```
7. Vision packages
      ```
      sudo apt-get install v4l-utils v4l2ucp v4l-conf
      sudo add-apt-repository ppa:pj-assis/ppa
      sudo apt-get update
      sudo apt-get install guvcview
      ```
8. Python deps
```
      sudo apt-get install sshpass
      sudo apt-get install python-pip python-dev build-essential
      sudo pip install --upgrade pip
      sudo pip install --upgrade virtualenv
    ## Failed   sudo pip install --upgrade --no-deps --force-reinstall pexpect
      sudo pip install termcolor
```      
9. ncurses Library:

      ```sudo apt-get install libncurses5-dev
      ```
10. x264 Library:

      ```sudo apt-get install libx264-dev
      ```
11. GCC ARM Compiler:

      ```sudo apt-get install gcc-arm-none-eabi
      ```
12. Doxygen Documentation System:

      ```sudo apt-get install doxygen
      ```

13. Utilities (optional, choose relevant ones):
      ```
      sudo apt-get install curl tshark ssh screen
      sudo apt-get install git git-gui gitk qgit
      sudo apt-get install joe vim nano kwrite kdiff3 colordiff kompare
      sudo apt-get install gdb valgrind tree htop
      ```


Additional installs for errors : during "nimbro make". Raised a github issue to fix the error.
### TODO
  create a pull request to generate the docs from doxygen.

```
sudo apt-get install libcholmod2.1.2 libsuitesparse-metis-dev
sudo apt-get install ros-indigo-libg2o
```
### Installation

Place the following into your .bashrc:
```
source /opt/ros/indigo/setup.bash
source ~/NimbRo-OP/src/nimbro/scripts/env.sh # Or alternate path
export NIMBRO_ROBOT_TYPE=P1
export NIMBRO_ROBOT_NAME=xs0
export NIMBRO_ROBOT_VARIANT=nimbro_op_hull
```

Clone repository

```
git clone https://github.com/AIS-Bonn/humanoid_op_ros ~/NimbRo-OP
```

System setup

The robotcontrol node needs realtime permissions to run reliably. Create a file
 /etc/security/limits.d/nimbro.conf  
with contents (replace USER with your username):
```
*    hard rtprio 0
*    soft rtprio 0
USER hard rtprio 20
USER soft rtprio 20
```

You will need to log out and in again to load the security settings. Alternatively, you can use the following to emulate the login:
```
sudo -i -u user
```
  //### failed as : -bash: /home/sachin/NimbRo-OP/devel/setup.bash: No such file or directory


If you want to set up udev rules for devices you want to use, then refer to:
```
src/nimbro/scripts/set_camera.py

src/nimbro/scripts/set_cm7X0.py
```
For installation and deployment of the required files to the robots, a special installation folder is required:
```
sudo mkdir -p /nimbro

sudo chown $USER /nimbro
```
---------


Simulation is failing on VMbox, need to check for solutions .
### Simulation
http://nimbro.net/OP/Doc/html/simulation.html
```
roslaunch nimbro_op_gazebo nimbro_op.launch   
```
###### starts gazebo, creates the world and spawns the robot.
```
roslaunch launch gazebo_robot_standing_cap.launch   
```
###### starts the robotcontrol node and connects to the virtual robot.


#### Additonal Steps followed to make gazebo running
following steps from
```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -

sudo apt-get update

sudo apt-get install libsdformat1 libsdformat-dev

sudo apt-get install libsdformat-dev

sudo apt-get install gazebo2

sudo apt-get install ros-indigo-gazebo-ros

sudo apt-get install ros-indigo-gazebo-ros-pkgs ros-indigo-gazebo-ros-control
```



###### If gazebo fails in VM, then execute below command and execute gazebo.
```echo "export SVGA_VGPU10=0" >> ~/.bashrc
```

Links

a. [Nimbro Installation](http://nimbro.net/OP/Doc/html/installation.html) online docs

b. [StepFiles](https://github.com/igusGmbH/HumanoidOpenPlatform/tree/master/STEP_Files)

c. [nimbroOp](https://github.com/NimbRo/nimbro-op2)

d. [ROS-Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu)

e. [gazebo 2.2](http://gazebosim.org/tutorials?tut=install&ver=2.2)

f. [VMError](http://answers.gazebosim.org/question/13214/virtual-machine-not-launching-gazebo/)

g. [gazeboinstall](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install()
