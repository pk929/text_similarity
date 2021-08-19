# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/7/30

# 系统包
import os
import jieba


# 自定义包
def text_processing_one(text, stopwords, **kwargs):
    """
    文本处理一：对传入文本进行添加自定义词库、分词、去除停用词处理
    :param text: 文本
    :param stopwords: 停用词
    :param kwargs:
    :return:
    """
    cut_all = kwargs.get('cut_all')  # 全分词开关
    cut_all = True if cut_all is True or cut_all == 'True' else False
    # 分词
    str_list = jieba.lcut(text, cut_all=cut_all)
    # 去除停用词
    str_list1 = move_stopwords(str_list, stopwords)
    return str_list1


# def text_processing_one(text_one, text_two, stopwords, **kwargs):
#     """
#     文本处理一：对传入文本进行添加自定义词库、分词、去除停用词处理
#     :param text_one: 文本一
#     :param text_two: 文本二
#     :param stopwords: 停用词
#     :return:
#     """
#     cut_all = kwargs.get('cut_all')  # 全分词开关
#     cut_all = True if cut_all is True or cut_all == 'True' else False
#
#     # 分词
#     str_list1 = jieba.lcut(text_one, cut_all=cut_all)
#     str_list2 = jieba.lcut(text_two, cut_all=cut_all)
#     # 去除停用词
#     str_list1 = move_stopwords(str_list1, stopwords)
#     str_list2 = move_stopwords(str_list2, stopwords)
#     return str_list1, str_list2


def is_included(included_text=None, text=None):
    """
    全包含关系匹配，匹配text中是否含有included_text
    :param included_text: 被包含文本
    :param text: 包含文本
    :return:
    """
    flag = False
    try:
        if included_text in text:
            flag = True
    except Exception as e:
        raise e
    finally:
        return flag


def read_words(file_path):
    """
    按行读取文本
    :param file_path: 文件路径
    :return:
    """
    words = []
    try:
        words = [line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()]
    except Exception as e:
        raise e
    finally:
        return words


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
