set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath
nmap <C-p> <Plug>MarkdownPreviewToggle
lua require('plugins')

source ~/.vimrc
