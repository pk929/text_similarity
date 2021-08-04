# -*- ecoding: utf-8 -*-
# @Function: <短文本相似度算法>
# @Author: pkuokuo
# @Time: 2021/8/4

# 系统包

# 自定义包
from text_similarity_modular.common.utils import *
from text_similarity_modular.basic_algorithm import *


def short_text_sim(str_input1, str_input2, stopwords, **kwargs):
    """
    短文本相似度计算
    :param str_input1: 文本一
    :param str_input2: 文本二
    :param stopwords: 停用词列表
    :param kwargs: 自定义参数
        inclusion_relation：包含关系匹配开关
    :return:
    """
    inclusion_relation = kwargs.get('inclusion_relation')  # 包含关系匹配开关

    if inclusion_relation == 'yes':
        isInclude = is_included(included_text=str_input1, text=str_input2)
        if isInclude:
            return 1.0

    # 文本处理
    str_list1, str_list2 = text_processing_one(str_input1, str_input2, stopwords)

    similarity_cosine = cosine_sim(str_list1, str_list2)
    similarity_jaccard = jaccard_sim(str_list1, str_list2)
    if similarity_cosine >= similarity_jaccard:
        return similarity_cosine
    else:
        return similarity_jaccard
