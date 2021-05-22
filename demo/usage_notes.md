# Help Python find it's way

Python still doesn't like using relative paths to import things.  So things need to be 'installed' first.

From the top folder:
>pip install .

## Demo paths

Create a file 'localpaths.py' in this folder, provide variables 'sample_paths', 'old_file_path', 'backup_folder', and 'new_folder' (as needed by the various demos).

## Folders need to be writable

Files can either be copied or moved.

There are three paths (existing, new & backup).  If these drives are mounted, then they need the appropriate ownwership, ex: https://askubuntu.com/questions/75154/cannot-move-file-to-trash-warning-when-trying-to-delete-a-file-in-nautilus/958491#958491

Additionally, Ubuntu can have difficulty with Windows system drives, ex: https://askubuntu.com/questions/857089/cant-mount-ntfs-partition-with-write-permissions