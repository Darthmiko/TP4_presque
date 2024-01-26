#créé par Enzo Sanchez Valero et Mikolai Szychowski
#créé le 10\01\24
#TP4


import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle():
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color


    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
           de votre jeu à l'écran.
        """


        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)
        #arcade.draw_circle_filled()


    def update(self, cercle_change_x, cercle_change_y, cercle_x, cercle_y, rayon):


        self.x += cercle_change_x
        self.y += cercle_change_y
        cercle_x += 3
        cercle_y += 3
        cercle_change_x = 3
        cercle_change_y = 3

        if self.x < rayon:
            pass
        if self.x > SCREEN_WIDTH - rayon:
            pass
        if self.y < rayon:
            pass
        if self.y > SCREEN_HEIGHT - rayon:
            pass
        if self.x < rayon:
            self.x *= -1


class Rectangle():
    def __init__(self, x, y, change_x, change_y, width_rectangle, height_rectangle, color, float):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color
        self.width_rectangle = width_rectangle
        self.height_rectangle = height_rectangle
        self.float = float
    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
           de votre jeu à l'écran.
        """

        arcade.draw_rectangle_filled(self.x, self.y, self.width_rectangle, self.height_rectangle, self.color)




class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.liste_balle = []
            self.liste_rectangle = []


        def setup(self):

            pass

        def on_update(self, delta_time: float):
            pass

        def on_draw(self):

            arcade.start_render()
            arcade.draw_circle_filled(self.c_x, self.c_y, 50, arcade.color.GREEN, 20)
            arcade.draw_rectangle_filled(self.c_x, self.c_y, 50, arcade.color.BLUE, 20)


        def on_update(self, delta_time):
            self.c_x += self.x_speed + delta_time
            self.c_x += self.x_speed + delta_time

            if self.c_x > 300 - 50 or self.c_x < 0 + 50:
                self.x_speed += -1
            if self.c_y > 720 - 50 or self.c_y < 0:
                self.y_speed += -1

            for i in self.liste_balle:
                i.on_draw(arcade.color.BLUE)
                i.on_draw(arcade.color.RED)
                i.on_draw(arcade.color.GREEN)

            for i in self.liste_rectangle:
                i.on_draw(arcade.color.BLUE)
                i.on_draw(arcade.color.RED)
                i.on_draw(arcade.color.GREEN)

        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            if button == arcade.MOUSE_BUTTON_LEFT:
                ball = Balle(x, y, random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), COLOR[random.randint(0, 3)])
                self.liste_balle.append(ball)
            if button == arcade.MOUSE_BUTTON_RIGHT:
                rectangle = Rectangle(x, y, random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), COLOR[random.randint(0, 3)])
                self.liste_rectangle.append(rectangle)



def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()