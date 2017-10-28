# -*- coding: utf-8 -*-
# FileName: entertainment_center.py
# Creater: DiabloCC
# EMail: chh986212@126.com
# Git: https://github.com/DiabloCC

from media import movie, movie_list
import fresh_tomatoes


def build_movies():
  l = movie_list()
  m = movie('七宗罪',
            'http://g1.ykimg.com/0516000052FB46A86758394F330B8CA8',
            'http://v.youku.com/v_show/id_XMzU1ODI1MzA0')
  m.add_info(director='大卫·芬奇', 
             actors='布拉德·皮特/摩根·弗里曼',
             country='美国',
             year='1995',
             story_brief='每个人心中都有一颗罪恶的心')
  l.add_movie(m)
  
  m = movie('银翼杀手2049',
            'http://g2.ykimg.com/0516000059E99A16ADBC09A1A50613A3',
            'http://v.youku.com/v_show/id_XMzAyMzM2OTgyMA')
  m.add_info(country='美国',
             year='2017')
  l.add_movie(m)
	  
  m = movie('肖申克的救赎',
            'http://g4.ykimg.com/051600005355D7B167379F50CA08A983',
            'http://v.youku.com/v_show/id_XMzgzNjY2Njky')
  m.add_info(director='弗兰克·德拉邦特', 
             actors='蒂姆·罗宾斯 / 摩根·弗里曼',
             country='美国',
             year='1994',
             story_brief='永远不要习惯命运的不公，永远要保持希望。')
  l.add_movie(m)
  
  m = movie('羞羞的铁拳',
            'http://r1.ykimg.com/0516000059C4A70CADBC0904BF0E0A38',
            'http://v.youku.com/v_show/id_XMzA1MjQ0NzU5Mg')
  m.add_info(director='宋阳 / 张吃鱼', 
             actors='艾伦/马丽/沈腾/田雨',
             country='中国大陆',
             year='2017')
            
  l.add_movie(m)

  return l
  
if __name__ == '__main__':
  fresh_tomatoes.open_movies_page(build_movies().movies())
  
  
  
  