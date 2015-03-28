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
1. ```set nocompatible``` 50.56%
2. ```set expandtab``` 50.00%
3. ```filetype plugin indent on``` 44.37%
4. ```set number``` 43.10%
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
42. ```set nu``` 12.82%
43. ```set guioptions-=T``` 12.68%
44. ```colorscheme solarized``` 12.68%
45. ```autocmd BufReadPost *``` 12.68%
46. ```set list``` 12.68%
47. ```endf``` 11.97%
48. ```set softtabstop=2``` 11.83%
49. ```set noerrorbells``` 11.69%
50. ```set wrap``` 11.41%
51. ```""``` 11.13%
52. ```set showmode``` 11.13%
53. ```let mapleader=","``` 11.13%
54. ```endfun``` 10.99%
55. ```endfor``` 10.56%
56. ```set undofile``` 10.42%
57. ```set termencoding=utf-8``` 10.14%
58. ```set novisualbell``` 9.01%
59. ```try``` 8.87%
60. ```endtry``` 8.87%
61. ```filetype plugin indent on     ``` 8.87%
62. ```set cindent``` 8.73%
63. ```colorscheme desert``` 8.59%
64. ```set nocompatible               ``` 8.59%
65. ```set fileencoding=utf-8``` 8.45%
66. ```set t_vb=``` 8.17%
67. ```set title``` 7.89%
68. ```endwhile``` 7.61%
69. ```set scrolloff=3``` 7.46%
70. ```catch``` 7.46%
71. ```set wildmode=list:longest``` 7.32%
72. ```filetype off                   ``` 7.32%
73. ```nnoremap ; :``` 7.04%
74. ```end``` 6.90%
75. ```set history=1000``` 6.90%
76. ```nnoremap j gj``` 6.76%
77. ```set backspace=2``` 6.76%
78. ```nnoremap k gk``` 6.76%
79. ```set cmdheight=2``` 6.62%
80. ```set nowb``` 6.62%
81. ```set encoding=utf8``` 6.48%
82. ```set visualbell``` 6.48%
83. ```set linebreak``` 6.34%
84. ```set lbr``` 6.34%
85. ```set ttyfast``` 6.20%
86. ```autocmd FileType css set omnifunc=csscomplete#CompleteCSS``` 6.20%
87. ```set tm=500``` 6.20%
88. ```set foldmethod=indent``` 6.06%
89. ```set backspace=eol,start,indent``` 6.06%
90. ```colorscheme molokai``` 5.92%
91. ```set modeline``` 5.92%
92. ```let g:neocomplcache_enable_at_startup = 1``` 5.77%
93. ```set shiftround``` 5.77%
94. ```set clipboard=unnamed``` 5.63%
95. ```vnoremap < <gv``` 5.49%
96. ```map <C-l> <C-W>l``` 5.49%
97. ```map <C-h> <C-W>h``` 5.49%
98. ```vnoremap > >gv``` 5.49%
99. ```map <C-j> <C-W>j``` 5.35%

#Plot
Strangely it doesn't follow the power law distribution. Likely because some settings are highly correlated with the others.
![plot](fig.png)
