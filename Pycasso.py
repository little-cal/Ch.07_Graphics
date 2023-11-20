'''
PYCASSO PROJECT (4pts)
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
import random
SH = 500
SW = 500
arcade.open_window(SW, SH, "Caleb Little")
arcade.set_background_color(arcade.color.UBE)
arcade.start_render()
# making a randomized background
transparency = 255
for j in range(transparency):
    for i in range(8):
        x = random.randint(0, SW)
        y = random.randint(0, SH)
        r = random.randint(15, 30)
        arcade.draw_circle_filled(x, y, r, (105, 53, 156, transparency))
    transparency -= 1
    for i in range(8):
        x = random.randint(0, SW)
        y = random.randint(0, SH)
        r = random.randint(15, 30)
        arcade.draw_circle_filled(x, y, r, (150, 120, 182, transparency))
    transparency -= 1
    for i in range(8):
        x = random.randint(0, SW)
        y = random.randint(0, SH)
        r = random.randint(15, 30)
        arcade.draw_circle_filled(x, y, r, (78, 81, 128, transparency))
    transparency -= 1
# border around the entire picture
arcade.draw_rectangle_outline(250, 250, SW, SH, arcade.color.UBE, 16)
arcade.draw_rectangle_outline(250, 250, SW-7.5, SH-7.5, arcade.color.WHITE, 2)

# start of the drawing itself

# popsicle

# point lists for polygons
pop_side = [(150, 175), (130, 200), (130, 410), (150, 398)]

triangle_in_arc = [(250, 450), (150, 400), (350, 400)]

filled_arc = [(130, 410), (150, 400), (250, 450)]

arcade.draw_polygon_filled(triangle_in_arc, (167, 107, 207, 150))
arcade.draw_polygon_filled(filled_arc, (167, 107, 207, 200))
arcade.draw_polygon_filled(pop_side, (167, 107, 207, 200))

arcade.draw_lrtb_rectangle_filled(150, SW-150, 400, 175, (167, 107, 207, 200))
arcade.draw_lrtb_rectangle_outline(150, SW-150, 400, 175, arcade.color.BLACK, 2)

arcade.draw_arc_filled(230, 410, 200, 100, (167, 107, 207, 200), 0, 180)
arcade.draw_arc_outline(230, 410, 200, 100, arcade.color.BLACK, 0, 180, 3)
arcade.draw_circle_filled(320, 415, 15, (167, 107, 207, 200))

arcade.draw_arc_filled(250, 398, 200, 100, (167, 107, 207, 200), 0, 180)
arcade.draw_arc_outline(250, 398, 200, 100, arcade.color.BLACK, 0, 180, 3)

# outlines for polygons
arcade.draw_line(150, 175, 130, 200, arcade.color.BLACK, 2)
arcade.draw_line(130, 200, 130, 410, arcade.color.BLACK, 2)
arcade.draw_line(130, 410, 150, 398, arcade.color.BLACK, 2)
arcade.draw_line(150, 400, SW-150, 400, (167, 107, 207, 130))

# stick
arcade.draw_lrtb_rectangle_filled(225, 275, 175, 50, (166, 123, 91))
arcade.draw_lrtb_rectangle_outline(225, 275, 175, 50, arcade.color.BLACK, 2)

arcade.draw_arc_filled(250, 50, 50, 40, (166, 123, 91), -180, 0)
arcade.draw_arc_outline(250, 50, 50, 40, arcade.color.BLACK, -180, 0, 3)

arcade.draw_line(226, 50, 274, 50, (166, 123, 91), 2)

arcade.draw_rectangle_filled(265, 100, 8, 75, (192, 153, 153, 200))
arcade.draw_arc_filled(265, 137.5, 8, 8, (192, 153, 153, 200), 0, 180)
arcade.draw_arc_filled(265, 62.5, 8, 8, (192, 153, 153, 200), 0, 180, 180)
arcade.draw_circle_filled(265, 50, 4, (192, 153, 153, 200), 100)

# scene inside the popsicle

# moon
arcade.draw_circle_filled(290, 390, 35, (255, 204, 51, 215))
arcade.draw_circle_outline(290, 390, 35, arcade.color.BLACK)
arcade.draw_circle_filled(275, 395, 20, (167, 107, 207, 200))
arcade.draw_circle_outline(275, 395, 20, arcade.color.BLACK)

# land
arcade.draw_parabola_filled(151, 160, 349, 60, (10, 186, 181, 175))
arcade.draw_parabola_outline(150, 160, 350, 60, arcade.color.BLACK, 2)
arcade.draw_rectangle_filled(250, 198, 198, 45, (10, 186, 181, 175))

# cloud

for i in range(18):
    x = random.randint(210, 285)
    y = random.randint(340, 350)
    arcade.draw_circle_filled(x, y, 20, arcade.color.PERIWINKLE)

# rain drops
arcade.draw_circle_filled(250, 280, 6, (65, 125, 193, 175))
arcade.draw_arc_filled(250, 280, 12, 40, (65, 125, 193, 175), 0, 180)

arcade.draw_circle_filled(220, 290, 6, (65, 125, 193, 150))
arcade.draw_arc_filled(220, 290, 12, 40, (65, 125, 193, 175), 0, 180)

arcade.draw_circle_filled(280, 290, 6, (65, 125, 193, 175))
arcade.draw_arc_filled(280, 290, 12, 40, (65, 125, 193, 175), 0, 180)

# stars
for i in range(250):
    x = random.randint(150, 340)
    y = random.randint(175, 420)
    font_size = random.randint(4, 10)
    arcade.draw_text("*", x, y, arcade.color.ANTI_FLASH_WHITE, font_size)

# glare/reflections
arcade.draw_rectangle_filled(330, 300, 15, 160, (240, 255, 255, 200))
arcade.draw_arc_filled(330, 380, 15, 15, (240, 255, 255, 200), 0, 180)
arcade.draw_arc_filled(330, 220, 15, 15, (240, 255, 255, 200), 0, 180, 180)
arcade.draw_circle_filled(330, 200, 7.5, (240, 255, 255, 200))

arcade.draw_rectangle_filled(165, 230, 7.5, 80, (240, 255, 255, 200))
arcade.draw_arc_filled(165, 270, 7.5, 7.5, (240, 255, 255, 200), 0, 180)
arcade.draw_arc_filled(165, 190, 7.5, 7.5, (240, 255, 255, 200), 0, 180, 180)
arcade.draw_circle_filled(165, 285, 7.5/2, (240, 255, 255, 200), 0, 40)

arcade.finish_render()
arcade.run()
