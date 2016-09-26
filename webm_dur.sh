ffmpeg -i 480p.webm -f null - 2>&1 | grep time= | sed '.*s/time=\(.*\) bitrate.*/\1/'
