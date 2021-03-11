package pl.pjatk.unit_tests.test;

import org.junit.Assert;
import org.junit.Test;
import pl.pjatk.unit_tests.Mapdecoder;

import java.util.HashMap;

public class MapdecoderTest {
    @Test
    public void decodeShouldReturnNull(){
        String str = null;
        Assert.assertNull(Mapdecoder.decode(str));

    }

    @Test
    public void decodeShouldReturnMap(){
        Assert.assertTrue( Mapdecoder.decode("") instanceof HashMap);

    }

    @Test
    public void decodeShouldReturnEmptStrIfKeyEmpt(){
        Assert.assertTrue( "".equals(Mapdecoder.decode("=1&two=2")));

    }

    @Test
    public void decodeShouldReturnEmptStrIfValueEmpt(){
        Assert.assertTrue( "".equals(Mapdecoder.decode("one=1&two=")));

    }

    @Test
    public void show(){
        HashMap hm = (HashMap)Mapdecoder.decode("one=1&two=2");
        for (Object i : hm.keySet()) {
            System.out.println("key: " + i + " value: " + hm.get(i));
        }

    }

}
