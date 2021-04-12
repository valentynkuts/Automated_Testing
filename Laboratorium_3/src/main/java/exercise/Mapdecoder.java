package exercise;

import java.util.HashMap;

public class Mapdecoder {

    public static Object decode(String str) throws IllegalArgumentException{

        if (str == null) {
            return null;
        }
        HashMap<String, String> hm = new HashMap<>();
        if (str.isEmpty()) {
            return hm;
        }
        String[] splitted = str.split("&");


        if(!(str instanceof String)){
            throw new IllegalArgumentException();
        }
        String[] temp;
        for (String s : splitted) {
            temp = s.split("=");
            if ((temp.length < 2) || temp[0].isEmpty()) {
                return "";
            } else{
               hm.put(temp[0], temp[1]);
            }
        }

        return hm;
    }


}
