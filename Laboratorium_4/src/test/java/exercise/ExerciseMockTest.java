package exercise;

import org.junit.Assert;
import org.junit.Test;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import org.mockito.MockedStatic;
import org.mockito.Mockito;
import static org.mockito.BDDMockito.*;

public class ExerciseMockTest {
    int[] numbers = new int[]{};

    @Test
    public void example1() {
        Calculator calc = mock(Calculator.class);
        when(calc.powerForMock(2, 2)).thenReturn(2L);
        long b = calc.powerForMock(2, 2);
        Assert.assertEquals(2, b);
    }

    @Test
    public void example1a() {
        Calculator calc = mock(Calculator.class);
        given(calc.powerForMock(2, 2)).willReturn(8L);
        long b = calc.powerForMock(2, 2);
        Assert.assertEquals(8, b);
    }

    @Test
    public void example2() {

        try (MockedStatic<Calculator> utilities = Mockito.mockStatic(Calculator.class)) {
            utilities.when(() -> Calculator.power(2, 6))
                    .thenReturn(10L);
            Assert.assertEquals(10L, Calculator.power(2, 6));
        }
    }

    @Test
    public void example3() {
        Calculator calc = mock(Calculator.class);
        when(calc.return1234()).thenReturn(2);
        int b = calc.return1234();
        Assert.assertEquals(2, b);
    }

    @Test
    public void example3a() {
        Calculator calc = mock(Calculator.class);
        given(calc.return1234()).willReturn(100);
        int b = calc.return1234();
        Assert.assertEquals(100, b);
    }

    @Test
    public void example4() {
        try (MockedStatic<ArraysStatistics> utilities = Mockito.mockStatic(ArraysStatistics.class)) {
            utilities.when(() -> ArraysStatistics.min(numbers))
                    .thenReturn(345);
            Assert.assertEquals(345, ArraysStatistics.min(numbers));
        }
    }

    @Test
    public void example4a() {
        ArraysStatistics as = mock(ArraysStatistics.class);
        when(as.minForMock(numbers)).thenReturn(2);
        Assert.assertEquals(2, as.minForMock(numbers));
    }

    @Test
    public void example4b() {
        ArraysStatistics as = mock(ArraysStatistics.class);
        given(as.minForMock(numbers)).willReturn(11);
        Assert.assertEquals(11, as.minForMock(numbers));
    }

}
