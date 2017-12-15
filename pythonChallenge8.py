"""
* On clicking image, opens a pop-up asking username and password.
* The page source has `un` and `pw`.
* Strings are bz2 encoded strings.
* Write these strings to a bz2 file and open (decompress) and you'll find the
plain text username and password
"""

import bz2


f = bz2.BZ2File('level8.bz2', 'w')
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

f.write(un)
f.close()
