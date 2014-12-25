This script scrapes vimrc's hosted in github and returns the most commonly used vim configurations.

1. ```mkdir -p github_vimrcs```
2. ```python eigenvimrc.py```

#Tentative result

Most common vim config out of 21 vimrc's:

0. return, 32
1. call append(line(, 20
2. set nocompatible, 17
3. set expandtab, 17
4. set incsearch, 16
5. if has(, 16
6. syntax on, 15
7. filetype plugin indent on, 15
8. set ruler, 14
9. set hlsearch, 14
10. filetype off, 13
11. set smarttab, 13
12. set autoindent, 13
13. set number, 13
14. set showmatch, 12
15. set ignorecase, 12
16. set wildmenu, 12
17. set smartcase, 12
18. NeoBundle, 12
19. augroup END, 11
20. set shiftwidth=4, 10
21. set laststatus=2, 10
22. execute, 10
23. return a:char, 10
24. set encoding=utf-8, 9
25. Bundle 'gmarik/vundle', 9
26. call vundle#rc(), 9
27. set mouse=a, 9
28. set showcmd, 9
29. set shiftwidth=2, 8
30. set rtp+=~/.vim/bundle/vundle/, 8
31. syn match pythonError, 8
32. set t_Co=256, 8
33. Bundle 'scrooloose/nerdtree', 8
34. Bundle, 8
35. set background=dark, 8
36. set tabstop=2, 8
37. \ }, 8
38. set smartindent, 7
39. set wrap, 7
40. set hidden, 7
41. syntax enable, 7
42. set tabstop=4, 7
43. let mapleader =, 7
44. filetype plugin on, 6
45. set noerrorbells, 6
46. filetype indent on, 6
47. set foldmethod=indent, 6
48. set cursorline, 6
49. set softtabstop=4, 6
