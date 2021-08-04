# -*- ecoding: utf-8 -*-
# @Function: <语音转文字短文本相似度算法>
# @Author: pkuokuo
# @Time: 2021/8/4

# 系统包

# 自定义包
from text_similarity_modular.common.utils import *
from text_similarity_modular.basic_algorithm import *


def voice_to_short_text_sim(str_input1, str_input2, **kwargs):
    """
    语音转文字短文本相似度计算
    :param str_input1: 文本一
    :param str_input2: 文本二
    :return:
    """
    inclusion_relation = kwargs.get('inclusion_relation')  # 包含关系匹配开关
    pinyin_conversion = kwargs.get('pinyin_conversion')  # 拼音开关

    if pinyin_conversion == 'yes':
        ''

    if inclusion_relation == 'yes':
        isInclude = is_included(included_text=str_input1, text=str_input2)
        if isInclude:
            return 1.0

    # 文本处理

