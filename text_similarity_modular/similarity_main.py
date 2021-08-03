# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/7/30

# 系统包

# 自定义包
from text_similarity_modular.basic_algorithm import *
from text_similarity_modular.synthesis_algorithm import *

def get_text_similarity(text_one, text_two, algorithm_type='COSINE', stopwords=[], **kwargs):
    """
    获取文本相似度
    :param text_one: 输入文本一
    :param text_two: 输入文本二
    :param algorithm_type: 所用算法类型，默认使用余弦相似度算法
        value:
            COSINE:余弦相似度算法
            JACCARD:杰卡德相似度算法
    :param stopwords: 停用词列表
    :param kwargs: 参数集合
        value:
            pinyin_conversion: 拼音转换开关，yes：转换成拼音后再进行匹配，no：原字符匹配（默认）
                可使用算法：
    :return:
    """
    similarity = 0.0
    try:
        if text_one is None or text_two is None or text_one == '' or text_two == '':
            similarity = 0.0
        elif text_one == text_two:
            similarity = 1.0

        else:
            if algorithm_type == 'COSINE':
                str_list1, str_list2 = text_processing_one(text_one, text_two, stopwords)
                similarity = cosine_similarity(str_list1, str_list2)
            elif algorithm_type == 'JACCARD':
                str_list1, str_list2 = text_processing_one(text_one, text_two, stopwords)
                similarity = jaccard_similarity(str_list1, str_list2)

    except Exception as e:
        raise e
    finally:
        return similarity


