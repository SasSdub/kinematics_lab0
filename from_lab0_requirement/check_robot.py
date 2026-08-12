import sys
import time
from pathlib import Path

try:
    import numpy as np
    from roboticstoolbox import Robot
    import swift
except Exception as e:
    print("[FAIL] import error:", e)
    print('Fix:  pip install "numpy<2" "roboticstoolbox-python[swift]"')
    sys.exit(1)

HERE = Path(__file__).resolve().parent

if not (HERE / "my_robot" / "robot.urdf").exists():
    print("[FAIL] my_robot/robot.urdf not found - put your exported URDF there")
    sys.exit(1)

links, name, _, _ = Robot.URDF_read("my_robot/robot.urdf", tld=HERE.as_posix())
robot = Robot(links, name=name)
print(f"[ok] loaded '{name}'  ({robot.n} joints)")

missing = [g.filename for link in robot.links for g in link.geometry
           if getattr(g, "filename", None) and not Path(g.filename).exists()]
if missing:
    print("[FAIL] these mesh files were not found - fix the paths or add the files:")
    for m in missing:
        print("   ", m)
    sys.exit(1)
print("[ok] all mesh files found")

env = swift.Swift()
env.launch(realtime=True)
env.add(robot)
print("[ok] your robot is shown in the browser - closing in 5s")
time.sleep(5)
env.close()
