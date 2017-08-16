import  unittest, my_math
import profile
from subprocess import Popen, PIPE
from my_math import Count

class MathTestCase(unittest.TestCase):

    def setUp(self):
        self.count = 1

    def testTable(self):
        a = [1, 2, 3]
        p = my_math.Count(a)
        self.failUnless(p == len(a))

    def testNum(self):
        a = 1
        p = my_math.Count(a)
        self.failUnless(p == 0)

    def tearDown(self):
        self.count += 1
        print self.count

    # # subprocess moudule to call checker
    # def testWithPyChecker(self):
    #     cmd = 'pychecker', '-Q', my_math.__file__.rstrip('c')
    #     pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
    #     self.assertEqual(pychecker.stdout.read(),'')

if __name__ == '__main__':
    # unit test case
    unittest.main()
    # profile test
    # profile.run('Count([1,2,3,4,5])')
