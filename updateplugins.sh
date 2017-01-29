#!/bin/bash
find ~/.vim/pack/plugins/start/ -maxdepth 1 -type d -exec sh -c '(cd {} && git pull && git submodule update --init --recursive)' ';'
