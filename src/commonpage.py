import sys
#filename =  sys.argv[1]
file_prefix = sys.argv[1]

import os
workdir = '../md5'


def findcommompage(filename,needfiles):
#sig db initialize
    sig_db = []
    for f in needfiles:
        fobj = open(workdir+'/'+f, 'r')
        lines = fobj.readlines()
        sig_db.append(lines)

#load pattern
    sig_pattern = open(workdir+'/'+filename, 'r').readlines()

#match
    match_array =[]
    pattern_len = len(sig_pattern)

    for lines in sig_db:
        match_count =0
        rangelen = pattern_len
        if len(lines) < pattern_len:
            rangelen = len(lines)

        for i in range(rangelen):
            if sig_pattern[i].split()[0] =='620f0b67a91f7f74151bc5be745b7110':
                continue
            if sig_pattern[i].split()[0] == lines[i].split()[0]:
               # print 'match ' + sig_pattern[i]
                match_count = match_count +1

        #print match_count
        match_array.append(match_count)


#output
    for i in range(len(needfiles)):
        print needfiles[i],
        print match_array[i]
        if match_array[i] > 0:
            print '* ',
      



#os.chdir(workdir)

pattern_files = []
for files in os.listdir(workdir):
    if files.upper().startswith(file_prefix.upper()):
  #      print files
        pattern_files.append(files);


for f in pattern_files:
    fobj = open(workdir+'/'+f, 'r')
    print f, 
    print len(fobj.readlines())


print '*********************************none zero page count*********************************'
for pattern_file in pattern_files:
    fobj = open(workdir+'/'+pattern_file, 'r')
    lines = fobj.readlines()
    none_zero_page_count =0
    for line in lines:
         if line.split()[0] == '620f0b67a91f7f74151bc5be745b7110':
             continue
         none_zero_page_count = none_zero_page_count +1
    print pattern_file,
    print none_zero_page_count

for pattern_file in pattern_files:
    print '*********************************'+pattern_file+'*********************************' 
    needfiles = pattern_files[:] #copy list
    needfiles.remove(pattern_file)
    findcommompage(pattern_file, needfiles)


