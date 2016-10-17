import os
import json
import requests
import collections
import time

import util

# requires internet connection; time intensive
step2 = 0  # 2 for ghtorrent.csv, 1 for github.json

# doesn't require internet connection
step3 = step4 = step5 = 1
step5 = 0

api_url = "https://api.github.com/search/repositories"
content_url = "https://raw.githubusercontent.com/"
tic = time.time()

# step 2: scrape vimrc's
if step2:
    print "downloading vimrc's"
    if step2 is 1:
        data = json.load(open("github.json"))["items"]
    elif step2 is 2:
        data = []
        import csv
        with open("ghtorrent.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)  # skip the header
            for row in reader:
                repo_name = row[0].replace("https://api.github.com/repos/", "")
                data.append({"full_name": repo_name})
    counter = 0
    offset = 0

    def save_text(repo, request):
        with open('github_vimrcs/'+repo['full_name'].replace('/', ''), 'wb') \
                as f:
            f.write(request.text.encode('utf8'))

    # essentially `mkdir -p github_vimrcs`
    if not os.path.isdir("github_vimrcs"):
        os.makedirs("github_vimrcs")
    for i in data:
        if counter > offset:
            r = requests.get(content_url+i['full_name']+'/master/.vimrc')
            if r.status_code == 200:
                save_text(i, r)
            else:
                r2 = requests.get(content_url+i['full_name']+'/master/vimrc')
                if r2.status_code == 200:
                    save_text(i, r2)

        counter += 1
        print "%d %.2f%%" % (counter, counter*1./len(data)*100)

# step 3: process data
if step3:
    vimrcs = []
    total_vimrc = 0
    excluded_keywords = ['endfunction', 'endfunc', 'call', 'if ', 'else',
                         'endif', 'return', 'augroup', 'Bundle', 'execute',
                         '\\ }', '\\', 'endfun', 'endf', 'try', 'endtry',
                         'endwhile', 'catch', 'end', 'au!']

    for vimrc in os.listdir('github_vimrcs'):
        txt = open('github_vimrcs/'+vimrc, 'r').read().split('\n')
        if len(txt) < 10:
            continue
        total_vimrc += 1
        sanitized_txt = []
        for line in txt:
            if (not line.startswith('\"')) and \
               not any(s in line for s in excluded_keywords):
                # strip trailing whitespaces
                sanitized_line = line.strip()
                # strip whitespace surrounding '=' operator
                sanitized_line = sanitized_line.replace(" = ", "=")
                # format short-hand keyword
                sanitized_line = util.keyword_reformat(sanitized_line)
                if len(sanitized_line)>0 and sanitized_line[-1] == ' ':
                    print "ugh"
                    exit()
                # strip comment
                # detection is done by checking if the number of quotes
                # are odd
                if line.count('"') % 2 != 0:
                    sanitized_line = sanitized_line[:sanitized_line.rfind('"')]
                # only append when line is not empty
                if len(sanitized_line) > 0:
                    sanitized_txt.append(sanitized_line)
        vimrcs.append(sanitized_txt)

    # flatten the nested list
    vimrcs = [item for sublist in vimrcs for item in sublist]

    print "Most common vim config out of " + str(total_vimrc) + " vimrc's\n"
    eigenvimrc = collections.Counter(vimrcs).most_common(100)
    for n, i in enumerate(eigenvimrc):
        print "%d. ```%s``` %.2f%%" % (n, i[0], i[1]*100./total_vimrc)

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
            if i[1]*100./total_vimrc >= 30:  # 30% most used
                f.write(i[0]+'\n')

# step 5: generate plot for analysis
if step5:
    if not step3:
        print "this step depends on step #3, please enable step3"
        exit()
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    import pylab
    y = [i[1] for i in eigenvimrc]
    x = range(1, len(y) + 1)
    pylab.scatter(x, y, c='r')
    pylab.ylabel("Number of usage")

    # power law fit
    import scipy.optimize as optimize
    logx = pylab.log10(x)
    logy = pylab.log10(y)

    def fitfunc(p, x):
        return p[0] + p[1] * x

    errfunc = lambda p, x, y: (y - fitfunc(p, x)) ** 2
    powerlaw = lambda x, amp, index: amp * (x**index)
    pinit = [1.0, -1.0]
    out = optimize.leastsq(errfunc, pinit,
                           args=(logx, logy), full_output=1)
    pfinal = out[0]
    covar = out[1]
    index = pfinal[1]
    amp = 10.0**pfinal[0]
    print covar

    pylab.plot(x, powerlaw(x, amp, index))
    pylab.legend(['power law fit', 'data'])
    pylab.xlim([1, x[-1]])

    pylab.savefig('fig.png')

print 'elapsed: ', time.time() - tic
