#!/usr/bin/env python

import stat
import os
import subprocess
import time
import uuid

#source: http://stackoverflow.com/questions/2773604/query-size-of-block-device-file-in-python
def get_file_size(filename):
    "Get the file size by seeking at end"
    fd= os.open(filename, os.O_RDONLY)
    try:
        return os.lseek(fd, 0, os.SEEK_END)
    finally:
        os.close(fd)

driveName = "sr1"
drivePath = "/dev/" + driveName
disk = False

def driveListen(drivePath, disk):
    
    
    while disk == False:
    
        try:
            get_file_size(drivePath)
            disk = True
        except:
            disk = False

    #do stuff with disk
    print "Disk found, ripping disk"

    """
    #this section was for mounting and examining or copying from the disk instead of imaging

    #make and mount to directory
    os.mkdir("/home/bcadmin/Documents/sr2")
    subprocess.call(["sudo", "mount", "/dev/sr2", "/home/bcadmin/Documents/sr2"], shell=False)

    #list dir
    for stuff in os.listdir("/home/bcadmin/Documents/sr2"):
        print stuff
        if len(stuff) == 8:
            print "found jobnumber"
      
            try:
                for stuff2 in os.listdir(os.path.join("/home/bcadmin/Documents/sr2", stuff)):
                    print stuff2
            except:
                subprocess.call(["chmod", "u-x,go+r", "/home/bcadmin/Documents/sr2"])
                for stuff2 in os.listdir(os.path.join("/home/bcadmin/Documents/sr2", stuff)):
                    print stuff2
        else:
            print "error not an exact job number"

    #unmount disk
    subprocess.call(["lsof", "|", "grep", "/dev/sr2"], shell=False)
    subprocess.call(["sudo", "umount", "/dev/sr2"], shell=False)
    os.rmdir("/home/bcadmin/Documents/sr2")

    """

    
    #image disk
    start = time.time()
    subprocess.call(["dd", "if=/dev/" + driveName, "of=/home/bcadmin/Documents/ua395/disk" + str(uuid.uuid4())  + ".dd"], shell=False)
    end = time.time()
    elapsed = end - start
    print str(elapsed) + " seconds"
    print str(elapsed / 60) + " minutes"
       
    


    print "eject disk"
    subprocess.call(["eject", driveName], shell=False)
    
    print "listen again"
    disk = False
    driveListen(drivePath, disk)

driveListen(drivePath, disk)
