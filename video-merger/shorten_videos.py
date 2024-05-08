import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.video.fx.speedx as speedx  # Import speedx module


# Directory containing your MP4 videos
video_directory = "raw_video"

# Get a list of all MP4 files in the directory
video_files = [os.path.join(video_directory, file) for file in os.listdir(video_directory)]

for fileName in video_files:

	try:
		# Load all video clips
		video_clip = VideoFileClip(fileName)
		final_clip = speedx.speedx(video_clip, factor=90)  # 60x speed, adjust as needed
		shortName = fileName.split('\\')[-1].split(".")[0]

		final_clip.write_videofile("short_videos/"+shortName+".mp4", fps=30)
		video_clip.close()

	except:
		print(fileName)