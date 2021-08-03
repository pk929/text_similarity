# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/7/30

# 系统包
import jieba


# 自定义包

def text_processing_one(text_one, text_two, stopwords):
    """
    文本处理一：对传入文本进行分词、去除停用词处理
    :param text_one: 文本一
    :param text_two: 文本二
    :param stopwords: 停用词
    :return:
    """
    # 分词
    str_list1 = jieba.lcut(text_one)
    str_list2 = jieba.lcut(text_two)
    # 去除停用词
    str_list1 = move_stopwords(str_list1, stopwords)
    str_list2 = move_stopwords(str_list2, stopwords)
    return str_list1, str_list2


def is_included(text_one=None, text_two=None):
    """
    全包含关系匹配，匹配main_str中是是否包含有secondary_str
    :param text_one: 字符串1
    :param text_two: 字符串2
    :return:
    """
    flag = False
    try:
        if text_one in text_two or text_two in text_one:
            flag = True
    except Exception as e:
        raise e
    finally:
        return flag


def move_stopwords(sentence, stopwords):
    """
    对句子去除停用词
    :param sentence: 原有句子词集合
    :param stopwords: 停用词集合
    :return:
    """
    santi_words = sentence
    try:
        santi_words = [x for x in sentence if len(x) > 0 and x not in stopwords]
    except Exception as e:
        raise e
    finally:
        return santi_words
