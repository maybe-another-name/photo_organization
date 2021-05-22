import exifread
import re
from io import BufferedReader
import pathlib


def new_path_for_photo_file(photo_file: BufferedReader) -> str:
  tags = exifread.process_file(photo_file)

  file_extension = pathlib.Path(photo_file.name).suffix

  image_model = tags['Image Model'].printable
  image_date = tags['EXIF DateTimeOriginal'].printable

  return _filename_with_timestamp_and_model(
      date_string=image_date, image_model=image_model)+file_extension, tags


def _format_timestamp(date_string: str) -> str:
  # replace whitespace with dunder
  whitespace_pattern = "\s"
  replacement_character = "__"
  no_space_date = re.sub(
      whitespace_pattern, replacement_character, date_string)

  # replace all non word characters
  non_word_pattern = "\W"
  replacement_character = "_"
  return re.sub(non_word_pattern, replacement_character, no_space_date)


def _format_model_suffix(image_model: str) -> str:
  return re.sub("\W", "_", image_model.strip())


def _filename_with_timestamp_and_model(date_string: str, image_model: str) -> str:
  return _format_timestamp(date_string) + "__" + _format_model_suffix(image_model=image_model)
