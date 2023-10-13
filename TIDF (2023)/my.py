import jieba
from jieba.analyse import tfidf

with open("task5data.txt", "r", encoding='GBK') as f:
    data = f.read()

    # 以句号为单位，把每句话分离出来做准备
    juzi = [sentence.strip() for sentence in data.split('。') if sentence.strip()]

    # 分词处理
    fenci = list(jieba.cut(data))

    # 关键词句
    keywords = tfidf(data, withWeight=True)

    # 创建个字典，为后续的排序做准备
    sentence_keywords = {}

    # 开始遍历关键词和权重
    for keyword, weight in keywords:
        sentence_tfidf = 0  # 初始化关键词的权重
        for i, sentence in enumerate(juzi):  # 开始遍历句子
            if keyword in sentence:  # 如果关键词在句子中，则把权重加入句子中
                sentence_tfidf += weight

                sentence_keywords[sentence] = sentence_tfidf  # 字典

    sorted_sentences = sorted(sentence_keywords.items(), key=lambda x: x[1], reverse=True)  # 排序字典

    summary_sentences = [sentence for sentence, _ in sorted_sentences[:3]]  # 输出权值前三的句子

    summary = "\n".join(summary_sentences)  # 分割
    print(summary)
