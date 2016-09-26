import subprocess
import sys
import re
from os import listdir
from os.path import isfile, join
import pandas as pd

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(m) * 60 + int(s)

def one_dur(webm):
    fcmd = 'ffmpeg -i ' + webm + ' -f null - 2>&1 | grep time='
    try:
        # all [null @] error, fout contains two lines and need merge to one
        # to let regexpr work correctly!
        fout = subprocess.check_output(['bash', '-c', fcmd]).replace('\n', '')
        # print(fout)
        t_hms = re.search('^.+time=(.+)\.\d+ ', fout.rstrip()).group(1)
        print(webm + ': ' + t_hms)
        t_sec = get_sec(t_hms)
    except Exception, e:
        t_sec = 0
    return(t_sec)

# check all webm videos in a dir (argv[1]) and save DF into argv[2]
mypath = sys.argv[1]
webms = [f for f in listdir(mypath) if isfile(join(mypath, f))]
secs = [one_dur(join(mypath, w)) for w in webms]

df = pd.DataFrame({'id': webms,
                   'dur': secs})
df.to_csv(sys.argv[2], index=False)
