package exercise;

import org.junit.Assert;
import org.junit.Test;
import exercise.StringUtils;

public class StringUtilsTest {

    // ---- Lab 3 ----
    @Test
    public void strOfNumToAverageReturnDouble() {
        Assert.assertEquals(2.5, StringUtils.strOfNumToAverage("1,2,3,4"), 0.01);
    }

    @Test
    public void strOfNumToAverageReturn00() {
        Assert.assertEquals(0.0, StringUtils.strOfNumToAverage("1,2,3,X"), 0.01);
    }

    @Test
    public void strOfNumToAverageReturnDouble0() {
        Assert.assertEquals(0.0, StringUtils.strOfNumToAverage(""), 0.01);
    }

    @Test
    public void strOfNumToAverageReturn0() {
        Assert.assertEquals(0.0, StringUtils.strOfNumToAverage("num"), 0.01);
    }

    // ---- Lab 1 ----
    @Test
    public void ala_ma_kotaReturnALA_MA_KOTA() {
        Assert.assertEquals("ALA_MA_KOTA", StringUtils.toUpperCase("ala_ma_kota"));
    }

    @Test
    public void strIsPolindrom() {
        Assert.assertEquals(true, StringUtils.polindrom("qwelewq"));
    }

    @Test
    public void agaIsPolindrom() {
        Assert.assertEquals(true, StringUtils.polindrom("aga"));
    }

    @Test
    public void strIsNotPolindrom() {
        Assert.assertEquals(false, StringUtils.polindrom("A kilku tu klika"));
    }

    @Test
    public void sumOfDigits52Return7() {
        Assert.assertEquals(7, StringUtils.sumOfDigits("52"));
    }

    @Test
    public void sumOfDigits884Return20() {
        Assert.assertEquals(20, StringUtils.sumOfDigits("884"));
    }

}
