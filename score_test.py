import sys
import os

def score_test():
    cmd = 'perl score pku_training.utf8 pku_test_gold.utf8 test-info.txt.seg > score-info.txt'
    os.system(cmd)

def main():
    score_test()

if __name__ == '__main__':
    main()
    
