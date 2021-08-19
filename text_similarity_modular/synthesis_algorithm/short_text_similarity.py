# -*- ecoding: utf-8 -*-
# @Function: <短文本相似度算法>
# @Author: pkuokuo
# @Time: 2021/8/4

# 系统包
from xpinyin import Pinyin

# 自定义包
from text_similarity_modular.common.utils import *
from text_similarity_modular.basic_algorithm import *

pinyin = Pinyin()


def short_text_sim(str_input1, str_input2, stopwords, **kwargs):
    """
    短文本相似度计算
    :param str_input1: 文本一
    :param str_input2: 文本二
    :param stopwords: 停用词列表
    :param kwargs: 自定义参数
        inclusion_relation：包含关系匹配开关
        pinyin_conversion：拼音转换开关
        similarity_threshold：相似度阀值
    :return:
    """
    inclusion_relation = kwargs.get('inclusion_relation')  # 包含关系匹配开关
    pinyin_conversion = kwargs.get('pinyin_conversion')  # 拼音开关
    similarity_threshold = kwargs.get('similarity_threshold')  # 相似度阀值

    similarity_threshold = (float(similarity_threshold) if similarity_threshold is not None else 0.7) * 1.2

    max_similarity = 0.0
    str_list2 = text_processing_one(str_input2, stopwords, **kwargs)
    if inclusion_relation:
        '判断是否包含'
        isInclude = is_included(included_text=str_input1, text=str_list2)
        if isInclude:
            max_similarity = similarity_threshold

    if pinyin_conversion:
        text_pin1 = pinyin.get_pinyin(str_input1)
        text_pin2 = pinyin.get_pinyin(str_input2)

        # 文本处理
        str_list_pin1 = text_processing_one(text_pin1, stopwords, **kwargs)
        str_list_pin2 = text_processing_one(text_pin2, stopwords, **kwargs)
        similarity_cosine = cosine_sim(str_list_pin1, str_list_pin2)
        similarity_jaccard = jaccard_sim(str_list_pin1, str_list_pin2)
        if similarity_cosine >= max_similarity and similarity_cosine >= similarity_jaccard:
            max_similarity = similarity_cosine
        elif similarity_jaccard >= max_similarity and similarity_jaccard > similarity_cosine:
            max_similarity = similarity_jaccard

    else:
        # 文本处理
        str_list1 = text_processing_one(str_input1, stopwords, **kwargs)
        similarity_cosine = cosine_sim(str_list1, str_list2)
        similarity_jaccard = jaccard_sim(str_list1, str_list2)
        if similarity_cosine >= max_similarity and similarity_cosine >= similarity_jaccard:
            max_similarity = similarity_cosine
        elif similarity_jaccard >= max_similarity and similarity_jaccard > similarity_cosine:
            max_similarity = similarity_jaccard

    return max_similarity
