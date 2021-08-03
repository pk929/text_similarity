# -*- ecoding: utf-8 -*-
# @Function: <杰卡德相似度算法>
# @Author: pkuokuo
# @Time: 2021/7/30

# 系统包
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import jieba

# 自定义包
from text_similarity_modular.common import *


def jaccard_similarity(str_list1, str_list2):
    """
    计算杰卡德相似度
    :param str_list1: 句一列表
    :param str_list2: 句二列表
    :return:
    """
    # 将字中间加入空格
    s1, s2 = __add_space(str_list1), __add_space(str_list2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator


def __add_space(s):
    return ' '.join(list(s))


def __add_space_pinyin(s):
    return ' '.join(s.split("-"))
