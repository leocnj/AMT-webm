ffmpeg -i 480p.webm -s 640x480 -strict -2 -b:v 1000k -c:v h264 -r 30 -y 480p.mp4
