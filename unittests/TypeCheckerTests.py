# Copyright (c) 2010 Siddhu Warrier (http://siddhuwarrier.homelinux.org, 
# siddhuwarrier AT gmail DOT com). 
# 
# This file is part of the utils package.
# The utils package is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

## @brief Test cases for the decorator for type checking.
# 
# @author Siddhu Warrier (siddhuwarrier@gmail.com)
# @date 21/01/2010

import unittest
import sys

from TypeChecker import *

##@brief test function used to test the TypeChecker decorator.
@require(validKwargs = ["a", "b", "c"], \
             x = int, y = (int,), a = (int,), b = (int,), c = (int,))
def testFunction(x, y, **kwargs):
    print x+y

## @brief Test class to allow testing TypeChecker
# @author Siddhu Warrier (siddhuwarrier@gmail.com)
# @date 22/01/2010
class TestClass:
    ##@brief Test instance method used to test the TypeChecker decorator.
    #
    # The test function does nothing except implementing the decorator.
    # @date 22/01/2010
    @require(validKwargs = ["a", "b", "c"], \
             x = (int,), y = int, a = (int, float), b = (int,), c = (int, ))
    def testFunction(self, x, y, **kwargs):
        pass
    
## @brief Test case class that (success) tests on a function (not an instance method of a class)
# @author Siddhu Warrier (siddhuwarrier@gmail.com)
# @date 22/01/2010
class TypeSuccessTests_Function(unittest.TestCase):        
    ## @brief Tests the TypeChecker decorator if no keyword arguments are provided.
    #
    # This test case initialises testFunction with all of the required arguments
    # and none of the optional keyword arguments 
    # @date 22/01/2010
    def testNoOptionalKeywordArguments(self):
        try:
            testFunction(2, 3)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")

    ## @brief Tests the TypeChecker decorator if some keyword arguments are provided.
    #
    # This test case initialises testFunction with all of the required arguments
    # and some of the optional keyword arguments 
    # @date 22/01/2010
    def testSomeOptionalKeywordArguments(self):
        try:
            testFunction(1, 4,  a = 3)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")
            
    ## @brief Tests the TypeChecker decorator if even compulsory arguments are provided
    # as keyword arguments.
    #
    # This test case initialises testFunction with all of the required arguments
    # as keyword arguments (and some of the kwargs as well). 
    # @date 22/01/2010
    def testCompulsoryArgumentsAsKeywordArguments(self):
        try:
            testFunction(x = 1,y = 5, a = 3, b = 4, c = 5)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")        

    ## @brief Tests the TypeChecker decorator if all keyword arguments are provided.
    #
    # This test case initialises testFunction with all of the required arguments
    # *and* all of the optional keyword arguments 
    # @date 22/01/2010
    def testAllOptionalKeywordArguments(self):
        try:
            testFunction(1,3, a = 3, b = 4, c = 5)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")
            
## @brief Test case class that (success) tests on instance methods of classes.
# @author Siddhu Warrier (siddhuwarrier@gmail.com)
# @date 22/01/2010
class TypeSuccessTests_InstanceMethod(unittest.TestCase):
    
    def setUp(self):
        self.testClass = TestClass()
    
    ## @brief Tests the TypeChecker decorator if no keyword arguments are provided.
    #
    # This test case initialises the testFunction instance method with all of the required arguments
    # and none of the optional keyword arguments 
    # @date 22/01/2010
    def testNoOptionalKeywordArguments(self):
        try:
            self.testClass.testFunction(2, 3)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")

    ## @brief Tests the TypeChecker decorator if no keyword arguments are provided.
    #
    # This test case initialises the testFunction instance method with all of the
    #  required arguments and none of the optional keyword arguments 
    # @date 22/01/2010
    def testSomeOptionalKeywordArguments(self):
        try:
            self.testClass.testFunction(2, 3, a = 5)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")

    ## @brief Tests the TypeChecker decorator if even compulsory arguments are provided
    # as keyword arguments.
    #
    # This test case initialises testFunction with all of the required arguments
    # as keyword arguments (and some of the kwargs as well). 
    # @date 22/01/2010
    def testCompulsoryArgumentsAsKeywordArguments(self):
        try:
            self.testClass.testFunction(x = 1,y = 5, a = 3, b = 4, c = 5)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")            

    ## @brief Tests the TypeChecker decorator if all keyword arguments are provided.
    #
    # This test case initialises testFunction with all of the required arguments
    # *and* all of the optional keyword arguments 
    # @date 22/01/2010
    def testAllOptionalKeywordArguments(self):
        try:
            self.testClass.testFunction(1,3, a = 3, b = 4, c = 5)
        except Exception as error:
            self.fail("Exception" + str(error.args) + "raised.")

## @brief Test case class for failrue tests
# @author Siddhu Warrier (siddhuwarrier@gmail.com)
# @date 22/01/2010
class TypeFailureTest(unittest.TestCase):
    def testCompulsoryArgumentMissing(self):
        self.assertRaises(NameError, testFunction, 2);
    
    def testCompulsoryArgumentIncorrect(self):
        self.assertRaises(TypeError, testFunction, "x", 4);
    
    def testInvalidKeywordArguments(self):
        self.assertRaises(NameError, testFunction, 5, 4, superman=6);
    
    def testWrongTypeOfKeywordArguments(self):
        self.assertRaises(TypeError, testFunction, 5, 4, a="4");

## @brief Test suite for TypeChecker Success tests
def typeCheckerSuccessSuite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TypeSuccessTests_InstanceMethod)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TypeSuccessTests_Function))
    return suite

## @brief Test suite for TypeChecker Failure tests
def typeCheckerFailureSuite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TypeFailureTest)
    return suite

#Test harness
if __name__ == '__main__':
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    runner.run(typeCheckerSuccessSuite())
    runner.run(typeCheckerFailureSuite())