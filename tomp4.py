import pandas as pd
import sys, re
import subprocess

df = pd.read_csv('amt_916_tk.csv', dtype=str) # using 'str' for a easy work

# find toRate == 1
tks = df[df['toRate']== '1']
for index, row in tks.iterrows():
    ec = row['entryCode']
    tk = row['turker.index']
    for item in range(1,9):
        webm = '../amt_916_919/' + ec + '_' + str(item) + '.webm'
        mp4 = '../forRating_916/SELTCAWRS_t' + str(tk) + '_v' + str(item) + '.mp4'
        fcmd = 'ffmpeg -i ' + webm + ' -s 640x480 -strict -2 -b:v 1000k -c:v h264 -r 30 -y ' + mp4
        print(fcmd)
        subprocess.check_output(['bash', '-c', fcmd])
