import arcade

SW = 600
SH = 600


class FrontSide:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, lw, dx, dy, col):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.lw = lw
        self.dx = dx
        self.dy = dy
        self.col = col

    def draw_side(self):
        arcade.draw_polygon_outline(((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3),
                                     (self.x4, self.y4)), self.col, self.lw)

    def update_side(self):
        self.x3 -= self.dx
        self.x4 -= self.dx

        self.y1 += self.dy
        self.y2 += self.dy

        if self.x3 > 500 or self.x3 < 100:
            self.dx *= -1
        if self.x1 < 100 or self.x1 > 500:
            self.dx *= -1
        if self.y2 < 400 or self.y1 > 300:
            self.dy *= -1


class BackSide:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, lw, dx, dy, col):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.lw = lw
        self.dx = dx
        self.dy = dy
        self.col = col

    def draw_side(self):
        arcade.draw_polygon_outline(((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3),
                                     (self.x4, self.y4)), self.col, self.lw)

    def update_side(self):
        self.x1 -= self.dx
        self.x2 -= self.dx

        self.y3 -= self.dy
        self.y4 -= self.dy

        if self.x3 > 500 or self.x3 < 100:
            self.dx *= -1
        if self.x1 < 100 or self.x1 > 500:
            self.dx *= -1
        if self.y3 > 300 or self.y4 < 400:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BYZANTIUM)

        self.side_1 = FrontSide(300, 200, 300, 400, 100, 450, 100, 250, 6, 3, .75, arcade.color.BLACK)
        self.side_2 = FrontSide(300, 200, 300, 400, 500, 450, 500, 250, 6, 3, .75, arcade.color.BLACK)
        self.side_3 = BackSide(100, 450, 100, 250, 300, 300, 300, 500, 6, 3, .75, arcade.color.BLACK)
        self.side_4 = BackSide(500, 450, 500, 250, 300, 300, 300, 500, 6, 3, .75, arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for i in range(0, SW, 40):
            arcade.draw_line(i, 0, i, SH, (143, 188, 143, 200), 6)
        for i in range(0, SH, 40):
            arcade.draw_line(0, i, SW, i, (143, 188, 143, 200), 6)
        arcade.draw_rectangle_outline(300, 300, SW, SH, arcade.color.DARK_SLATE_BLUE, 10)
        self.side_1.draw_side()
        self.side_2.draw_side()
        self.side_3.draw_side()
        self.side_4.draw_side()

    def on_update(self, dt):
        pass
        self.side_1.update_side()
        self.side_2.update_side()
        self.side_3.update_side()
        self.side_4.update_side()


def main():
    window = MyGame(SW, SH, "cool")
    arcade.run()


if __name__ == "__main__":
    main()
