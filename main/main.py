import os
import msvcrt
import logging
import time
from process import check_if_process_running, launch_program
from connectivity import check_internet_connectivity

logging.basicConfig(level=logging.INFO)

os.environ['DISCORD_PATH'] = 'C:\\Users\\phaib\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
os.environ['LINE_PATH'] = 'C:\\Users\\phaib\\AppData\\Local\\LINE\\bin\\LineLauncher.exe'

approved_programs = {
    'discord': os.environ['DISCORD_PATH'],
    'line': os.environ['LINE_PATH']
}

def main(programs):
    while True:
        all_launched = True
        if check_internet_connectivity():
            time.sleep(3)
            for program_name, program_path in programs.items():
                if program_name in approved_programs:
                    if not launch_program(program_name, program_path):
                        all_launched = False
                        break
                else:
                    logging.warning(
                        f"{program_name} is not an approved program and will not be launched.")
        if all_launched and check_if_process_running("discord") and check_if_process_running('line'):
            break
        logging.warning("Press any key to reconnect...")
        msvcrt.getch()
        os.system('cls')


if __name__ == '__main__':
    main(approved_programs)
