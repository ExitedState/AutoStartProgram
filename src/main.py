import socket
import subprocess
import psutil
import msvcrt
import os
import ctypes

def check_internet_connectivity(timeout=0.5):
    # Check if we can ping a known stable server
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("1.0.0.1", 53))
        print("Internet connectivity detected via DNS query to Cloudflare's DNS server.")
        return True
    except socket.error:
        pass
    # Send a simple HTTP request to a web server
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        print("Internet connectivity detected via DNS query to Google's DNS server.")
        return True
    except socket.error:
        pass

    print("No internet connectivity detected. Please connect to the internet and try again.")
    return False


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
            print(f"Opening {program_name.capitalize()}")
        except FileNotFoundError:
            print(
                f"{program_name} could not be found. Please check your program path and try again.")
            return False
    return True


os.environ['DISCORD_PATH'] = 'C:\\Users\\User\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
os.environ['LINE_PATH'] = 'C:\\Users\\phaib\\AppData\\Local\\LINE\\bin\\LineLauncher.exe'

approved_programs = {
    'discord': os.environ['DISCORD_PATH'],
    'line': os.environ['LINE_PATH']
}

def hide_terminal_window():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)


def main(programs):
    while True:
        if not check_internet_connectivity():
            print("Press any key to reconnect...")
            msvcrt.getch()
            os.system('cls')
            continue
        else:
            hide_terminal_window()

        all_launched = True
        for program_name, program_path in programs.items():
            if program_name not in approved_programs:
                print(f"{program_name} is not an approved program and will not be launched.")
                all_launched = False
                break

            if not launch_program(program_name, program_path):
                all_launched = False
                break

        if all_launched and all(check_if_process_running(program) for program in programs):
            break

if __name__ == '__main__':
    main(approved_programs)