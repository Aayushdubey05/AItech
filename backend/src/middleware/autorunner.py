import time
import subprocess
import os
count = 0
def run_scripts():
    pid = str(os.getpid())
    with open("service.pid","w") as f:
        f.write(pid)
    print(f"Systems Pid : {pid}")

    while True:
        try:
            print("Running the linkedinjobs.py")
            subprocess.run(['python','linkedinjobs.py'])
            print(f"Successfully excuted the scripts {count+1} time")
        except subprocess.CalledProcessError as e:
            print(f"Error while running the scripts: {e}")
        except Exception as e:
            print(f"Error: {e}")
        

        time.sleep(24*3600)



