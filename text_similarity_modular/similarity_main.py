# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/7/30

# 系统包
import os

# 自定义包
from text_similarity_modular.basic_algorithm import *
from text_similarity_modular.synthesis_algorithm import *

project_path = os.path.dirname(__file__)


class TextSimilarity(object):
    def __init__(self, stopWord_path=None, customWord_path=None):
        """
        初始化文本相似度计算类，
        加载停用词词库与自定义词词库，不传则使用默认停用词词库路径、自定义词词库路径
        :param stopWord_path: 停用词路径
        :param customWord_path: 自定义词库路径
        """
        self.stopwords = []
        if stopWord_path is None:
            self.stopWord_path = project_path + os.path.sep + 'date/stopWord.txt'
        else:
            self.stopWord_path = stopWord_path
        if customWord_path is None:
            self.customWord_path = project_path + os.path.sep + 'date/customWord.txt'
        else:
            self.customWord_path = customWord_path

        if os.path.exists(self.stopWord_path):
            self.stopwords = read_words(self.stopWord_path)
        if os.path.exists(self.customWord_path):
            jieba.load_userdict(self.customWord_path)

    def get_text_similarity(self, text_one, text_two, algorithm_type='COSINE', **kwargs):
        """
        获取文本相似度
        :param text_one: 输入文本一
        :param text_two: 输入文本二
        :param algorithm_type: 所用算法类型，默认使用余弦相似度算法
            value:
                COSINE:余弦相似度算法
                JACCARD:杰卡德相似度算法

                SHORT_TEXT:短文本相似度算法
                VOICE_TO_SHORT_TEXT:语音转文字短文本相似度算法
        :param kwargs: 参数集合
            value:
                inclusion_relation: 包含关系匹配开关。yes：开启，no：关闭（默认）
                    注意：只判断文本二中是否包含了文本一。
                    可使用算法：
                        SHORT_TEXT
                        VOICE_TO_SHORT_TEXT
                pinyin_conversion: 拼音转换开关。yes：转换成拼音后再进行匹配，no：原字符匹配（默认）
                    可使用算法：
                        VOICE_TO_SHORT_TEXT
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
                    str_list1, str_list2 = text_processing_one(text_one, text_two, self.stopwords)
                    similarity = cosine_sim(str_list1, str_list2)

                elif algorithm_type == 'JACCARD':
                    str_list1, str_list2 = text_processing_one(text_one, text_two, self.stopwords)
                    similarity = jaccard_sim(str_list1, str_list2)

                elif algorithm_type == 'SHORT_TEXT':
                    similarity = short_text_sim(text_one, text_two, self.stopwords,  **kwargs)

                elif algorithm_type == 'VOICE_TO_SHORT_TEXT':
                    similarity = voice_to_short_text_sim(text_one, text_two, **kwargs)

        except Exception as e:
            print(str(e))
            raise e
        finally:
            return similarity
