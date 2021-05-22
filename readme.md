# Photo metadata reader

## Setup

    python3.8 -m venv venv
    source venv/bin/activate
    pip install wheel
    pip install exifread
    pip install .

## General idea
>Make filenames great again!

>Who is your daddy and what does he do?

Filename format:
>'EXIF DateTimeOriginal'__Make__Model

ex:
    2019_01_04__18_10_49__Apple__iPhone_XR.jpg

##### Duplicates?

Datetime precision is to the second.  If that isn't sufficient, and metadata differs, then an exception is raised.  (If the metadata is the same, the duplicate is ignored).


##### Dashes vs underscores?

Online stuff seems to prefer dashes for tokenization.

Locally:
- gedit
  - all tokenization (ctrl+arrow/double-click) is by dash
- Bash
  - ctrl+arrow is by dash & underscore
  - double-click is by dash

Generally more convenient to have the entire filename selected upon double click, so using underscores.

## Inspiration
https://github.com/dbader/photosorter
https://github.com/wting/exifrenamer/blob/master/exifrenamer.py
https://github.com/ianare/exif-py


## Issues

* Detect if the destination file already exists
** Only add the timestamp if there are duplicates?
*** Keep timestamps so they are uniform
** If file has same tags, then don't do anything...
* Helpers for remounting filesystem to be write-able...
* Concurrency (threading)
** Take an entire folder, break it up into chunks, and send it to the queue
* Logging
* Typically complains about not having wheel on first go...
* Improved duplicate handling (differing metadata with same timestamp - suffix?)
* Support for checkpointing really large directories (keeping track of 'last file completed')