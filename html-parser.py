import os
import glob
import fileinput
import re
path = '/path/to/where/files/are/*'
# for infile in glob.glob( os.path.join(path, '*.html') ):
# 	print "current file is: " + infile
	
def scandirs(path):
    fo=open('lalkar.csv','w')
    # fo.write('title|subtitle|text|date\n')

    for currentFile in glob.glob( os.path.join(path, '*.htm*') ):
        if os.path.isdir(currentFile):
            print 'got a directory: ' + currentFile
            scandirs(currentFile)

        title=''
        subtitle=''
        text=''
        f=open(currentFile,'r')
        xfile=f.read()
        xfile=xfile.replace('\n',' ')
        xfile=xfile.replace('\r',' ')

        # r = re.compile('<P ALIGN="CENTER">(.*?)</P>')
        # m = r.search(xfile)
        # if m:
        #     # print m.group(1)
        #     title=m.group(1)
        # r = re.compile('<B><FONT SIZE=4><P>(.*?)</P>')
        # m = r.search(xfile)
        # if m:
        #    # print m.group(1)
        #    title=m.group(1)
        # r = re.compile('<B><FONT SIZE=3><P>(.*?)</P>')
        # m = r.search(xfile)
        # if m:
        #    # print m.group(1)
        #    title=m.group(1)
        # r = re.compile('<B><P>(.*?)</P>')
        # m = r.search(xfile)
        # if m:
        #    # print m.group(1)
        #    title=m.group(1)
        # r = re.compile('<FONT SIZE=4><P ALIGN="JUSTIFY">(.*?)</P>')
        # m = r.search(xfile)
        # if m:
        #    # print m.group(1)
        #    title=m.group(1)
        # r = re.compile('<FONT SIZE=3><P ALIGN="JUSTIFY">(.*?)</P>')
        # m = r.search(xfile)
        # if m:
        #    # print m.group(1)
        #    title=m.group(1)
        # m = re.findall('<P ALIGN="JUSTIFY">(.*?)</P>',xfile, re.DOTALL)
        # for p in m:
        #     # print p
        #     text+=p.rstrip('\n')


        r = re.compile('<span class="title">(.*?)</span>')
        m = r.search(xfile)
        if m:
           print m.group(1)
           title=m.group(1)
        r = re.compile('<span class="subtitle">(.*?)</span>')
        m = r.search(xfile)
        if m:
           print m.group(1)
           subtitle=m.group(1)
 	    
        m = re.findall('<p>(.*?)</p>',xfile,re.MULTILINE)
        for p in m:
            text+='<p>' + p.rstrip('\n') + '</p>'
        if text=='':
            m = re.findall('<br>(.*?)<br>',xfile,re.MULTILINE)
            for p in m:
                text+=p.rstrip('\n').replace('<span class="subtitle"></span>',' ').replace('<a href="mailto:lalkarpublications@hotmail.com"><img src="../../../images/email.gif" width="17" height="13" alt="" border="0"></a> Comments on this article? <a href="mailto:lalkarpublications@hotmail.com">E-mail the editor</a>','').replace('<a class="mainlink" href="mailto:lalkarpublications@hotmail.com"><img src="../../../images/email.gif" width="17" height="13" alt="" border="0"></a> Comments on this article? <a class="mainlink" href="mailto:lalkarpublications@hotmail.com">E-mail the editor</a>','').replace('<span class="subtitle">','<h4>').replace('</span>','</h4>')
            

        r = re.compile('/contents/(.*?)/')
        m=r.search(currentFile)
        # print m.group(1)[0:3].capitalize()
        # print m.group(1)[3:7]
		
        fo.write(title + '|' + subtitle + '|' + text + '|' + '01 ' + m.group(1)[0:3].capitalize() + ' ' +  m.group(1)[3:7] +'\n')

scandirs('/path/to/where/files/are/*')


	