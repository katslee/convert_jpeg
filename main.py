
import os
import pprint
import subprocess

src_dir = 'F:/1999'
dst_dir = 'F:/out'
image = ['.bmp', '.jpg', '.jpeg', '.png']

for root, dirs, files in os.walk(src_dir):
    for f in files:
        prefix, suffix = os.path.splitext(f)
        if suffix.lower() in image:
            abspath_in = root + '/' + f
            dir_out = root.replace(src_dir, dst_dir)
            if not os.path.exists(dir_out):
                os.makedirs(dir_out)
            abspath_out = dir_out + '/' + prefix + '.jpg'
            subprocess.call(['ffmpeg', '-i', abspath_in, '-y', abspath_out])