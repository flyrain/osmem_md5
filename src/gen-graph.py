header =[]
header.append('''
=stacked;PGD Identification;Kernel Code Identification;Signature Generation;Signature Matching
column=last
max=100
font=Helvetica
=arithmean
# =sortbmarks
=nogridy
colors=grey1,grey4,grey6,white
=noupperright
legendx=right
legendy=center
=nolegoutline
legendfill=
yformat=%g%%
''')

filename ='bargraph.perf'
f =open(filename,'w+');
f.writelines(header);
f2 = open('barg','r')
f.writelines(f2.readlines())
f.close();

import os
os.system('~/bargraphgen-4.6/bargraph.pl -pdf '+filename+ '> graph.pdf')
