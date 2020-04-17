import os

while True:
    dir = "/tmp/SSH/"
    dirlist = os.listdir(dir)
    for file in dirlist:
        print(file)
        filecontent = open(dir+file,'r')
        with filecontent as fc:
            print(fc.read())
