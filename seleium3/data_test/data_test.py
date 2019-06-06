# conding=utf-8
import ddt
import unittest


@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这是setUp")

    def tearDown(self):
        print('这是tearDown')

    def test01(self):
        print(90)
    #
    @ddt.data(
        [1, 2],
        [3, 4]
    )

    @ddt.unpack
    def test_add(self,a,b):
        print(a + b)


if __name__ == '__main__':
    unittest.main()
