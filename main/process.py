import psutil
import subprocess
import time
import logging

def check_if_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except psutil.NoSuchProcess:
            pass
    return False

def launch_program(program_name, program_path):
    if not check_if_process_running(program_name):
        try:
            subprocess.run(program_path, start_new_session=True)
            logging.info(f"Opening {program_name.capitalize()}")
            time.sleep(5)
        except FileNotFoundError:
            logging.warning(
                f"{program_name} could not be found. Please check your program path and try again.")
            return False
    return True
