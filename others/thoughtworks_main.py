import unittest
from others.thoughtworks import *

class TestProcess(unittest.TestCase):
    # 测试处理例子数据: 例子1
    def test_normal_case1(self):
        text = "The main theme of education in engineering school is learning to teach yourself"
        expect_result = "The(1); (1);main(1); (1);theme(1); (1);of(1); (1);education(1); (1);in(1); (2);engineering(2); (2);school(2); (2);is(2); (2);learning(2,3); (3);to(3); (3);teach(3); (3);yourself(3);"
        print( "input: \n" + text)
        print("output: \n" + process(text, 30))
        self.assertEquals(process(text,30), expect_result)

    # 测试处理例子数据: 例子2，包含多个连续空格
    def test_normal_case2(self):
        text = "So   many whitespaces"
        expect_result = "So(1);   (1);many(1); (1);whitespaces(2,3);"
        print( "input: \n" + text)
        print("output: \n" + process(text, 10))
        self.assertEquals(process(text,10), expect_result)

    # 测试处理例子数据: 例子3， 一个单词跨越多行
    def test_normal_case3(self):
        text = "So   many whitespaceswhitespaceswhitespaces"
        expect_result = "So(1);   (1);many(1); (1);whitespaceswhitespaceswhitespaces(2,3,4,5);"
        print( "input: \n" + text)
        print("output: \n" + process(text, 10))
        self.assertEquals(process(text,10), expect_result)

    # 测试处理例子数据: 例子4， 有大量连续的空格
    def test_normal_case4(self):
        text = "So                         many whitespaceswhitespaceswhitespaces"
        expect_result = "So(1);                         (1,2,3);many(3,4); (4);whitespaceswhitespaceswhitespaces(4,5,6,7);"
        print( "input: \n" + text)
        print("output: \n" + process(text, 10))
        self.assertEquals(process(text,10), expect_result)

    # 测试异常： 包含异常字符
    def test_abnormal_input_character(self):
        text = "The main theme of educatio,bn"
        expect_result = "ERROR: Invalid character detected!"
        print( "input: \n" + text)
        print("output: \n" + process(text, 30))
        self.assertEquals(process(text,30), expect_result)

    # 测试异常： 包含异常字符
    def test_abnormal_input_range_1(self):
        text = "The main theme of educatiobn"
        expect_result = "ERROR: Width out of range!"
        print( "input: \n" + text)
        print("output: \n" + process(text, 8))
        self.assertEquals(process(text,8), expect_result)

    # 测试异常： 包含异常字符
    def test_abnormal_input_range_2(self):
        text = "The main theme of educatiobn"
        expect_result = "ERROR: Width out of range!"
        print( "input: \n" + text)
        print("output: \n" + process(text, 82))
        self.assertEquals(process(text,82), expect_result)