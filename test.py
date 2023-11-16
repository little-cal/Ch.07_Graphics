import arcade
SH = 600
SW = 600
arcade.open_window(SW, SH, "Star Wars Art")
arcade.set_background_color((255, 255, 255))
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(200, 300, 400, 300, arcade.color.AIR_FORCE_BLUE)
arcade.draw_rectangle_filled(SW/2, SH/2, 300, 50, (0, 255, 0, 150), 45)
arcade.draw_rectangle_outline(SW/2, SH/2, 300, 50, (0, 0, 0), 2, -45)
arcade.draw_point(300, 300, arcade.color.AFRICAN_VIOLET, 10)
arcade.draw_line(0, 0, SW, SH, (0, 0, 255), 2)

for i in range(10, SW, 10):
    arcade.draw_line(i, 0, i, SH, (255, 0, 0), 2)

arcade.draw_circle_filled(100, 100, 30, arcade.color.ANTIQUE_BRASS)
arcade.draw_ellipse_filled(400, 400, 300, 60, (0, 255, 0), 45)

radius = 50
y = 50

for i in range(3):
    arcade.draw_circle_filled(100, y, radius, arcade.color.BLUE)
    y=y+1.8*radius
    radius*=.8
arcade.finish_render()

arcade.run()
