import os
import json
import requests
import shutil
import re
import collections
import time

step1 = 0
step2 = 0
step3 = 1

#step 1: collect links to vimrc's
if step1:
    print "collecting vimrc links..."
    page = 1

    txts = json.loads("{}")
    while page < 100:
        r = requests.get('https://api.github.com/search/repositories?q=vimrc&L=VimL&page='+str(page))
        if r.status_code == 200:
            items = json.loads(r.text.encode('utf8'))['items']
            if txts:
                txts['items'].extend(items)
            else:
                txts['items'] = items
            print "receiving page %d, length %d" %(page, len(r.text.encode('utf8')))
        time.sleep(1)
        page += 1
    with open('github.json','wb') as f:
        json.dump(txts, f)

#step 2: scrape vimrc's
if step2:
    print "downloading vimrc's"
    github_data = json.load(open('github.json'))['items']
    counter = 0
    for i in github_data:
        r = requests.get('https://raw.githubusercontent.com/'+i['full_name']+'/master/.vimrc')
        if r.status_code == 200:
            with open('github_vimrcs/'+ i['full_name'].replace('/',''),'wb') as f:
                f.write(r.text.encode('utf8'))
        counter += 1
        print "%.2f%%" %(counter*1./len(github_data)*100)

#step 3: process data
if step3:
    vimrcs = []
    total_vimrc = 0
    excluded_keywords = ['endfunction', 'endfunc', 'call', 'if ', 'else', 'endif', 'return', 'augroup', 'Bundle']

    for vimrc in os.listdir('github_vimrcs'):
        total_vimrc += 1
        txt = open('github_vimrcs/'+vimrc,'r').read().split('\n')
        sanitized_txt = []
        for line in txt:
            if (not line.startswith('\"')) and not any(s in line for s in excluded_keywords):
                # strip comments
                sanitized_txt.append(re.sub('\".*$','', line))
                # strip trailing whitespaces
                sanitized_txt[-1] = sanitized_txt[-1].strip()
                # strip empty lines
                if len(sanitized_txt[-1]) == 0: sanitized_txt.pop()
        vimrcs.append(sanitized_txt)

    #flatten the nested list
    vimrcs = [item for sublist in vimrcs for item in sublist]

    print "Most common vim config out of " + str(total_vimrc) + " vimrc's"
    for n,i in enumerate(collections.Counter(vimrcs).most_common(50)):
        print "%d. %s, %.2f%%" %(n, i[0], i[1]*100./total_vimrc)
