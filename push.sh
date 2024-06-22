#!/bin/bash
cp .vimrc ~/
cp .tmux.conf ~/
cp .pylintrc ~/
cp .spacemacs ~/
cp .xinputrc ~/
mkdir ~/.config
mkdir ~/.config/nvim
cp init.vim ~/.config/nvim
mkdir ~/.vim
mkdir ~/.vim/syntax
cp markdown.vim ~/.vim/syntax
mkdir ~/.emacs.d
cp .emacs.d/init.el ~/.emacs.d/init.el
cp .emacs.d/grayscale-theme.el ~/.emacs.d/grayscale-theme.el

mkdir .termux
cp termux.properties ~/.termux/termux.properties

pip3 install pynvim
