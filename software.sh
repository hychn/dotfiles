sudo snap install emacs --classic
rm -rf $HOME/.emacs.d
git clone https://github.com/hychn/spacemacs $HOME/.emacs.d
sudo apt install texlive
sudo apt install texlive-latex-extra
sudo apt install okular
sudo apt install dvipng
sudo apt install nmtui
sudo apt install sagemath
sudo apt install tmux
sudo apt install flameshot


sudo systemctl stop unattended-upgrades
sudo apt-get purge unattended-upgrades

