# -*- ecoding: utf-8 -*-
# @Function: <基于关键词的余弦相似度算法>
# @Author: pkuokuo
# @Time: 2021/8/5

# 系统包
import os
import jieba
import jieba.analyse
from sklearn.metrics.pairwise import cosine_similarity

# 自定义包


def keyword_cosine_sim(text_one, text_two, stopWord_path, **kwargs):
    """
    余弦相似度算法
        对语句先设置停用词，再提取关键词列表，然后根据交集、并集产生词向量，最后计算两个向量的余弦值。
    :param text_one: 文本一
    :param text_two: 文本二
    :param stopWord_path:
    :param kwargs: 自定义参数
        cut_all: jieba分词模式开关，默认为False
    :return:
    """
    cut_all = kwargs.get('cut_all')  # 全分词开关
    cut_all = True if cut_all is True or cut_all == 'True' else False

    # 设置停用词
    if os.path.exists(stopWord_path):
        jieba.analyse.set_stop_words(stopWord_path)

    # 切割
    text_one_seg_list = jieba.lcut(text_one, cut_all=cut_all)
    text_two_seg_list = jieba.lcut(text_two, cut_all=cut_all)

    # 提取关键词
    text_one_keyword_list = jieba.analyse.extract_tags("|".join(text_one_seg_list), topK=200, withWeight=False)
    text_two_keyword_list = jieba.analyse.extract_tags("|".join(text_two_seg_list), topK=200, withWeight=False)

    # 词的并集
    union = set(text_one_keyword_list).union(set(text_two_keyword_list))
    # 编码
    word_dict = {}
    i = 0
    for word in union:
        word_dict[word] = i
        i += 1
    # oneHot编码
    s1_cut_code = __one_hot(word_dict, text_one_keyword_list)
    s2_cut_code = __one_hot(word_dict, text_two_keyword_list)

    # 余弦相似度计算
    sample = [s1_cut_code, s2_cut_code]
    # 除零处理
    try:
        sim = cosine_similarity(sample)
        return sim[1][0]

    except Exception as e:
        raise e


def __one_hot(word_dict, keywords):  # oneHot编码
    # cut_code = [word_dict[word] for word in keywords]
    cut_code = [0] * len(word_dict)
    for word in keywords:
        cut_code[word_dict[word]] += 1
    return cut_code
