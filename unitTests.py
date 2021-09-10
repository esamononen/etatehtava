import unittest

import tehtava

class MyTestCase(unittest.TestCase):
    def testParameterValidation(self):
        ## The first argument is a random pattern consisting of characters S and T. For example 'STTTS'.
        with self.assertRaises(TypeError) as cm:
            tehtava.validateInput("STASTSSSTT", "1")
        self.assertEqual(tehtava.sampleProgram.characterError, str(cm.exception))

        # The following arguments are N (N >= 1) number of integers. For example 1 5 8. Each integer is
        # separated from previous one with a space.
        with self.assertRaises(TypeError) as cm:
            tehtava.validateInput("ST", "1 ")
        self.assertEqual(tehtava.sampleProgram.numberError, str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            tehtava.validateInput("ST", "1 0")
        self.assertEqual(tehtava.sampleProgram.numberError, str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            tehtava.validateInput("ST", "1 ")
        self.assertEqual(tehtava.sampleProgram.numberError, str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            tehtava.validateInput("ST", " ")
        self.assertEqual(tehtava.sampleProgram.numberError, str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            tehtava.validateInput("ST", "-1")
        self.assertEqual(tehtava.sampleProgram.numberError, str(cm.exception))

    def testSingleLine(self):
        self.assertEqual("Soft", tehtava.getSingleLine("ST", 1))

        self.assertEqual("Soft, Tough, Soft and Soft", tehtava.getSingleLine("STS", 4))


if __name__ == '__main__':
    unittest.main()
