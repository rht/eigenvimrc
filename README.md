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

#Plot
![plot](fig.png)
