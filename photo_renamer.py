import exifread
import re
from pathlib import Path

INPUT_DIR = "~/Pictures"
OUTPUT_DIR = "~/Pictures/sorted"

# file just has a list called 'sample_paths'
import localpaths


def format_date(date_string: str) -> str:
  # replace whitespace with dunder
  whitespace_pattern = "\s"
  replacement_character = "__"
  no_space_date = re.sub(
      whitespace_pattern, replacement_character, date_string)

  # replace all non word characters
  non_word_pattern = "\W"
  replacement_character = "_"
  return re.sub(non_word_pattern, replacement_character, no_space_date)


def format_model_suffix(image_model: str) -> str:
  return re.sub("\W", "_", image_model.strip())


def filename_with_date_and_model(date_string: str, image_model: str) -> str:
  return format_date(date_string) + "__" + format_model_suffix(image_model=image_model)


for photo_path in localpaths.sample_paths:
  file_photo = open(photo_path, "rb")
  tags = exifread.process_file(file_photo)

  image_model = tags['Image Model'].printable
  image_date = tags['EXIF DateTimeOriginal'].printable

  print(filename_with_date_and_model(
      date_string=image_date, image_model=image_model))
  #print("\t"+image_date)
  #print("\t"+image_model)
