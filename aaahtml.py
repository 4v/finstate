# /usr/bin/python
# -*- coding: utf-8; py-indent-offset:4 -*-
import sys
import getopt

def showImageInHTML(imageTypes,savedir):
    files=getAllFiles(savedir+'/pic')
    images=[f for f in files if f[f.rfind('.')+1:] in imageTypes]
    images=[item for item in images if os.path.getsize(item)>5*1024]
    images=['pic'+item[item.rfind('/'):] for item in images]
    newfile='%s/%s'%(savedir,'images.html')
    with open(newfile,'w') as f:
        f.write('<div>')
        for image in images:
            f.write("<img src='%s'>\n"%image)
        f.write('</div>')
    print('success,images are wrapped up in %s'%newfile)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error:
            raise Usage(msg)
    except Usage:
        return 2

if __name__ == "__main__":
    sys.exit(main())