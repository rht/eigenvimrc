import os
import json
import requests
import shutil
import re
import collections

def flatten(lst): return [item for sublist in lst for item in sublist]

if 0:
    page = 1

    txts = json.loads("{}")
    while page < 3:
        r = requests.get('https://api.github.com/search/repositories?q=vimrc&L=VimL&page='+str(page))
        if r.status_code == 200:
            txts.update(json.loads(r.text.encode('utf8')))
            #txts = txts + ',' + r.text.encode('utf8')
        page += 1
    with open('github.json','wb') as f:
        json.dump(txts, f)

#github
if 0:
    github_data = json.load(open('github.json'))['items']
    #github_data = flatten([i['items'] for i in json.load(open('github.json','r'))])
    counter = 0
    for i in github_data:
        r = requests.get('https://raw.githubusercontent.com/'+i['full_name']+'/master/.vimrc')
        if r.status_code == 200:
            with open('github_vimrcs/'+ i['full_name'].replace('/',''),'wb') as f:
                f.write(r.text.encode('utf8'))
        counter += 1
        print counter*1./len(github_data)*100

vimrcs = []
total_vimrc = 0
for vimrc in os.listdir('github_vimrcs'):
    total_vimrc += 1
    txt = open('github_vimrcs/'+vimrc,'r').read().split('\n')
    sanitized_txt = []
    for line in txt:
        if (not line.startswith('\"')) and (not 'endfunction' in line) and (not 'else' in line) and (not 'endif' in line):
            sanitized_txt.append(re.sub('\".*$','', line))
            #sanitized_txt[-1] = sanitized_txt[-1].replace(' ', '')
            sanitized_txt[-1] = sanitized_txt[-1].strip()
            if len(sanitized_txt[-1]) == 0:
                sanitized_txt.pop()
    vimrcs.append(sanitized_txt)
vimrcs = flatten(vimrcs)

print "Most common vim config out of " + str(total_vimrc) + " vimrc's"
for n,i in enumerate(collections.Counter(vimrcs).most_common(50)):
    print str(n)+'. '+i[0]+', '+str(i[1])
