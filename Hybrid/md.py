class Univ():

    def __init__(self,):
        self._enginetype = ""
        self._speed = int()
        self._color = ""

    def set_enginetype(self, enginetype):
        self._enginetype = enginetype

    def set_speed(self,speed):
        self._speed = speed
    
    def set_color(self,color):
        self._color = color

    def get_enginetype(self):
        return self._enginetype        

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color
    