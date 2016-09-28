video:
	ffmpeg -y -r 15 -i "frames/frame_%03d.png" animated.mp4

frames:
	python geometry.py

tags:
	ctags -R
