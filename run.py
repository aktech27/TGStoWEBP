import pylottie
import os
import time

path = 'TGSfiles'

files = os.listdir(path)
i=0
print("Starting Conversion...\n")

for f in files:
        i+=1
        pylottie.convertLottie2Webp("TGSfiles/{}".format(f), "WEBPfiles/{}.webp".format(f[0:-4]))
        print("Completed %d of %d\r"%(i,len(files)),end="")

print("\n\n\nCompleted all. Please check the WEBPfiles folder")
input("Press any key to close")
