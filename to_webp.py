# -*- coding: utf-8 -*-
"""../pipeline/frames_hq/cutNN_a.png 40장 -> img/cutNN.webp (폭 1080, q82)

키프레임을 다시 뽑았을 때만 돌리면 된다.
  python to_webp.py
"""
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "pipeline", "frames_hq")
DST = os.path.join(HERE, "img")
W = 1080
Q = 82

os.makedirs(DST, exist_ok=True)
total_src = total_dst = 0
for n in range(1, 41):
    s = os.path.join(SRC, "cut%02d_a.png" % n)
    d = os.path.join(DST, "cut%02d.webp" % n)
    if not os.path.isfile(s):
        sys.exit("없음: %s" % s)
    im = Image.open(s).convert("RGB")
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    im.save(d, "WEBP", quality=Q, method=6)
    total_src += os.path.getsize(s)
    total_dst += os.path.getsize(d)
    print("cut%02d  %5.1fMB -> %5.0fKB" % (n, os.path.getsize(s) / 1e6, os.path.getsize(d) / 1e3))

print("\n합계  %.1f MB -> %.1f MB" % (total_src / 1e6, total_dst / 1e6))
