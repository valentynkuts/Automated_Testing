package exercise;

public class Calculator {
     // ---- Lab 3 ----
     public static boolean isPrimeNum(int number) {
         boolean isItPrime = true;
         if (number <= 1) {
             isItPrime = false;
             return isItPrime;
         } else {
             for (int i = 2; i <= number / 2; i++) {
                 if (number % i == 0) {
                     isItPrime = false;
                     break;
                 }
             }
             return isItPrime;
         }
     }

    // ---- Lab 1 ----
    public static long power(int a, int b) {
        if (a >= 0 && b >= 0) {
            if (b == 0)
                return 1;
            else if (b % 2 == 1)
                return power(a, b - 1) * a;
            else
                return power(a * a, b / 2);
        }
        return -1;
    }

    public static int NWD(int a, int b){
        if(b == 0)
            return a;
        return NWD(b, a%b);
    }

    public static boolean isDivisible(int a, int b){
        if(b == 0)
            return false;
        else if(a % b == 0)
            return true;
        else
            return false;
    }
}
