#!/usr/bin/python3
""" New class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherist from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    def _str_(self):
        """ str special method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def _str_(self):
        """ str special method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size
def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attributes[i] == 'size':
                    setattributes(self, 'width', args[i])
                    setattributes(self, 'height', args[i])
                else:
                    setattributes(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattributes(self, 'width', value)
                    setattributes(self, 'height', value)
                else:
                    setattributes(self, key, value)

def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_attributes = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_attributes:
            if key == 'size':
                dict_res[key] = getattributes(self, 'width')
            else:
                dict_res[key] = getattributes(self, key)


                return  dict_res