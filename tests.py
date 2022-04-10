import pytest
import Calc
import mySelenium

def testAdd():
    assert Calc.add(3,5)

def testSubstruc():
    assert Calc.substruc(3,5)

def testMultiply():
    assert Calc.multiply(3,8)

def testDivide():
    assert Calc.divide(3,0)
    assert Calc.divide(8,2)

def testDiveideEvenlly():
    assert Calc.diveideEvenlly(3,5)
    assert Calc.diveideEvenlly(4,4)

def testMudolo():
    assert Calc.mudolo(3,5)
    assert Calc.mudolo(45,0)

def testSqrt():
    assert Calc.sqrt(9)
    assert Calc.sqrt(0)

def testSelenium():
    assert mySelenium.openYTB()


