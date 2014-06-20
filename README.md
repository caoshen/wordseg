#WordSeg

Chinese Word Segmentation using [CRF++][link1].

**简介**

WordSeg 是一个中文分词工具。

中文分词 (Chinese Word Segmentation)指的是将一个汉字序列切分成一个一个单独的词。分词就是将连续的字序列按照一定的规范重新组合成词序列的过程。

现有的分词算法可分为三大类：基于字符串匹配的分词方法、基于理解的分词方法和基于统计的分词方法。按照是否与词性标注过程相结合，又可以分为单纯分词方法和分词与标注相结合的一体化方法。

WordSeg 属于基于统计的字标注分词方法。

**字标注**

字标注（以字分词），就是把分词视为字的词位分类问题。字的构词位置（词位）： 词首B、词位E、词中M、单字词S。比如对于分词：上海/计划/到/本/世纪/ 末/实现/人均/国内/生产/总值/五千美元/。 可以标注为：上/B海/E计/B 划/E到/S本/S世/B纪/E末/S/实/B现/E人/B均/E国/B内/E生/B产/E总/B/值/ E五/B千/M美/M元/E。/S

**CRF**

CRF （Conditional Random Field）条件随机域：
条件随机域模型是由 Lafferty 在2001年提出的一种典型的判别式模型。它在观测序列的基础上对目标序列进行建模,重点解决序列化标注的问题。

CRF++ （Yet Another CRF toolkit）是一个实现 CRF 的开源工具包，主要用来分词和序列标注。

**准备数据（data）**

* pku_training.utf8: 训练数据
* pku_test.utf8: 测试数据
* pku_test_gold.utf8: 对比数据

**WordSeg 工作流程**

对训练集进行字标注以及编写模板后使用CRF++工具，学习得到相应model，然后使用model对测试集自动标注，最后根据标好的字得到分词结果。

**WordSeg 使用方法**

```
python tag.py pku_training.utf8
python tag.py pku_test.utf8
python crf_exec.py
python seg.py test-info.txt
python score_test.py
```

1. 字标注训练数据和测试数据 (Training and Test file formats)
2. crf++ 训练模型 (Preparing feature templates & Training (encoding))，标注测试集 Testing (decoding)
3. 标注文件转化为分词结果 (Get segmentation)
4. 评测 (F1 score of result)

**分词效果**

召回率 0.972，准确率 0.942，f值 0.956。 see score-info.txt

```
=== TOTAL TRUE WORD COUNT:	104372
=== TOTAL TEST WORD COUNT:	102545
=== TOTAL TRUE WORDS RECALL:	0.972
=== TOTAL TEST WORDS PRECISION:	0.942
=== F MEASURE:	0.956
```

**Tools and Data**

[CRF++][link1]

[Data sets & Scoring script][link2]

[link1]:http://crfpp.googlecode.com/svn/trunk/doc/index.html

[link2]:http://sighan.cs.uchicago.edu/bakeoff2005/


