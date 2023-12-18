'''
PYCASSO PROJECT
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

# By Matthew Avis for CSP

# Importing arcade module
import arcade
import math

class application(arcade.Window):
    def __init__(self):
        super().__init__(800,800, "Matthew Avis")  # Make 800x800 Window
        self.pointList = []  # List of points to build the shape
        self.a = 0  # Incrementing value that spins the shape
        self.color = [155,255,255]
        self.colorMod = 0

    def on_draw(self):
        arcade.start_render()

        # /// BACKGROUND ///

        arcade.set_background_color((255,192,203 + self.colorMod))
        square_amt = 10
        for j in range(0,square_amt):
            for i in range(0,square_amt):
                arcade.draw_point(((i+0.5)/square_amt) * 800, ((j+0.5)/square_amt) * 800, arcade.color.WHITE, abs(math.sin(self.a*5+j/10)*50))

        # /// ROTATING SHAPE ///

        point_amt = abs(math.sin(self.a*2)*8) + 1  # Amount of points to draw

        for i in range(0,int(point_amt)):  # Uses sin() & cos() modulation to create a circling effect
            x_cord = math.sin((self.a + i/point_amt) * math.pi * 2) * 200 + 400  # X Modulation
            y_cord = math.cos((self.a + i/point_amt) * math.pi * 2) * 80 + 300  # Y Modulation
            self.pointList.append([x_cord, y_cord])  # Add to shape list

        arcade.draw_polygon_outline(self.pointList,self.color,5)  # Bottom face of the shape using the point list

        for i in self.pointList:  # Incrementing the Y coordinate to stack the shape on top
            i[1] += 200

        arcade.draw_polygon_outline(self.pointList,self.color,5)  # Top face of the shape using the point list

        for i in self.pointList:
            arcade.draw_polygon_outline((i,(i[0],i[1]-200)),self.color,5)  # Connect them together

        self.pointList.clear()  # Clearing the calculation

    def update(self, d_time):
        self.a += 0.005  # Incrementing the input value of the function
        self.colorMod = int(math.sin(self.a * 20) * 50)  # Color modulation
        self.color = [0, 0, 0]


newWindow = application()
newWindow.run()
