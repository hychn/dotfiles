# Install popular packages
## pdfoutliner
```
pip3 install pdfoutliner==0.0.3
sudo add-apt-repository ppa:malteworld/ppa
sudo apt update
sudo apt install pdftk
```
## android file transfer
May need to do this in ubuntu not dwm
```
sudo apt install android-file-transfer
```


# disable power button turning off immediately in dwm
```
/etc/systemd/logind.conf to have the line HandlePowerKey=ignore
remove the hashtag
```


# Usage
Clone this directory in home directory and call ./push.sh
```
git clone url
cd yotfiles
./push.sh
```

# Orgmode stuff
```
#+BEGIN_COMMENT -*- mode: org -*-
#+END_COMMENT
#+STARTUP: showall
#+HTML_HEAD: <link rel="stylesheet" type="text/css" href="styles.css" />
#+OPTIONS: html-postamble:nil
```

# Future
* install vimplug
* sudo apt-get install python3-neovim
* sudo apt-get install python3-pip
* pip3 install jedi
* install flux
* run scripts on startup

* dwm https://dwm.suckless.org/customisation/windows_key/
* dwm https://dwm.suckless.org/patches/warp/

```
#scripts just add in for now # .xinputrc
# im-config(8) generated on Wed, 15 Mar 2023 16:26:05 +0900
#run_im fcitx
# im-config signature: a7673d91aeb6a4da7061b047288d2e59  -
#
#eDP="$(xrandr | awk '/ connected/ && !/ disconnected/ {print $1}' |  sed -n '1p')"
#HDMI="$(xrandr | awk '/ connected/ && !/ disconnected/ {print $1}' |  sed -n '2p')"
#xrandr --output $eDP --mode 1680x1050 --set 'scaling mode' Full

sleep 0.5
xmodmap -e 'clear Lock' -e 'keycode 0x42 = Alt_L'
#xrandr --output $HDMI --auto --same-as $eDP --mode 1680x1050
xsetroot -solid '#2e3440'redshift -O 3400


#BAT="$(acpi | grep -o '.\{3\}%' | tr -d '%,')%"
#DATE="$(date +'%m.%d. (%a) %H:%M')"
#DWMSTATUS = "${BAT} ${DATE}"
#while true; do xsetroot -name "$DWMSTATUS"; sleep 2; done &
while true; do BAT="$(acpi | awk '{print $4}' | tr -d '%,')%"; DATE="$(date +'%m.%d. (%a) %H:%M')"; DWMSTATUS="${BAT} ${DATE}"; xsetroot -name "$DWMSTATUS"; sleep 2; done &
```

# TODO
ADD power management tools
Add markdown.vim and push to plugged/vim-markdown/syntax in push.sh
hmm seems to have some bug with overlapping wiht other syntax, investigate later
```
syn match mdlatex /$[^$]*\$/
hi mdlatex ctermfg=14  
```
