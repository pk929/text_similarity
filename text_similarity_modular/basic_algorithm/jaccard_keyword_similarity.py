# -*- ecoding: utf-8 -*-
# @Function: <基于关键词的杰卡德相似度算法>
# @Author: pkuokuo
# @Time: 2021/8/5

# 系统包
import jieba
import jieba.analyse
import os

# 自定义包


def keyword_jaccard_sim(text_one, text_two, stopWord_path, **kwargs):
    """
    基于关键词的杰卡德相似度算法
        对语句先设置停用词，再提取关键词列表，然后根据交集、并集计算两个列表的杰卡德相似度。
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

    # jaccard相似度计算
    intersection = len(list(set(text_one_keyword_list).intersection(set(text_two_keyword_list))))
    union = len(list(set(text_one_keyword_list).union(set(text_two_keyword_list))))
    # 除零处理
    sim = float(intersection)/union if union != 0 else 0
    return sim

