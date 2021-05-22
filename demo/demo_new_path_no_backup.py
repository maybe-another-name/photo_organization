from fu_python import move_and_rename_photo
from demo import localpaths


move_and_rename_photo.copy_and_rename_photo(
    photo_path=localpaths.old_file_path, new_photo_folder=localpaths.new_folder)
