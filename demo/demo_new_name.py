from demo import localpaths
from fu_python import photo_renamer

for photo_path in localpaths.existing_photo_paths:
  photo_file = open(photo_path, "rb")
  new_photo_name = photo_renamer.new_path_for_photo_file(photo_file=photo_file)[0]
  print(f"rename from: \n\t\t{photo_path} \n\tto \n\t\t{new_photo_name}")
