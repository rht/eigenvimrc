TODO: use ghtorrent

This script scrapes vimrc's hosted in github and returns the most commonly used vim configurations.

```python eigenvimrc.py```

The "voting" process may iterate as follows:

1. People curate their vimrc's.
2. 50% of the most commonly used settings gets assimilated into default.
3. goto #1

#Install
1. Go to ```~/.vim/bundle```
2. Clone this repo
3. Make sure pathogen is available
4. Make sure ```execute pathogen#infect()``` is in ```~/.vimrc```

#Result
Most common vim config out of 710 vimrc's

0. ```syntax on``` 64.51%
1. ```set number``` 55.92%
2. ```set nocompatible``` 50.56%
3. ```set expandtab``` 50.00%
4. ```filetype plugin indent on``` 44.37%
5. ```set autoindent``` 41.55%
6. ```set tabstop=4``` 40.85%
7. ```set shiftwidth=4``` 40.28%
8. ```set hlsearch``` 39.58%
9. ```set laststatus=2``` 37.89%
10. ```set incsearch``` 37.61%
11. ```set ignorecase``` 34.08%
12. ```set encoding=utf-8``` 31.41%
13. ```set background=dark``` 30.99%
14. ```set ruler``` 30.28%
15. ```filetype plugin on``` 29.58%
16. ```set smartcase``` 29.30%
17. ```set t_Co=256``` 27.61%
18. ```let mapleader=","``` 26.48%
19. ```set backspace=indent,eol,start``` 25.63%
20. ```set wildmenu``` 24.93%
21. ```set softtabstop=4``` 24.79%
22. ```set showmatch``` 24.51%
23. ```filetype off``` 23.66%
24. ```set smartindent``` 22.82%
25. ```set nobackup``` 22.11%
26. ```set smarttab``` 21.69%
27. ```set showcmd``` 21.55%
28. ```set rtp+=~/.vim/bundle/vundle/``` 20.85%
29. ```filetype indent on``` 20.14%
30. ```set mouse=a``` 19.58%
31. ```set noswapfile``` 19.01%
32. ```set cursorline``` 18.45%
33. ```set shiftwidth=2``` 18.31%
34. ```set tabstop=2``` 18.17%
35. ```set hidden``` 18.03%
36. ```autocmd!``` 17.32%
37. ```syntax enable``` 16.76%
38. ```filetype on``` 15.63%
39. ```set nowrap``` 13.80%
40. ```set autoread``` 12.96%
41. ```set guioptions-=T``` 12.68%
42. ```colorscheme solarized``` 12.68%
43. ```autocmd BufReadPost *``` 12.68%
44. ```set list``` 12.68%
45. ```set softtabstop=2``` 12.25%
46. ```set noerrorbells``` 11.69%
47. ```set wrap``` 11.41%
48. ```set showmode``` 11.13%
49. ```""``` 10.99%
50. ```set undofile``` 10.42%
51. ```set termencoding=utf-8``` 10.14%
52. ```set novisualbell``` 9.01%
53. ```set cindent``` 8.73%
54. ```filetype plugin indent on     ``` 8.73%
55. ```set nocompatible               ``` 8.59%
56. ```colorscheme desert``` 8.59%
57. ```set fileencoding=utf-8``` 8.45%
58. ```set t_vb=``` 8.17%
59. ```set title``` 7.89%
60. ```let g:mapleader=","``` 7.61%
61. ```set scrolloff=3``` 7.46%
62. ```set wildmode=list:longest``` 7.32%
63. ```filetype off                   ``` 7.32%
64. ```nnoremap ; :``` 7.04%
65. ```set history=1000``` 6.90%
66. ```let g:neocomplcache_enable_at_startup=1``` 6.90%
67. ```nnoremap j gj``` 6.76%
68. ```set backspace=2``` 6.76%
69. ```nnoremap k gk``` 6.76%
70. ```set cmdheight=2``` 6.62%
71. ```set nowb``` 6.62%
72. ```set encoding=utf8``` 6.48%
73. ```set visualbell``` 6.48%
74. ```set linebreak``` 6.34%
75. ```let Tlist_Use_Right_Window=1``` 6.34%
76. ```set lbr``` 6.34%
77. ```set ttyfast``` 6.20%
78. ```autocmd FileType css set omnifunc=csscomplete#CompleteCSS``` 6.20%
79. ```set tm=500``` 6.20%
80. ```set foldmethod=indent``` 6.06%
81. ```set backspace=eol,start,indent``` 6.06%
82. ```colorscheme molokai``` 5.92%
83. ```set modeline``` 5.92%
84. ```set shiftround``` 5.77%
85. ```set clipboard=unnamed``` 5.63%
86. ```vnoremap < <gv``` 5.49%
87. ```map <C-l> <C-W>l``` 5.49%
88. ```map <C-h> <C-W>h``` 5.49%
89. ```vnoremap > >gv``` 5.49%
90. ```set relativenumber``` 5.35%
91. ```map <C-j> <C-W>j``` 5.35%
92. ```autocmd FileType python setlocal omnifunc=pythoncomplete#Complete``` 5.35%
93. ```set magic``` 5.35%
94. ```map <C-k> <C-W>k``` 5.35%
95. ```set whichwrap+=<,>,h,l``` 5.21%
96. ```set nowritebackup``` 5.07%
97. ```set autochdir``` 5.07%
98. ```let rules += [``` 5.07%
99. ```set guioptions-=r``` 4.93%


#Plot
Strangely it doesn't follow the power law distribution. Likely because some settings are highly correlated with the others.
![plot](fig.png)
