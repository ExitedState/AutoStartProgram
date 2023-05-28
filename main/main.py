import toml
import os
import msvcrt
import logging
from process import check_if_process_running, launch_program
from connectivity import check_internet_connectivity

logging.basicConfig(level=logging.INFO)


def load_config(file_path):
    if not os.path.exists(file_path):
        # Define default approved programs
        default_config = {
            "approved_programs": {
                # "program_name": "program_path"
                # example: "Spotify": "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"
            }
        }
        with open(file_path, 'w') as file:
            toml.dump(default_config, file)
            logging.info(
                f"{file_path} not found. Created default config file.")
    with open(file_path, 'r') as file:
        return toml.load(file)


config = load_config('./main/config.toml')
approved_programs = config['approved_programs']


def main(programs):
    while True:
        if not check_internet_connectivity():
            logging.warning("Press any key to reconnect...")
            msvcrt.getch()
            os.system('cls')
            continue

        all_launched = True
        for program_name, program_path in programs.items():
            if program_name not in approved_programs:
                logging.warning(
                    f"{program_name} is not an approved program and will not be launched.")
                all_launched = False
                break

            if not launch_program(program_name, program_path):
                all_launched = False
                break

        if all_launched and all(check_if_process_running(program) for program in programs):
            break


if __name__ == '__main__':
    main(approved_programs)
