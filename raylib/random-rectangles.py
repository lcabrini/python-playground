#! /usr/bin/env python

import pyray as pr

pr.set_config_flags(pr.FLAG_VSYNC_HINT)
pr.init_window(1024, 768, "Basic")
pr.set_target_fps(60)

image = pr.load_image_from_screen()
pr.image_clear_background(image, pr.BLACK)

fill = False

while not pr.window_should_close():
    if pr.is_key_pressed(pr.KEY_F):
        fill = not False

    x = pr.get_random_value(0, 1024)
    y = pr.get_random_value(0, 768)
    w = pr.get_random_value(0, 1024-x)
    h = pr.get_random_value(0, 768-y)
    r = pr.get_random_value(0, 255)
    g = pr.get_random_value(0, 255)
    b = pr.get_random_value(0, 255)

    color = pr.Color(r, g, b, 255)
    if fill:
        pr.image_draw_rectangle(image, x, y, w, h, color)
    else:
        pr.image_draw_rectangle_lines(image, (x, y, w, h), 1, color)

    texture = pr.load_texture_from_image(image)

    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_texture(texture, 0, 0, pr.WHITE)
    pr.end_drawing()

    pr.unload_texture(texture)

pr.unload_image(image)
pr.close_window()