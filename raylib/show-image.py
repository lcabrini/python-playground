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

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_texture(texture, 0, 0, pr.WHITE)
    pr.end_drawing()

pr.unload_texture(texture)
pr.close_window()


