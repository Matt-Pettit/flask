# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import os,time,sys



def main():
    try:
        filename = str(sys.argv[1])

    except:
        print("Error: Did you forget the file name?")
        sys.exit(1)
    file = os.stat(filename)
    filesize = file.st_size

    def last():
        fileHandle = open( filename,"r")
        lineList = fileHandle.readlines()
        fileHandle.close()
        print(lineList[len(lineList)-1])

    while True:
        file = os.stat(filename)
        if filesize != file.st_size:
            filesize = file.st_size
            last()

    time.sleep(float(0.005))

main()
