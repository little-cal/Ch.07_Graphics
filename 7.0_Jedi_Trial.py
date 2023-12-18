import arcade
SH = 600
SW = 600
arcade.open_window(SW, SH, "213740")
arcade.set_background_color(arcade.color.AMAZON)
arcade.start_render()

# vertical lines for grid
for i in range(200, SW, 200):
    arcade.draw_line(i, 0, i, SH, arcade.color.BLACK)
# horizontal lines for grid
for i in range(200, SH, 200):
    arcade.draw_line(0, i, SW, i, arcade.color.BLACK)

# Upper left rectangle
arcade.draw_rectangle_filled(100, 500, 50, 50, arcade.color.NEON_CARROT)
arcade.draw_rectangle_outline(100, 500, 50, 50, arcade.color.BLACK, 2)

# filled circle
arcade.draw_circle_filled(300, 500, 50, arcade.color.BRIGHT_TURQUOISE)

# Left tilted polygon
polygon_point_list = [(100, 200), (200, 300), (100, 400), (0, 300)]
arcade.draw_polygon_filled(polygon_point_list, arcade.color.BARBIE_PINK)

# pac-man/arc upper right
arcade.draw_arc_filled(500, 500, 50, 50, arcade.color.YELLOW, -150, 150)

# diagonal lines in center
for i in range(220, 420, 20):
    arcade.draw_line(i, 200, 200, i, arcade.color.BLACK)
    arcade.draw_line(400, i, i, 400, arcade.color.BLACK)

# flag center left
y = 210
for i in range(5):
    arcade.draw_rectangle_filled(500, y, 200, 20, arcade.color.WHITE)
    y += 40
y = 230
for i in range(5):
    arcade.draw_rectangle_filled(500, y, 200, 20, arcade.color.RED)
    y += 40
arcade.draw_rectangle_filled(450, 350, 100, 100, arcade.color.NAVY_BLUE)

# repeating circles bottom left
for i in range(0, 200, 40):
    arcade.draw_circle_filled(i+20, 100, 20, arcade.color.BLUEBERRY)

# dot grid center bottom
for i in range(10, 200, 10):
    for j in range(210, 400, 10):
        arcade.draw_point(j, i, arcade.color.NEON_GREEN, 2)

# text bottom right
arcade.draw_text("Caleb Little", 460, 100, arcade.color.BLACK, 12, 100)
arcade.finish_render()
arcade.run()
