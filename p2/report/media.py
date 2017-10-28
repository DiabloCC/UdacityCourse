# -*- coding: utf-8 -*-
# FileName: media.py
# Creater: DiabloCC
# EMail: chh986212@126.com
# Git: https://github.com/DiabloCC

class movie():
  '''
  The movie class describes a movie in this demo project.
  Properties:
    1. title
    2. post_url
    3. trailer_url
    4. other_info
  Methods:
    1. add_info
  '''
  
  def __init__(self, title, post, trailer):
    self.title = title
    self.post_url = post
    self.trailer_url = trailer
    self.other_info = {'direcor':'', 'actors':'', 'year':'', 'story_brief':'', 'country':''}
  def add_info(field, value):
    if not self.other_info.get(field):
      self.other_info[field] = value
    else:
      return "couldn't find the info field named '%s'." % (field)


class movie_list():
  '''
  The movie_list class maintains a list of movies.
  Properties:
    1. movies
  Methods:
    1. add_movie
    2. remove_movie
    3. edit_movie
  '''
  
  def __init__(self):
    self.__movies = []
    # index of movie titles
    self.__index = {}
    
  def movies():
    '''
    Make the hidden list visible.
    '''
    return __movies

  def add_movie(movie):
    '''
    Append new movie object to list
    '''
    if not movie.title in self.__index:
      self.__movies.append(movie)
      self.__index[movie.title] = len(self.__movies)-1
      return 0
    else:
      # already in list
      return -1
    
  def __locate(title):
    if title in self.__index:
      return self.__index[title]
    else:
      return -2

  def remove_movie(title):
    id = __locate(title)
    if id < 0:
      # movie not found
      return id
    else:
      self.__movies.pop(id)
      self.__index.pop(title)
      # update indexes
      for t,idx in self.__index:
        if idx > id:
           self.__index[t] = idx - 1

  def edit_movie(title, field, value):
    id = __locate(title)
    if id < 0:
      return -2
    else:
      self.__movies[id]
