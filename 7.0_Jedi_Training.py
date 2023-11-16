# 7.0 Jedi Training (20pts)  Name:Caleb Little

'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
SH = 400
SW = 500
arcade.open_window(SW, SH, "Caleb Little Jedi Training 7")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

# vertical lines for grid
for i in range(20, SW, 20):
    arcade.draw_line(i, 0, i, SH, arcade.color.BLACK)
# horizontal lines for grid
for i in range(20, SH, 20):
    arcade.draw_line(0, i, SW, i, arcade.color.BLACK)
# Upper left rectangle
arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)
# center tilted rectangle
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
# filled circle
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
# ellipse
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
# text
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20, 200)
# red point lower right
arcade.draw_point(460, 10, arcade.color.RED, 5)
# pac-man/arc upper right
arcade.draw_arc_filled(405, 320, 110, 120, arcade.color.YELLOW, 30, 330)

arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.finish_render()

arcade.run()


'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
# A = 260
# E = A*0.054
# G = A*0.063
# arcade.open_window(A*1.9, A, "The Stars and Stripes")
# arcade.start_render()
# arcade.draw_lrtb_rectangle_filled(0, A*1.9, A, 0, arcade.color.WHITE)
# arcade.draw_rectangle_outline(A*1.9/2, A/2, A*1.9, A, arcade.color.BLACK)
# y = 0
# for i in range(7):
#     arcade.draw_lrtb_rectangle_filled(0, A*1.9, A*1/13+y, y, (191, 10, 48))
#     i += 1
#     y += A*1/13*2
#
# arcade.draw_lrtb_rectangle_filled(0, A*0.76+G/2, A, A-A*0.5385, (0, 40, 104))
#
# y = A-A*0.5385
# for i in range(5):
#     x = G
#     for j in range(6):
#         arcade.draw_text("*", x, y, arcade.color.WHITE, 20)
#         x += G*2
#     y += A*0.5385/5
#
# y = A-A*0.5385+E
# for k in range(4):
#     x = G*2
#     for j in range(5):
#         arcade.draw_text("*", x, y, arcade.color.WHITE, 20)
#         x += G*2
#     y += A * 0.5385/5
# arcade.finish_render()
# arcade.run()




