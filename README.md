# Automated Program Launcher 🚀

Python script designed to automatically launch a set of programs when internet connectivity is detected. (for windows)

## Features 🌟

- Automatically launch programs when internet connectivity is available
- The programs to be launched are easily configurable through a TOML configuration file
- The script continuously checks for internet connectivity and will attempt to launch the programs as soon as connectivity is restored

### Usage 💻

1. Ensure you have Python 3.6 or higher installed on your system.
2. Install necessary Python libraries
3. Clone this repository:
   `git clone https://github.com/ExitedState/AutoStartProgram.git`
4. CD to project directory:
   `cd AutoStartProgram`
5. Configure the programs you want to launch in the code line 60-64. Here's an example:

   ```py
   os.environ['DISCORD_PATH'] = 'C:\\Users\\phaib\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
   approved_programs = {
   'discord': os.environ['DISCORD_PATH'],}
   ```

6. Run `main.py` script:
   `python ./main/main.py`
   The script will check for internet connectivity, and will launch the programs in the `config.toml` file as soon as internet connectivity is detected.

### Notes 📝

> This script was designed for Windows. Some features may not work on other OS.<br>
> You can create an executable for windows use pyinstaller `pyinstaller --onefile filename.py` and place in `shell:startup`
