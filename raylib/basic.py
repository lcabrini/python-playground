#! /usr/bin/env python

import pyray as pr

pr.set_config_flags(pr.FLAG_VSYNC_HINT)
pr.init_window(1024, 768, "Basic")
pr.set_target_fps(60)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.end_drawing()

pr.close_window()