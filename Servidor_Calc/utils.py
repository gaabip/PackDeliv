#!/usr/bin/python3.5
"""Library for utilities functions for the calc server"""

class LatLng:
    """Class for use with coordinates"""
    def __init__(self, lat, lng):
        self.__lat = int(lat)
        self.__lng = int(lng)
    
    def get_lat(self):
        return self.__lat
    def get_lng(self):
        return self.__lng