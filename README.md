# FRA371 Kinematic Lab 0 - Installation Check & Robot Setup

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Robotics Toolbox](https://img.shields.io/badge/Robotics%20Toolbox-1.3.1-success)
![NumPy](https://img.shields.io/badge/NumPy-2.5.1-blue)
![Platform](https://img.shields.io/badge/OS-Windows-informational)

## Installation Check

Run this once before the lab to confirm the Robotics Toolbox for Python is installed
and the 3D viewer works.

### 0. Prerequisite

Python 3.10 or newer. Check with:

```
python --version
```

### 1. Install
Tested on RTB 1.3.1 / numpy 2.5.1

```
pip install -r requirements.txt
```

### 2. Run the verification script
If you use Ubuntu, run:
```
python verify_install.py
```

If you use Window, run:
```
python swift_windows_fix.py
python verify_install.py
```

### 3. What you should see

- Three `[ok]` lines printed in the terminal.
- A browser tab opens with a **robot arm that moves** for a 20 seconds, then closes.
- A final line: `[done] ... RTB is installed correctly`.

If you see the arm move, you are successfully installed.

## Robot Setup

After the installation check passes, add your own robot to this project and confirm it loads.

### 1. Move your robot into `my_robot/`

Your robot comes from a **URDF exporter** (your CAD tool): one `.urdf` file and a set
of `.stl` meshes.

1. Put your mesh files in `my_robot/meshes/`.
2. Save your URDF as `my_robot/robot.urdf`.

### 2. Re-path the meshes

In `my_robot/robot.urdf`, every mesh path **must** look like this:

```xml
<mesh filename="package://my_robot/meshes/YOUR_FILE.stl"/>
```

### 3. Check your robot

```
python check_robot.py
```

What you should see:

- `[ok] loaded ...` and `[ok] all mesh files found`
- a browser tab showing **your robot**, then it closes.

If a mesh is missing, the script lists the file - fix the path or add the file, then run
it again.


### If you have the error of Numpy 