package pl.pjatk.unit_tests;

import java.util.Arrays;
import java.util.OptionalDouble;


public class StringUtils {

    // ---- Lab 3 ----
    public static double strOfNumToAverage(String strNumbers) {
        if (strNumbers != null && !strNumbers.isBlank()) {
            try {
                OptionalDouble aver = Arrays.stream(strNumbers.split(",")).mapToInt((s) -> Integer.parseInt(s)).average();
                return aver.getAsDouble();
            } catch (NumberFormatException nfe) {
                System.out.println("No sequence of numbers");
            }
        }
        System.out.println("No parameters to count");
        return 0.0;
    }

    // ---- Lab 1 ----

    public static String toUpperCase(String str) {
        return str.toUpperCase();
    }

    public static boolean polindrom(String str) {
        String reverse = "";
        for (int i = str.length() - 1; i >= 0; i--) {
            reverse = reverse + str.charAt(i);
        }
        if (str.equals(reverse))
            return true;
        return false;
    }

    public static int sumOfDigits(String num) {
        int number = Integer.parseInt(num);
        int digit = 0;
        int Sum = 0;
        while (number > 0) {
            digit = number % 10;
            Sum = Sum + digit;
            number = number / 10;
        }
        return Sum;
    }

}
