# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/konstantinos/.zshrc'
PS1='%n:%B%F{240}%1~%f%b%# '
autoload -Uz compinit
compinit
# End of lines added by compinstall
alias ls='ls -lhNF --color=auto --group-directories-first'

###############################################################
#Custom python script
alias calendar='/home/konstantinos/.mypython/mycalendarscript.py'
#Config alias for git that stores my dots files
alias config='/usr/bin/git --git-dir=/home/konstantinos/.cfg/ --work-tree=/home/konstantinos'
