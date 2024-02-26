#!/usr/bin/python3
""" Module that contains class Base """
import json
import csv
import os.path


class Base:
        """ Class Base """
            __nb_objects = 0

                def _init_(self, id=None):
                            """ Initializes instances """
                                    if id is not None):
                   
                                        Base.__nb_objects += 1
self.id = Base.__nb_objects

