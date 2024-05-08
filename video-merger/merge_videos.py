import cv2
import os

output_file = "merged_video.mp4"
directory = "short_videos"

video_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Sort video files to maintain order
video_files.sort()

# Initialize variables
width, height = None, None
writer = None

for file in video_files:
	video_path = os.path.join(directory, file)
	cap = cv2.VideoCapture(video_path)

	if not cap.isOpened():
		print(f"Error: Unable to open video file {video_path}")
		continue

	if width is None or height is None:
		width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

	if writer is None:
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
		writer = cv2.VideoWriter(output_file, fourcc, 30, (width, height))

	while True:
		ret, frame = cap.read()

		if not ret:
			break

		writer.write(frame)

	cap.release()

if writer is not None:
	writer.release()
	print(f"Merged video saved as {output_file}")