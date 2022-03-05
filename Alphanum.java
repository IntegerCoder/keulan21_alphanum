import java.util.*;

public class Alphanum {
    public static int phoneWord2Num(String word) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('a', 2);
        map.put('b', 2);
        map.put('c', 2);
        map.put('d', 3);
        map.put('e', 3);
        map.put('f', 3);
        map.put('g', 4);
        map.put('h', 4);
        map.put('i', 4);
        map.put('j', 5);
        map.put('k', 5);
        map.put('l', 5);
        map.put('m', 6);
        map.put('n', 6);
        map.put('o', 6);
        map.put('p', 7);
        map.put('q', 7);
        map.put('r', 7);
        map.put('s', 7);
        map.put('t', 8);
        map.put('u', 8);
        map.put('v', 8);
        map.put('w', 9);
        map.put('x', 9);
        map.put('y', 9);
        map.put('z', 9);

        int value = 0;
        for (int i = 0; i < 7; i++) {
            char ch = Character.toLowerCase(word.charAt(i));
            int digit = map.get(ch);
            value += digit * Math.pow(10, (6 - i));
        }
        return value;
    }

    public static void main(String[] args) {
        System.out.println(phoneWord2Num("FLOWERS"));
        System.out.println(phoneWord2Num("PrOGrAM"));
        System.out.println(phoneWord2Num("Battery"));
    }
}
