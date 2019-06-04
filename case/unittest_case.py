# coding=utf-8
import unittest


class FistCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('-------------------全局的前置-------------------')

    @classmethod
    def tearDownClass(cls):
        print('-------------------全局的后置-------------------')

    def setUp(self):
        print('---前置---')

    def tearDown(self):
        print('--*后置*--')

    def testfirst01(self):
        print("***01***")

    def testfirst02(self):
        print("***02***")

    @unittest.skip('不执行的case')
    def testfirst03(self):
        print("***03***不执行的")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FistCase01("testfirst02"))
    # suite.addTest(FistCase01("testfirst01"))
    # unittest.TextTestRunner().run(suite)
