package exercise;

import org.junit.Assert;
import org.junit.Test;
import exercise.ArraysStatistics;

public class ArraysStatisticsTest {
    @Test
    public void minusOneShouldBeTheBiggest(){
        Assert.assertEquals(-1, ArraysStatistics.max(new int[]{-10,-5,-1,-2,-13}));
    }

    @Test
    public void maximumShouldBe5(){
        Assert.assertEquals(5, ArraysStatistics.max(new int[]{1,2,5,3,-1,0}));

    }

    @Test
    public void minimumShouldNotBePositiveNumber(){
        Assert.assertEquals(-211, ArraysStatistics.min(new int[]{-10,-5,-1,-211,-13}));
    }

    @Test
    public void minimumShouldBe3(){
        Assert.assertEquals(3, ArraysStatistics.min(new int[]{100,28,85,32,3,10}));

    }

    @Test
    public void avgShouldBeNegativeNumber(){
        Assert.assertEquals(- 4.0, ArraysStatistics.avg(new int[]{-1,-1,-10,-4}),0.01);
    }

    @Test
    public void avgShouldBe3p0(){
        Assert.assertEquals(3.0, ArraysStatistics.avg(new int[]{3,3,3}),0.01);//3.99 i 3.98

    }

    @Test
    public void sumShouldBeNegativeNumber(){
        Assert.assertEquals(- 19, ArraysStatistics.sum(new int[]{-1,-1,-10,-4, -3}));
    }

    @Test
    public void sumShouldBe100(){
        Assert.assertEquals(100, ArraysStatistics.sum(new int[]{30,30,30,10}));

    }

}
