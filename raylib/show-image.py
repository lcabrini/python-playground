#! /usr/bin/env python

import os.path
import sys

prog = os.path.basename(sys.argv[0])
if len(sys.argv) < 2:
    print(f"usage: {prog} IMAGE", file=sys.stderr)
    sys.exit(1)

import pyray as pr

pr.set_config_flags(pr.FLAG_VSYNC_HINT)
pr.init_window(1024, 768, "Show  Image")
pr.set_target_fps(60)

texture = pr.load_texture(sys.argv[1])
tw = texture.width
th = texture.height
if tw > 1024 or th > 768:
    scale_x = 1024.0 / tw
    scale_y = 768.0 / th
    scale = scale_y if scale_y < scale_x else scale_x
else:
    scale = 1

tw *= scale
th *= scale

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_texture_ex(texture, (1024/2 - tw/2, 768/2 - th/2), 0, scale, pr.WHITE)
    pr.end_drawing()

pr.unload_texture(texture)
pr.close_window()


