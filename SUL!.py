import os,sys
# SUL!
print("Welcome To SUL!")
print("Note: made for fun.")
print("Type 'cmds' to see a list of commands")
# SUL!
while True:
    cmd = input("$~ ")
    if cmd == "cmds":
        print("""
              Arch: yay update, pacman update, pacman update database
              Debian: apt update, apt upgrade
              Fedora: dnf update, dnf upgrade
              OpenSuSE: zypper update""")
    elif cmd == "yay update":
        os.system("yay -Syu") # Upgrade installed packages
    elif cmd == "pacman update":
        os.system("sudo pacman -Syu") # Update the system
    elif cmd == "pacman update database":
        os.system("sudo pacman -Syy") # Update the database
    elif cmd == "apt update":
        os.system("sudo apt uodate") # Update software repositories.
    elif cmd == "apt upgrade":
        os.system("sudo apt upgrade") # Upgrade system software.
    elif cmd == "dnf update": # Update all dnf packages
        os.system("sudo dnf update")
    elif cmd == "dnf upgrade": # Update Fedora Linux using the dnf command
        os.system("sudo dnf upgrade")
    elif cmd == "zypper update": # Update all the packages using the zypper update command
        os.system("sudo zypper update")
    elif cmd == "exit":
        sys.exit()
    else:
        print("Unknown Command.")