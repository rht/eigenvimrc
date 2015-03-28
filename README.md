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
6. ```set shiftwidth=4``` 40.28%
7. ```set hlsearch``` 39.58%
8. ```set tabstop=4``` 38.45%
9. ```set laststatus=2``` 37.89%
10. ```set incsearch``` 37.61%
11. ```set ignorecase``` 34.08%
12. ```set encoding=utf-8``` 31.41%
13. ```set background=dark``` 30.99%
14. ```set ruler``` 30.28%
15. ```filetype plugin on``` 29.58%
16. ```set smartcase``` 29.30%
17. ```set t_Co=256``` 27.61%
18. ```set backspace=indent,eol,start``` 25.63%
19. ```set wildmenu``` 24.93%
20. ```set showmatch``` 24.51%
21. ```set softtabstop=4``` 23.94%
22. ```filetype off``` 23.66%
23. ```set smartindent``` 22.82%
24. ```set nobackup``` 22.11%
25. ```set smarttab``` 21.69%
26. ```set showcmd``` 21.55%
27. ```set rtp+=~/.vim/bundle/vundle/``` 20.85%
28. ```filetype indent on``` 20.14%
29. ```set mouse=a``` 19.58%
30. ```set noswapfile``` 19.01%
31. ```set cursorline``` 18.45%
32. ```au!``` 18.31%
33. ```set shiftwidth=2``` 18.31%
34. ```set hidden``` 18.03%
35. ```autocmd!``` 17.32%
36. ```syntax enable``` 16.76%
37. ```set tabstop=2``` 16.20%
38. ```filetype on``` 15.63%
39. ```let mapleader = ","``` 15.35%
40. ```set nowrap``` 13.80%
41. ```set autoread``` 12.96%
42. ```set guioptions-=T``` 12.68%
43. ```colorscheme solarized``` 12.68%
44. ```autocmd BufReadPost *``` 12.68%
45. ```set list``` 12.68%
46. ```set softtabstop=2``` 11.83%
47. ```set noerrorbells``` 11.69%
48. ```set wrap``` 11.41%
49. ```""``` 11.13%
50. ```set showmode``` 11.13%
51. ```let mapleader=","``` 11.13%
52. ```set undofile``` 10.42%
53. ```set termencoding=utf-8``` 10.14%
54. ```set novisualbell``` 9.01%
55. ```try``` 8.87%
56. ```endtry``` 8.87%
57. ```filetype plugin indent on     ``` 8.87%
58. ```set cindent``` 8.73%
59. ```colorscheme desert``` 8.59%
60. ```set nocompatible               ``` 8.59%
61. ```set fileencoding=utf-8``` 8.45%
62. ```set t_vb=``` 8.17%
63. ```set title``` 7.89%
64. ```endwhile``` 7.61%
65. ```set scrolloff=3``` 7.46%
66. ```catch``` 7.46%
67. ```set wildmode=list:longest``` 7.32%
68. ```filetype off                   ``` 7.32%
69. ```nnoremap ; :``` 7.04%
70. ```end``` 6.90%
71. ```set history=1000``` 6.90%
72. ```nnoremap j gj``` 6.76%
73. ```set backspace=2``` 6.76%
74. ```nnoremap k gk``` 6.76%
75. ```set cmdheight=2``` 6.62%
76. ```set nowb``` 6.62%
77. ```set encoding=utf8``` 6.48%
78. ```set visualbell``` 6.48%
79. ```set linebreak``` 6.34%
80. ```set lbr``` 6.34%
81. ```set ttyfast``` 6.20%
82. ```autocmd FileType css set omnifunc=csscomplete#CompleteCSS``` 6.20%
83. ```set tm=500``` 6.20%
84. ```set foldmethod=indent``` 6.06%
85. ```set backspace=eol,start,indent``` 6.06%
86. ```colorscheme molokai``` 5.92%
87. ```set modeline``` 5.92%
88. ```let g:neocomplcache_enable_at_startup = 1``` 5.77%
89. ```set shiftround``` 5.77%
90. ```set clipboard=unnamed``` 5.63%
91. ```vnoremap < <gv``` 5.49%
92. ```map <C-l> <C-W>l``` 5.49%
93. ```map <C-h> <C-W>h``` 5.49%
94. ```vnoremap > >gv``` 5.49%
95. ```set relativenumber``` 5.35%
96. ```map <C-j> <C-W>j``` 5.35%
97. ```autocmd FileType python setlocal omnifunc=pythoncomplete#Complete``` 5.35%
98. ```set magic``` 5.35%
99. ```map <C-k> <C-W>k``` 5.35%


#Plot
Strangely it doesn't follow the power law distribution. Likely because some settings are highly correlated with the others.
![plot](fig.png)
