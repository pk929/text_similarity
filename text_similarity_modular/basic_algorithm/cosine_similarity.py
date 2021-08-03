# -*- ecoding: utf-8 -*-
# @Function: <余弦相似度算法>
# @Author: pkuokuo
# @Time: 2021/7/30

# 系统包
from collections import Counter
import jieba
import jieba.analyse
import numpy as np

# 自定义包
from text_similarity_modular.common import *


def cosine_similarity(str_list1, str_list2):
    """
    计算余弦相似度
    :param str_list1: 句一列表
    :param str_list2: 句二列表
    :return:
    """
    # 初始化计数器
    co_str1 = (Counter(str_list1))
    co_str2 = (Counter(str_list2))
    p_str1 = []
    p_str2 = []
    for temp in set(str_list1 + str_list2):
        p_str1.append(co_str1[temp])
        p_str2.append(co_str2[temp])
    p_str1 = np.array(p_str1)
    p_str2 = np.array(p_str2)
    result = p_str1.dot(p_str2) / (np.sqrt(p_str1.dot(p_str1)) * np.sqrt(p_str2.dot(p_str2)))
    return round(result, 3)
