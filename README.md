To make this script runnable as a normal shell command in MacOS I recommend:

1. mkdir -p ~/bin
2. copy the pwgen.py to ~/bin
3. chmod +x pwgen.py
4. mv pwgen.py pwgen
5. edit your ~/.zshrc and add "export PATH=$PATH":$HOME/bin"

This assumes you use zsh, if you are using bash edit your ~/.bash_profile.
This should work basically the same on Linux.