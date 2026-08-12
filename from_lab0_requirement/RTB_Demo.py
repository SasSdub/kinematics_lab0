import time
import sys
from pathlib import Path

try:
    import numpy as np
    from roboticstoolbox import Robot
    import swift
except Exception as e:
    print("[FAIL] import error:", e)
    sys.exit(1)

HERE = Path(__file__).resolve().parent

if not (HERE / "my_robot" / "robot.urdf").exists():
    print("[FAIL] my_robot/robot.urdf not found")
    sys.exit(1)

links, name, _, _ = Robot.URDF_read("my_robot/robot.urdf", tld=HERE.as_posix())
robot = Robot(links, name=name)

env = swift.Swift()
try:
    env.launch(realtime=True)
    env.add(robot)
    print("[ok] Swift is open. Press Ctrl+C to close it.")

    while True:
        time.sleep(1)
        q = robot.q
        T = robot.fkine(q)
        print(T)
except KeyboardInterrupt:
    print("\n[ok] closing Swift")
finally:
    env.close()

