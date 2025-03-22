import time
import subprocess
import os
import atexit
def run_scripts():
    pid = str(os.getpid())
    with open("service.pid","w") as f:
        f.write(pid)
    print(f"Systems Pid : {pid}")

    def cleanup():
        if os.path.exists("service.pid"):
            os.remove("service.pid")
            print("PID file removed.")
    atexit.register(cleanup)

    count = 0
    while True:
        try:
            print("Running the linkedinjobs.py")
            #I will only run this ... when we got high resource .. for MVP .. we made it bro 

            #subprocess.run([r'C:/Users/aayus/Developer_session/Jobportal/AI_libs/Scripts/python.exe','src/middleware/linkedinjobs.py'], check=False)
            count += 1
            print(f"Successfully excuted the scripts {count} time")
        except subprocess.CalledProcessError as e:
            print(f"Error while running the scripts: {e}")
        except Exception as e:
            print(f"Error: {e}")
        

        time.sleep(24*3600)
        return "Sussessfully running the background thread "