#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
    '''class constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width=width
        self.height=height
        self.x=x
        self.y=y
    @property
         def width(self)
    return self.__width
    @width.setter
             def width(self,value):
                 self.validate_integer("width",value,False)
                 self.__width=value
     @property
         def height(self)
             return self.__height
             @height.setter
                 def height(self,value):
                     self.validate_integer("height",value,False)
                     self.__heigth=value
     @property
         def x(self)
             return self.__x
             @x.setter
                 def x(self,value):
                     self.validate_integer("x",value)
                     self.__x=value
     @property
         def y(self)
             return self.__y
             @y.setter
                 def y(self,value):
                     self.validate_integer("y",value)
                     self.__y=value
    def validate_integer(self,name,value,eq=True):
        if type(value)!=int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value<=0:
            raise ValueError("{} must be >0".format(name))
        elif not eq and value<=0:
            raise ValueError("{} must be >=0".format(name))
    def area(self):
        return self.width*self.height
    def display(self):
        for _ in range(self.y):
            print()
        for _ in range (self.height)
        print (' '*self.x +'#' * self.width)
    def _str_(self):
        return '[{}] ({}) {}/{} ' .\
         format (type(self)._name_,self.id,self.x,self.y,self.width,self.height)
    def update(self, *args **kwargs):
        if args is not None and len(args) is not 0:
            list _attributes=['id','width','height','x','y']
            for i in range (len(args)):
                set attributes(self,list_attributes[i],args[i])
            else:
             for key ,values in kwargs.items():
                 set attributes(self,key,values) 
    def to_dictionary(self):
        list attributes=['id','width','height','x','y']
        dict_res={}

        for key in list_attributes:
            dict_res[key]=getattributes(self,key)
            return dict_res
