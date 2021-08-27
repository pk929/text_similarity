# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/3

# 系统包

# 自定义包
from text_similarity_modular import *
from text_similarity_modular.common import *
from text_similarity_modular.basic_algorithm import *


content_x = '不要'
content_y = '不要开通'
textSimilarity = TextSimilarity()
ts = textSimilarity.get_text_similarity(content_x, content_y, algorithm_type="SHORT_TEXT", inclusion_relation=True, pinyin_conversion=True, cut_all=False, similarity_threshold='0.7')
print(ts)

# import jieba
#
# print([i for i in jieba.cut(content_x, cut_all=True)])
# print(jieba.lcut(content_x, cut_all=True))


