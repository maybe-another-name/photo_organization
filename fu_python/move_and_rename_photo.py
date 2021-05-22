from fu_python import photo_renamer
import os
import shutil
import exifread

from dataclasses import dataclass


def copy_and_rename_photo(photo_path: str, new_photo_folder: str, photo_backup_folder: str = None) -> str:
  photo_details = _new_paths(photo_path, new_photo_folder, photo_backup_folder)

  if photo_details.backup_photo_path:
    _duplicate_copy(photo_path, photo_details.original_photo_tags,
                    photo_details.backup_photo_path)
  _duplicate_copy(photo_path, photo_details.original_photo_tags,
                  photo_details.new_photo_path)

# FIXME - needs work to help with non-writeable filesystems
# def move_and_rename_photo(photo_path: str, new_photo_folder: str, photo_backup_folder: str = None) -> str:
#   backup_photo_path, new_photo_path, tags = _new_paths(photo_path, new_photo_folder, photo_backup_folder)

#   _duplicate_copy(photo_path, backup_photo_path)
#   shutil.move(photo_path, new_photo_path)


@dataclass
class PhotoDetails:
  original_photo_tags: dict
  new_photo_path: str
  backup_photo_path: str = None


def _new_paths(photo_path, new_photo_folder, photo_backup_folder=None) -> PhotoDetails:
  with open(photo_path, "rb") as photo_file:
    new_photo_name, tags = photo_renamer.new_path_for_photo_file(
        photo_file=photo_file)

    new_photo_path = os.path.join(new_photo_folder, new_photo_name)

    if not photo_backup_folder:
      return PhotoDetails(tags, new_photo_path)

    backup_photo_path = os.path.join(photo_backup_folder, new_photo_name)

    return PhotoDetails(tags, new_photo_path, backup_photo_path)


def _duplicate_copy(old_photo_path, old_photo_tags, new_photo_path):
  if os.path.exists(new_photo_path):
    # check file metadata
    with open(new_photo_path, "rb") as new_photo_file:
      new_tags = exifread.process_file(new_photo_file)
      if set(old_photo_tags) == set(new_tags):
        print(
            f"{old_photo_path} is duplicate file, skipping copy to {new_photo_path}")
      else:
        raise Exception(f"{old_photo_path} has same timestamp but different metadata")
  else:
    shutil.copyfile(old_photo_path, new_photo_path)
