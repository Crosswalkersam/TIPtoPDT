from tqdm import tqdm
import os
import binascii

bitcount = os.stat("noaa_hrpt.tip").st_size
framecount = int(bitcount / 104)
output = open("minorFrames.txt", "w")
blocksize = 1

with open("noaa_hrpt.tip", "rb") as input:
    for counter in tqdm(range(framecount)):
        output.write(str(counter))
        for x in range(104):
            buf = input.read(blocksize)
            result = binascii.hexlify(buf)
            result = str(" ") + result.decode('utf-8')
            output.write(result)
        output.write("\n")