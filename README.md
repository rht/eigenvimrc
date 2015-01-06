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
Most common vim config out of 411 vimrc's

0. syntax on, 70.80%
1. set nocompatible, 70.32%
2. set expandtab, 61.80%
3. set incsearch, 57.91%
4. set number, 57.91%
5. filetype plugin indent on, 57.42%
6. set hlsearch, 55.72%
7. set shiftwidth=4, 49.88%
8. set autoindent, 49.39%
9. set tabstop=4, 48.42%
10. set ignorecase, 47.93%
11. set ruler, 47.69%
12. set laststatus=2, 46.23%
13. set showmatch, 37.47%
14. filetype off, 34.06%
15. set smartcase, 33.82%
16. filetype plugin on, 33.33%
17. set showcmd, 32.60%
18. set wildmenu, 31.39%
19. set t_Co=256, 29.68%
20. set nobackup, 29.44%
21. set smarttab, 28.95%
22. set softtabstop=4, 28.47%
23. set backspace=indent,eol,start, 27.74%
24. set encoding=utf-8, 27.25%
25. set background=dark, 27.01%
26. set smartindent, 26.03%
27. set hidden, 23.60%
28. set mouse=a, 22.38%
29. set shiftwidth=2, 21.65%
30. set cursorline, 21.41%
31. filetype indent on, 21.17%
32. set rtp+=~/.vim/bundle/vundle/, 21.17%
33. set noswapfile, 21.17%
34. syntax enable, 20.44%
35. exe, 20.19%
36. filetype on, 18.98%
37. autocmd!, 18.98%
38. set tabstop=2, 18.49%
39. exec, 18.49%
40. set wrap, 17.76%
41. set nowrap, 17.76%
42. set nu, 15.82%
43. set guioptions-=T, 15.57%
44. set autoread, 15.33%
45. set showmode, 14.36%
46. set noerrorbells, 14.36%
47. set list, 14.36%
48. au!, 14.36%
49. let mapleader =, 13.87%
50. set softtabstop=2, 12.65%
51. colorscheme desert, 11.92%
52. echo, 11.68%
53. set cindent, 11.19%
54. endfor, 11.19%
55. set novisualbell, 10.71%
56. echon, 10.46%
57. set visualbell, 10.46%
58. autocmd BufReadPost *, 10.22%
59. set undofile, 10.22%
60. let mapleader=, 10.22%
61. set shiftround, 10.22%
62. set cmdheight=2, 9.98%
63. set scrolloff=3, 9.98%
64. endf, 9.73%
65. set ai, 9.49%
66. set title, 9.49%
67. try, 9.25%
68. set backspace=2, 9.25%
69. endtry, 9.25%
70. set history=1000, 9.00%
71. endwhile, 8.76%
72. let rules += [, 8.76%
73. set magic, 8.27%
74. set foldenable, 8.27%
75. set lazyredraw, 8.27%
76. set termencoding=utf-8, 8.27%
77. set foldmethod=indent, 8.03%
78. set t_vb=, 8.03%
79. colorscheme solarized, 8.03%
80. set backup, 7.79%
81. set autochdir, 7.79%
82. catch, 7.79%
83. set nowb, 7.54%
84. set lbr, 7.54%
85. set wildmode=list:longest, 7.54%
86. set ttyfast, 7.54%
87. set linebreak, 7.54%
88. set clipboard=unnamed, 7.30%
89. let g:neocomplcache_enable_at_startup = 1, 6.81%
90. set si, 6.81%
91. map <C-h> <C-W>h, 6.57%
92. set encoding=utf8, 6.57%
93. map <C-k> <C-W>k, 6.57%
94. map <C-l> <C-W>l, 6.57%
95. map <C-j> <C-W>j, 6.57%
96. nnoremap ; :, 6.33%
97. nnoremap k gk, 6.33%
98. nnoremap j gj, 6.33%
99. set guioptions-=m, 6.33%

#Plot
Strangely it doesn't follow the power law distribution. Likely because some settings are highly correlated with the others.
![plot](fig.png)
