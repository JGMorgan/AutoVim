#AutoVim

![](http://i.imgur.com/YliejIw.jpg)

This is made to work with the default Vim 8 package manager.

This is a little script I built so that I can quickly set up vim
on a new computer. It clones all repos for my favorite plugins into
the .vim/pack/plugins/start directory.

Running autovim.py will create all the folders inside of .vim and clone
the plugins.

Running updateplugins.sh will update all the plugins from git.

Make sure you copy over my dotvimrc file into your ~ directory and 
copy over solarized.vim into .vim/colors
