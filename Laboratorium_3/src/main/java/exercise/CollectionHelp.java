package exercise;

import org.apache.commons.collections4.CollectionUtils;

import java.util.*;

public class CollectionHelp {

    public static boolean isNotEmpty(List list) {
        boolean isNotEmpty = (list != null && list.size() > 0);
        return isNotEmpty;
    }

    public static boolean inclusion(List list1, List list2) {
        return CollectionUtils.isSubCollection(list1, list2);
    }

    public static Collection unionCollections(List list1, List list2) {
        return CollectionUtils.union(list1, list2);
    }

    public static Collection intersectionCollections(List list1, List list2) {
        return CollectionUtils.intersection(list1, list2);
    }

}
