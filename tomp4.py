import pandas as pd
import sys, re
import subprocess

ios = {'src' : '../amt_916_919/',
       'dst' : '../forRating_916/',
       'csv' : 'amt_916_tk.csv'}

ios = {'src' : '../amt_920_923/',
       'dst' : '../forRating_920/',
       'csv' : 'amt_920_tk.csv'}

ios = {'src' : '../amt_907_915/',
       'dst' : '../forRating_907/',
       'csv' : 'amt_907_tk.csv'}

df = pd.read_csv(ios['csv'], dtype=str) # using 'str' for a easy work

# find toRate == 1
tks = df[df['toRate']== '1']
for index, row in tks.iterrows():
    ec = row['entryCode']
    tk = row['turker.index']
    for item in range(1,9):
        webm = ios['src'] + ec + '_' + str(item) + '.webm'
        mp4 =  ios['dst'] + 'SELTCAWRS_t' + str(tk) + '_v' + str(item) + '.mp4'
        fcmd = 'ffmpeg -i ' + webm + ' -s 640x480 -strict -2 -b:v 1000k -c:v h264 -r 30 -y ' + mp4
        print(fcmd)
        subprocess.check_output(['bash', '-c', fcmd])
