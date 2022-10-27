set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath
nmap <C-p> <Plug>MarkdownPreviewToggle
lua require('plugins')
" spell languages
set spelllang=en_us,el
set spellsuggest=best,5

nnoremap <silent> <F3> :set spell!<CR>
inoremap <silent> <F3> <C-O>:set spell!<CR>

source ~/.vimrc
