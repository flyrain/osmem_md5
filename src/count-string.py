#filename='linux-assemble-code'
def getPageAddr(line, ostype ):
    if ostype == 'pe':
        strarr = line.split(':')
        return strarr[1][:5]
    if ostype == 'elf':
        return line[:5]


import sys
if len(sys.argv) < 3:
    print 'Please indicate the file and pattern index'
    sys.exit()
filename =  sys.argv[1]
patternIndx = int(sys.argv[2])
argvlen = len(sys.argv)
pattern2 = ''
if(argvlen >3):
    pattern2 = sys.argv[3]
    print 'pattern2 is '+pattern2

f = open(filename,'r')
line = f.readline()
count =0
patterns=['hlt '
,'rdtsc'
,'rdmsr '
,'wrmsr '
,'xsetbv'
,'xgetbv'
,'rdtscp'
,'rdpmc'
,'rsm'
,'invd'
,'invlpg '
,'wbinvd'
, ' dr'
,'clts'
,'%cr'
,' cr'
,'%cr3'
,'%cr0'
,'%cr2'
,'%cr4'
,'0f 01 0d' #sidtl
,'sidt'
,'lidt' 
,'str '
,'ltr '
,'sgdt'
,'lgdt'
,'sldt'
,'lldt'
,'smsw'
,'lmsw']

print 'pattern is ' +patterns[patternIndx]
pagecount =0;
currentpage = '';
while(line != ''):
  
    if (argvlen <= 3 and line.__contains__(patterns[patternIndx])) or (argvlen > 3 and line.__contains__(patterns[patternIndx]) and  line.__contains__(pattern2) ) :
        pageAddr = getPageAddr(line,'elf')
        if (currentpage != pageAddr):
            currentpage = pageAddr
            pagecount = pagecount +1
            print 'Page Index: {0}'.format(pagecount)

        print line.rstrip('\n')
        count = count +1
    
    line = f.readline()
    
print 'count is {0}, page count is {1}'.format(count, pagecount)



