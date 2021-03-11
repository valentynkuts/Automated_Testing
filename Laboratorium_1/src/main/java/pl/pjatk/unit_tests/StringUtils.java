package pl.pjatk.unit_tests;

public class StringUtils {

    public static String toUpperCase(String str){
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
