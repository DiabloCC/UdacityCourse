# -*- coding: utf-8 -*-
# FileName: media.py
# Creater: DiabloCC
# EMail: chh986212@126.com
# Git: https://github.com/DiabloCC

class movie(object):
  '''
  The movie class describes a movie in this demo project.
  Properties:
    1. title
    2. poster_url
    3. trailer_url
    4. other_info
  Methods:
    1. add_info
  '''
  
  def __init__(self, title, post, trailer):
    self.title = title
    self.poster_url = post
    self.trailer_url = trailer
    self.other_info = {'director':'', 'actors':'', 'year':'', 'story_brief':'', 'country':''}
  
  def add_info(self, **kw):
    for key,value in kw.items():
      if key in self.other_info:
        self.other_info[key] = value
      else:
        # field not found
        return -1


class movie_list(object):
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
    
  def movies(self):
    '''
    Make the hidden list visible.
    '''
    return self.__movies

  def add_movie(self, movie):
    '''
    Append new movie object to list
    '''
    if not movie.title in self.__index:
      self.__movies.append(movie)
      self.__index[movie.title] = len(self.__movies)-1
      return 0
    else:
      # already in list
      return -2
    
  def __locate(self, title):
    if title in self.__index:
      return self.__index[title]
    else:
      return -3

  def remove_movie(self, title):
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

  def edit_movie(self, title, field, value):
    id = __locate(title)
    if id < 0:
      return id
    else:
      if hasattr(self.__movies[id], field):
        setattr(self.__movies[id], field, value)
      else:
        if field in self.__movies[id].other_info:
          self.__movies[id].other_info[field] = value
        else:
          # field not found
          return -4
