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
Most common vim config out of 289 vimrc's

0. set nocompatible, 73.70%
1. syntax on, 73.01%
2. set expandtab, 61.94%
3. filetype plugin indent on, 60.55%
4. set incsearch, 59.86%
5. set hlsearch, 57.79%
6. set number, 57.44%
7. set shiftwidth=4, 53.98%
8. set tabstop=4, 52.94%
9. set ignorecase, 49.83%
10. set ruler, 49.48%
11. set laststatus=2, 48.79%
12. set autoindent, 48.10%
13. set showmatch, 39.79%
14. filetype off, 37.72%
15. set smartcase, 35.64%
16. filetype plugin on, 35.64%
17. set wildmenu, 35.29%
18. set showcmd, 34.26%
19. set t_Co=256, 33.56%
20. set nobackup, 30.80%
21. set softtabstop=4, 30.10%
22. set encoding=utf-8, 29.76%
23. set smarttab, 29.76%
24. set backspace=indent,eol,start, 27.68%
25. set background=dark, 26.99%
26. exe, 25.61%
27. set smartindent, 25.26%
28. set mouse=a, 24.22%
29. set hidden, 23.88%
30. set rtp+=~/.vim/bundle/vundle/, 23.88%
31. filetype indent on, 23.53%
32. autocmd!, 23.53%
33. set cursorline, 23.18%
34. exec, 23.18%
35. set noswapfile, 22.49%
36. syntax enable, 20.76%
37. filetype on, 20.42%
38. set shiftwidth=2, 19.72%
39. set tabstop=2, 19.03%
40. set nu, 18.69%
41. set wrap, 18.69%
42. set nowrap, 17.99%
43. set showmode, 16.26%
44. set autoread, 16.26%
45. au!, 16.26%
46. set guioptions-=T, 16.26%
47. set noerrorbells, 14.88%
48. echon, 14.88%
49. let mapleader =, 14.53%
50. set list, 13.49%
51. endfor, 13.15%
52. echo, 13.15%
53. let rules += [, 12.46%
54. set softtabstop=2, 12.46%
55. colorscheme desert, 12.11%
56. endf, 11.76%
57. set cindent, 11.42%
58. set cmdheight=2, 11.07%
59. set undofile, 11.07%
60. set ai, 10.73%
61. autocmd BufReadPost *, 10.73%
62. set scrolloff=3, 10.38%
63. set shiftround, 10.38%
64. set backspace=2, 10.03%
65. endwhile, 10.03%
66. set novisualbell, 10.03%
67. try, 9.69%
68. set history=1000, 9.69%
69. set autochdir, 9.69%
70. set lazyredraw, 9.69%
71. endtry, 9.69%
72. set visualbell, 9.69%
73. set foldmethod=indent, 9.34%
74. let mapleader=, 9.34%
75. set title, 9.34%
76. set magic, 9.00%
77. set foldenable, 9.00%
78. set clipboard=unnamed, 8.65%
79. set termencoding=utf-8, 8.65%
80. let g:neocomplcache_enable_at_startup = 1, 8.30%
81. set nowb, 8.30%
82. set ttyfast, 8.30%
83. set linebreak, 8.30%
84. colorscheme solarized, 8.30%
85. set backup, 7.96%
86. set wildmode=list:longest, 7.96%
87. set lbr, 7.96%
88. catch, 7.96%
89. set t_vb=, 7.61%
90. set encoding=utf8, 7.61%
91. set si, 7.61%
92. set guioptions-=m, 7.27%
93. break, 6.92%
94. map <C-h> <C-W>h, 6.57%
95. endfun, 6.57%
96. map <C-k> <C-W>k, 6.57%
97. map <C-l> <C-W>l, 6.57%
98. map <C-j> <C-W>j, 6.57%
99. set enc=utf-8, 6.23%

#Plot
![plot](fig.png)
