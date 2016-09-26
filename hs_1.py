import sys
import re
import pandas as pd

ts = list(range(23,68))
vs = list(range(1,9))

ids = [''.join(['t', str(t), '_v', str(v)]) for t in ts for v in vs]
print(ids)

videos = [''.join(['https://nlp-pilot.ets.org/videos2016/SELTCAWRS_', id, '.mp4']) for id in ids]
videoLinks = [''.join(['=HYPERLINK(\"', v, '\")']) for v in videos]

df = pd.DataFrame({'VideoID': ids,
                   'VideoLink': videoLinks,
                   'Completed?': ""})

df.to_csv('hs_2nd_batch.csv', index=False)
