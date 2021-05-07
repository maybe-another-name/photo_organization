# Photo metadata reader

## Setup

    python3.8 -m venv venv
    source venv/bin/activate
    pip install exifread

## General idea
>Make filenames great again!

>Who is your daddy and what does he do?

Filename format:
>'EXIF DateTimeOriginal'__Make__Model

ex:
    2019_01_04__18_10_49__Apple__iPhone_XR.jpg

##### Duplicates?

Datetime precision is to the second.  If that isn't sufficient, and filesizes differ, then a roman numeral suffix is applied to the date.  (If the filesizes are the same, the duplicate is discarded).

ex:
    2019_01_04__18_10_49__Apple__iPhone_XR.jpg
    2019_01_04__18_10_49__i__Apple__iPhone_XR.jpg

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