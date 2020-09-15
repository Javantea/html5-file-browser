#!/usr/bin/env python3
"""
Make an index.
"""

import glob
import urllib.parse

b = ''
for file in glob.glob('*.png') + glob.glob('*.flac') + glob.glob('*.gif') + glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.ogg'):
    b += '<a href="{0}">{1}</a>\n'.format(urllib.parse.quote(file), file)

open('uploads.html','w').write(b)
