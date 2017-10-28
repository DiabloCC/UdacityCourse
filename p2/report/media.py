# -*- coding: utf-8 -*-
# FileName: media.py
# Creater: DiabloCC
# EMail: chh986212@126.com
# Git: https://github.com/DiabloCC

class movie():
  '''
  The movie class describes a movie in this demo project.
  Properties:
    1. id
    2. title
    3. post_url
    4. trailer_url
    5. other_info
  Methods:
    1. add_info
  '''
  
  def __init__(self, id, title, post, trailer):
    self.id = id
    self.title = title
    self.post_url = post
    self.trailer_url = trailer
    self.other_info = {}
    
class movie_list():
  '''
  The movie_list class maintains a list of movies.
  Properties:
    1. movies
  Methods:
    1. add_movie
    2. remove_movie
  '''
  
  def __init__(self):
    self.__movies = []
    
  def 