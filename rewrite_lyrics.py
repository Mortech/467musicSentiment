import os


for subdir, dirs, files in os.walk('lyrics/'):
    for file in files:
        f =  open(subdir+'/'+file, 'r')
        newfile = ''
        for line in f:
            newline = line.translate(None, '!.?\n')+'.\n'
            if newline!='.\n':
                newfile+=newline
        f.close()
        f = open(subdir+'/'+file, 'w')
        f.write(newfile)
        f.close()