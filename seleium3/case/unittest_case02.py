# coding=utf-8
import unittest


class FistCase02(unittest.TestCase):
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

    def testfirst001(self):
        print("***001***")

    def testfirst002(self):
        print("***002***")

    @unittest.skip('不执行的case')
    def testfirst003(self):
        print("***003***不执行的")


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FistCase01("testfirst002"))
    # suite.addTest(FistCase01("testfirst001"))
    # unittest.TextTestRunner().run(suite)
