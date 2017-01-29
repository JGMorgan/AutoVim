'''
Creates .vim directory and sub directories and clones my favorite plugins
Makes setting up vim on new computers and work computers easy
'''

import os
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
'''
creates dir tree for .vim
'''
def create_vim_dir_structure():
    dirs = ['~/.vim',
        '~/.vim/colors',
        '~/.vim/pack',
        '~/.vim/pack/plugins',
        '~/.vim/pack/plugins/start']
    for dir in dirs:
        try:
            os.mkdir(dir)
        except OSError:
            print dir, 'already exists'

'''
clones my fav plugins
'''
def clone_plugins():
    plugins = ['https://github.com/scrooloose/nerdtree.git',
        'https://github.com/scrooloose/nerdcommenter.git',
        'https://github.com/rust-lang/rust.vim.git',
        'https://github.com/vim-airline/vim-airline.git',
        'https://github.com/Chiel92/vim-autoformat.git',
        'https://github.com/vim-syntastic/syntastic.git',
        'https://github.com/reasonml/vim-reason-loader.git',
        'https://github.com/sheerun/vim-polyglot.git',
        'https://github.com/Valloric/YouCompleteMe.git']
    print os.getcwd()
    vimdir = os.path.expanduser('~/.vim/pack/plugins/start')
    os.chdir(vimdir)
    for plugin in plugins:
        try:
            subprocess.check_call(['git', 'clone', plugin])
        except subprocess.CalledProcessError:
            print plugin, 'already exists'

'''
updates all repos
'''
def update():
    print dname
    os.chdir(dname)
    try:
        subprocess.check_call(['sh', './updateplugins.sh'])
    except subprocess.CalledProcessError:
        print "couldn't update"

create_vim_dir_structure()
clone_plugins()
update()
