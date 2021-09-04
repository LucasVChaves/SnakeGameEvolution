# Snake Game Evolution

## What is this?

It is a common Snake Game clone, but, when you loose the game, it punishes you by setting up a reverse-shell, rick rolling you and starting a fake windows update screen.  

All malware code is located in `malware.py`, and all game code in `main.py`.  
The game is built with [Pygame](https://www.pygame.org/wiki/about).  
NetCat listener command: `stty raw -echo; (stty size; cat) | nc -lvnp 666`. For some reason it only works on a bash shell, `sudo command` won't do.  
The reverse-shell one-liner is not from my authorship, check it [here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#c).  

This program was built for a Coding Jam, please ignore any bad or spaghetti code.  

## TODO:

- [x] Build a working snake game.
- [x] Create the reverse-shell.
- [x] NetCat listener at the attacker machine.
- [x] Add the Rick Roll and Windows Update Screen.
- [x] Loading the malware only when the player looses.
- [ ] Make a `.exe` with Pyinstaller.

*Disclaimer: This software contains possible malicious code. It SHOULD NOT be used without consent of the target, and the author IS NOT responsible for any misuse of the code, this is just for educational and academic purposes.*