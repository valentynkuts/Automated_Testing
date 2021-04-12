package exercise;

import org.junit.Assert;
import org.junit.Test;
import exercise.CollectionHelp;

import java.util.*;


public class CollectionHelpTest {

    List<String> list0 = Arrays.asList("1", "2", "3", "10");
    List<String> list1 = Arrays.asList("1", "2", "3");
    List<String> list2 = Arrays.asList("4", "5", "6");

    @Test
    public void listNotEmptyReturnTrue() {
        Assert.assertTrue(CollectionHelp.isNotEmpty(list1));
    }

    @Test
    public void listIsSubcollectionReturnTrue() {
        Assert.assertTrue(CollectionHelp.inclusion(list1, list0));
        System.out.println(list2);
    }

    @Test
    public void unionTwoCollections() {
        Collection<String> union = CollectionHelp.unionCollections(list1, list2);

        Assert.assertTrue(union.contains("1"));
        Assert.assertTrue(union.contains("5"));
    }

    @Test
    public void intersectionCollectionsReturnTrueIfSize3() {
        Collection<String> intersection = CollectionHelp.intersectionCollections(list1, list0);
        Assert.assertTrue(intersection.size() == 3);
    }

}