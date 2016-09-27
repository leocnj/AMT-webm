#
# A simple script to generate the csv file guiding PASS raters to finish survey-style
# interview rating.
#
# Due to the nature of generating rating data incrementally, update ts (turker)
#
#
#
import sys
import re
import pandas as pd

ts = list(range(68,128))  # starting ID, ending ID + 1
vs = list(range(1,9))

ids = [''.join(['t', str(t), '_v', str(v)]) for t in ts for v in vs]
print(ids)

videos = [''.join(['https://nlp-pilot.ets.org/videos2016/SELTCAWRS_', id, '.mp4']) for id in ids]
videoLinks = [''.join(['=HYPERLINK(\"', v, '\")']) for v in videos]

df = pd.DataFrame({'VideoID': ids,
                   'VideoLink': videoLinks,
                   'Completed?': ""})

df.to_csv('hs_3rd_batch.csv', index=False)
