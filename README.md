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
0. set nocompatible, 77.18%
1. syntax on, 75.77%
2. set expandtab, 64.37%
3. filetype plugin indent on, 61.27%
4. set incsearch, 60.99%
5. set hlsearch, 59.86%
6. set number, 59.72%
7. set autoindent, 53.38%
8. set laststatus=2, 52.39%
9. set ignorecase, 51.97%
10. set ruler, 51.13%
11. set shiftwidth=4, 49.86%
12. set tabstop=4, 47.46%
13. set showmatch, 41.13%
14. filetype off, 38.87%
15. set showcmd, 38.17%
16. set wildmenu, 37.18%
17. set smartcase, 36.76%
18. set backspace=indent,eol,start, 35.21%
19. set encoding=utf-8, 34.93%
20. set background=dark, 34.93%
21. filetype plugin on, 34.37%
22. set t_Co=256, 34.08%
23. set nobackup, 31.97%
24. set smarttab, 29.58%
25. set softtabstop=4, 28.73%
26. set hidden, 27.89%
27. set cursorline, 27.32%
28. set smartindent, 26.90%
29. set mouse=a, 25.35%
30. filetype indent on, 24.37%
31. set noswapfile, 22.11%
32. set shiftwidth=2, 21.97%
33. set nowrap, 21.13%
34. syntax enable, 20.85%
35. set rtp+=~/.vim/bundle/vundle/, 20.85%
36. exec, 20.42%
37. set tabstop=2, 19.44%
38. set autoread, 19.30%
39. set showmode, 19.30%
40. filetype on, 19.30%
41. exe, 18.59%
42. au!, 18.31%
43. let mapleader =, 17.32%
44. autocmd!, 17.32%
45. set wrap, 17.04%
46. set guioptions-=T, 17.04%
47. set noerrorbells, 16.62%
48. set nu, 15.63%
49. set list, 15.35%
50. let mapleader=, 13.80%
51. set softtabstop=2, 13.80%
52. set title, 13.80%
53. colorscheme solarized, 13.24%
54. set undofile, 13.24%
55. autocmd BufReadPost *, 12.68%
56. set novisualbell, 12.25%
57. endf, 11.97%
58. set history=1000, 11.69%
59. echo, 11.55%
60. set scrolloff=3, 11.27%
61. endfun, 10.99%
62. set shiftround, 10.85%
63. set cmdheight=2, 10.70%
64. endfor, 10.56%
65. set visualbell, 10.56%
66. set cindent, 10.56%
67. set termencoding=utf-8, 10.42%
68. set backspace=2, 10.14%
69. colorscheme desert, 9.72%
70. set wildmode=list:longest, 9.58%
71. set ttyfast, 9.44%
72. set linebreak, 9.44%
73. set fileencoding=utf-8, 9.01%
74. set t_vb=, 8.87%
75. try, 8.87%
76. endtry, 8.87%
77. set foldmethod=indent, 8.73%
78. set ai, 8.59%
79. set clipboard=unnamed, 8.31%
80. set foldenable, 8.31%
81. set magic, 8.03%
82. set backup, 7.89%
83. set lazyredraw, 7.89%
84. endwhile, 7.89%
85. catch, 7.46%
86. set guioptions-=m, 7.32%
87. set undolevels=1000, 7.18%
88. set autochdir, 7.18%
89. nnoremap ; :, 7.04%
90. set gdefault, 6.90%
91. end, 6.90%
92. set history=50, 6.90%
93. set modeline, 6.90%
94. set nowb, 6.90%
95. set encoding=utf8, 6.76%
96. nnoremap j gj, 6.76%
97. nnoremap k gk, 6.76%
98. set nowritebackup, 6.62%
99. set lbr, 6.48%

#Plot
Strangely it doesn't follow the power law distribution. Likely because some settings are highly correlated with the others.
![plot](fig.png)
