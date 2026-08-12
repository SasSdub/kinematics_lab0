"""
FRA371 Kinematic Labs - Installation Check
Run:  python verify_install.py
If a robot arm opens in your browser and moves, your setup is correct.
"""

import sys
import time

try:
    import numpy as np
    import roboticstoolbox as rtb
    import swift
except Exception as e:
    print("[FAIL] import error:", e)
    print("Fix:  pip install -r requirements.txt")
    sys.exit(1)

print(f"[ok] roboticstoolbox {rtb.__version__}  /  numpy {np.__version__}")

robot = rtb.models.Panda()                 # sample robot bundled with RTB
print(f"[ok] loaded sample robot '{robot.name}'  ({robot.n} joints)")

env = swift.Swift()
env.launch(realtime=True)
env.add(robot)
print("[ok] Swift open in browser - the arm should now be moving")

q0 = robot.qr
t = 0.0
for _ in range(400):
    t += 0.05
    robot.q = q0 + 0.3 * np.sin(t + np.arange(robot.n))
    env.step(0.05)

print("[done] if you saw the arm move, RTB is installed correctly - closing in 3s")
time.sleep(3)
env.close()