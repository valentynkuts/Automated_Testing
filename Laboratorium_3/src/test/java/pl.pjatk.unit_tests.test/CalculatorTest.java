package pl.pjatk.unit_tests.test;

import org.junit.Assert;
import org.junit.Test;
import pl.pjatk.unit_tests.Calculator;

public class CalculatorTest {
    // ---- Lab 3 ----
    // prime numbers:
    // 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
    // 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
    // 137, 139, 149, 151, 157, ...
    @Test
    public void number139IsPrimeNum(){
        Assert.assertTrue(Calculator.isPrimeNum(139));
    }
    @Test
    public void number71IsPrimeNum(){
        Assert.assertTrue(Calculator.isPrimeNum(71));
    }
    @Test
    public void number1IsNotPrimeNum(){
        Assert.assertFalse(Calculator.isPrimeNum(1));
    }
    @Test
    public void number8IsNotPrimeNum(){
        Assert.assertFalse(Calculator.isPrimeNum(8));
    }
    // ---- Lab1 ----
    @Test
    public void fiveToTwoShouldReturn25(){
        Assert.assertEquals(25, Calculator.power(5,2));

    }

    @Test
    public void fiveToZeroShouldReturn1(){
        Assert.assertEquals(1,Calculator.power(5,0));

    }

    @Test
    public void nwd32and16return16(){
        Assert.assertEquals(16, Calculator.NWD(32,16));
    }

    @Test
    public void nwd100and30return10(){
        Assert.assertEquals(10, Calculator.NWD(100,30));

    }
    @Test
    public void isDivisible33pz11(){
        Assert.assertTrue(Calculator.isDivisible(33,11));
    }
    @Test
    public void isNotDivisible73pz0(){
        Assert.assertFalse(Calculator.isDivisible(73,0));
    }

}
