from datetime import datetime
import piexif
from os import listdir, path
import json

directoryPath = 'C:\Users\owenm\Downloads\Takeout\Google Photos\Photos from 2018'
filenames = set()
for i in listdir('testdata'):
  filenames.add(path.splitext(path.splitext(i)[0])[0])

for i in filenames:

  imagePath = f'{directoryPath}/{i}.jpeg'
  jsonPath = f'{directoryPath}/{i}.jpeg.json'
  
  # open the json and get the date
  file = open(jsonPath)
  jsonData = json.loads(file.read())
  file.close()
  new_date = datetime.fromtimestamp(int(jsonData['photoTakenTime']['timestamp'])).strftime("%Y:%m:%d %H:%M:%S")

  # modify the image data
  exif_dict = piexif.load(imagePath)
  exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
  exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
  exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
  exif_bytes = piexif.dump(exif_dict)
  piexif.insert(exif_bytes, imagePath)
