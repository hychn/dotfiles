sudo apt-get install build-essential libx11-dev libxinerama-dev sharutils suckless-tools

cd /usr/local/src
sudo wget http://dl.suckless.org/dwm/dwm-6.2.tar.gz
sudo tar xvzf dwm-6.2.tar.gz
chown -R `id -u`:`id -g` dwm-6.2
cd dwm-6.2

sudo apt-get install libxinerama-dev
sudo apt-get install libxft-dev

sudo make clean install

sudo apt-get install dwm
sudo cp /usr/share/xsessions/dwm.desktop{,.bak}
sudo apt-get purge dwm
sudo mv /usr/share/xsessions/dwm.desktop{.bak,}
