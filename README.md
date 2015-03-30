TODO2: create phylogenetic tree of vimrcs

This script scrapes vimrc's hosted in github and returns the most commonly used vim configurations.

```python eigenvimrc.py```

The "voting" process may iterate as follows:

```python
def vote(default):
    vimrcs = people_curate_their_vimrc()
    sleep(a_month)
    new_default = most_common_50_percent(vimrcs)
    if new_default != default:
        return vote(new_default)
    else:
        return new_default
```

#Install
3. Make sure pathogen is available and ```execute pathogen#infect()``` is in ```~/.vimrc```
2. ```cd ~/.vim/bundle```
3. ```git clone git://github.com/tpope/vim-fugitive.git```

#Result
```syntax on``` > ```set no compatible```

Most common vim config out of 11804 vimrc's

0. ```syntax on``` 70.70%
1. ```set number``` 59.72%
2. ```set nocompatible``` 59.18%
3. ```filetype plugin indent on``` 53.67%
4. ```set expandtab``` 52.71%
5. ```set hlsearch``` 47.80%
6. ```set laststatus=2``` 47.41%
7. ```set incsearch``` 40.30%
8. ```set ignorecase``` 39.67%
9. ```set backspace=indent,eol,start``` 38.71%
10. ```let mapleader=","``` 38.09%
11. ```set background=dark``` 37.10%
12. ```set ruler``` 34.95%
13. ```set tabstop=2``` 34.45%
14. ```set autoindent``` 33.54%
15. ```set wildmenu``` 31.93%
16. ```set smartcase``` 29.55%
17. ```set t_Co=256``` 29.41%
18. ```set showcmd``` 28.66%
19. ```set shiftwidth=2``` 28.05%
20. ```set cursorline``` 26.75%
21. ```set tabstop=4``` 26.63%
22. ```set shiftwidth=4``` 26.62%
23. ```autocmd!``` 26.45%
24. ```set nobackup``` 26.35%
25. ```set mouse=a``` 25.49%
26. ```filetype off``` 25.45%
27. ```set encoding=utf-8``` 24.22%
28. ```set list``` 23.86%
29. ```set showmatch``` 21.64%
30. ```syntax enable``` 19.83%
31. ```set hidden``` 19.69%
32. ```set noswapfile``` 19.42%
33. ```autocmd BufReadPost *``` 19.18%
34. ```set title``` 18.51%
35. ```filetype plugin on``` 18.41%
36. ```set smartindent``` 18.38%
37. ```set showmode``` 18.24%
38. ```filetype on``` 18.08%
39. ```colorscheme solarized``` 17.97%
40. ```set smarttab``` 17.24%
41. ```set relativenumber``` 16.70%
42. ```set ttyfast``` 16.37%
43. ```set noerrorbells``` 16.09%
44. ```set softtabstop=4``` 15.85%
45. ```set nowrap``` 15.57%
46. ```set scrolloff=3``` 15.49%
47. ```set clipboard=unnamed``` 15.33%
48. ```set softtabstop=2``` 13.61%
49. ```set nowritebackup``` 13.50%
50. ```filetype indent on``` 13.39%
51. ```set undodir=~/.vim/undo``` 13.20%
52. ```set gdefault``` 12.87%
53. ```set rtp+=~/.vim/bundle/vundle/``` 12.56%
54. ```let save_cursor=getpos(".")``` 12.29%
55. ```set backupdir=~/.vim/backups``` 12.28%
56. ```set modeline``` 12.02%
57. ```let old_query=getreg('/')``` 12.00%
58. ```set directory=~/.vim/swaps``` 12.00%
59. ```set nostartofline``` 11.36%
60. ```set autoread``` 11.18%
61. ```set splitright``` 10.33%
62. ```set undofile``` 10.08%
63. ```set shortmess=atI``` 10.01%
64. ```set splitbelow``` 9.81%
65. ```set binary``` 9.34%
66. ```set noeol``` 9.32%
67. ```set encoding=utf-8 nobomb``` 9.24%
68. ```set esckeys``` 9.16%
69. ```set rtp+=~/.vim/bundle/Vundle.vim``` 9.00%
70. ```nnoremap k gk``` 8.81%
71. ```nnoremap j gj``` 8.79%
72. ```function! StripWhitespace()``` 8.66%
73. ```autocmd BufNewFile,BufRead *.json setfiletype json syntax=javascript``` 8.61%
74. ```set wrap``` 8.60%
75. ```set numberwidth=5``` 8.54%
76. ```set wildmode=list:longest,list:full``` 8.53%
77. ```noremap <leader>W :w !sudo tee % > /dev/null<CR>``` 8.52%
78. ```au BufReadPost * set relativenumber``` 8.20%
79. ```set exrc``` 7.88%
80. ```let g:airline_powerline_fonts=1``` 7.87%
81. ```set secure``` 7.84%
82. ```set visualbell``` 7.65%
83. ```colorscheme molokai``` 7.63%
84. ```Plugin 'gmarik/Vundle.vim'``` 7.45%
85. ```nnoremap Y y$``` 7.05%
86. ```set modelines=4``` 7.00%
87. ```set guioptions-=T``` 6.90%
88. ```set laststatus=2 ``` 6.85%
89. ```let g:Tlist_Ctags_Cmd="ctags --exclude='*.js'"``` 6.79%
90. ```set shiftround``` 6.68%
91. ```set history=1000``` 6.51%
92. ```set ignorecase ``` 6.51%
93. ```let g:Powerline_symbols='fancy'``` 6.49%
94. ```autocmd FileType text setlocal textwidth=78``` 6.45%
95. ```set lazyredraw``` 6.25%
96. ```set wildmode=list:longest``` 6.18%
97. ```nnoremap <C-h> <C-w>h``` 6.10%
98. ```nnoremap <C-l> <C-w>l``` 6.07%
99. ```nnoremap <C-k> <C-w>k``` 6.06%


#Plot
Strangely it doesn't follow the power law distribution. Likely because some settings are highly correlated with the others.
![plot](fig.png)

#Data
Repository list is queried from [ghtorrent.org/dblite/](ghtorrent.org/dblite/)
```select * from projects where language = 'VimL' and name = 'dotfiles'```
