import os
import json
import requests
import re
import collections
import time

# requires internet connection
step1 = 1
step2 = 1  # most time intensive

# doesn't require internet connection
step3 = 1
step4 = 1
step5 = 1

api_url = 'https://api.github.com/search/repositories'
content_url = 'https://raw.githubusercontent.com/'

# step 1: collect links to vimrc's
if step1:
    print "collecting vimrc links..."
    page = 1

    txts = json.loads("{}")
    while page < 2000:
        r = requests.get('%s?q=vimrc&L=VimL&page=%d&access_token=%s'
                         % (api_url, page,
                            '33245750450464986df3c83a4e65de625d8f1f90'))
        if r.status_code == 200:
            items = json.loads(r.text.encode('utf8'))['items']
            if txts:
                txts['items'].extend(items)
            else:
                txts['items'] = items
            print "receiving page %d, length %d" \
                  % (page, len(r.text.encode('utf8')))
        time.sleep(.1)
        page += 1
    with open('github.json', 'wb') as f:
        json.dump(txts, f)

# step 2: scrape vimrc's
if step2:
    print "downloading vimrc's"
    github_data = json.load(open('github.json'))['items']
    counter = 0
    # essentially `mkdir -p github_vimrcs`
    if not os.path.isdir("github_vimrcs"):
        os.makedirs("github_vimrcs")
    for i in github_data:
        r = requests.get(content_url+i['full_name']+'/master/.vimrc')
        if r.status_code == 200:
            with open('github_vimrcs/' + i['full_name'].replace('/', ''), 'wb') as f:
                f.write(r.text.encode('utf8'))
        else:
            r2. requests.get(content_url+i['full_name']+'/master/vimrc')
            if r2.status_code == 200:
                with open('github_vimrcs/' + i['full_name'].replace('/', ''), 'wb') as f:
                    f.write(r2.text.encode('utf8'))

        counter += 1
        print "%.2f%%" % (counter*1./len(github_data)*100)

# step 3: process data
if step3:
    vimrcs = []
    total_vimrc = 0
    excluded_keywords = ['endfunction', 'endfunc', 'call', 'if ', 'else',
                         'endif', 'return', 'augroup', 'Bundle', 'execute',
                         '\\ }', '\\']

    for vimrc in os.listdir('github_vimrcs'):
        txt = open('github_vimrcs/'+vimrc, 'r').read().split('\n')
        if len(txt) < 10:
            continue
        total_vimrc += 1
        sanitized_txt = []
        for line in txt:
            if (not line.startswith('\"')) and \
               not any(s in line for s in excluded_keywords):
                # strip comments
                sanitized_txt.append(re.sub('\".*$', '', line))
                # strip trailing whitespaces
                sanitized_txt[-1] = sanitized_txt[-1].strip()
                # strip empty lines
                if len(sanitized_txt[-1]) == 0:
                    sanitized_txt.pop()
        vimrcs.append(sanitized_txt)

    # flatten the nested list
    vimrcs = [item for sublist in vimrcs for item in sublist]

    print "Most common vim config out of " + str(total_vimrc) + " vimrc's"
    eigenvimrc = collections.Counter(vimrcs).most_common(100)
    for n, i in enumerate(eigenvimrc):
        print "%d. %s, %.2f%%" % (n, i[0], i[1]*100./total_vimrc)

# step 4: generate eigenvimrc.vim
if step4:
    if not step3:
        print "this step depends on step #3, please enable step3"
        exit()
    # essentially `mkdir -p plugin`
    if not os.path.isdir("plugin"):
        os.makedirs("plugin")
    with open('plugin/eigenvimrc.vim', 'wb') as f:
        for i in eigenvimrc:
            if i[1]*100./total_vimrc >= 50:  # 50% most used
                f.write(i[0]+'\n')

# step 5: generate plot for analysis
if step5:
    if not step3:
        print "this step depends on step #3, please enable step3"
        exit()
    import pylab
    pylab.plot([i[1] for i in eigenvimrc])
    pylab.ylabel("Number of usage")
    pylab.savefig('fig.png')
