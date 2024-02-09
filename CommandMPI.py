import subprocess
import time

for n in [1, 2, 4, 8]:
    now = time.time()
    subprocess.run(["mpiexec",  "-n", str(n), "python3", "task.py"], text=True, capture_output=True)
    print(f"Running task with {n} nodes completed in {round(time.time()-now,3)} secs")