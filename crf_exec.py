# -*- coding:utf-8 -*-

import codecs
import sys
import os

# options of crf_leaern:

# -c float: 
# With this option, you can change the hyper-parameter for the CRFs.
# With larger C value, CRF tends to overfit to the give training corpus.
# This parameter trades the balance between overfitting and underfitting.
# The results will significantly be influenced by this parameter.
# You can find an optimal value by using held-out data or more general model selection method such as cross validation.

# -f NUM:
# This parameter sets the cut-off threshold for the features.
# CRF++ uses the features that occurs no less than NUM times in the given training data.
# The default value is 1.
# When you apply CRF++ to large data,
# the number of unique features would amount to several millions.
# This option is useful in such cases.

# -p NUM:
# If the PC has multiple CPUs,
# you can make the training faster by using multi-threading.
# NUM is the number of threads.

def crf_exec():
    cmd_learn = 'crf_learn -c 5 -p 128 template pku_training.utf8.data model > train-info.txt'
    cmd_test = 'crf_test -m model pku_test.utf8.data > test-info.txt'
    os.system(cmd_learn)
    os.system(cmd_test)

def main():
    crf_exec()

if __name__ == '__main__':
    main()
