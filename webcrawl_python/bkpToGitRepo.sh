#!/usr/bin/env bash

copyTo_mysystemconf() {
    GitRepo=$(git rev-parse --show-toplevel)
    yes | cp ~/.emacs ${GitRepo}/emacs/
    yes | cp -r ~/.emacs.d/packages ${GitRepo}/emacs/
    yes | cp ~/.gitconfig ${GitRepo}/git/
    yes | cp ~/.tmux.conf ${GitRepo}/tmux/
    yes | cp ~/.vimrc ${GitRepo}/vim/
    yes | cp -r ~/.vim/* ${GitRepo}/vim/packages/
    yes | cp ~/.zshrc ${GitRepo}/zsh/
    yes | cp ~/.config/i3/config ${GitRepo}/i3WM/
}

copyTo_mysystemconf
