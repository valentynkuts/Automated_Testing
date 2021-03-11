package pl.pjatk.unit_tests.test;

import org.junit.Assert;
import org.junit.Test;
import pl.pjatk.unit_tests.Calculator;

public class CalculatorTest {
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
