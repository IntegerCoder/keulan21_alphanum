public class AlphanumSwitchEnhanced {
    public static int phoneWord2Num(String word) {
        int value = 0;
        for (int i = 0; i < 7; i++) {
            char ch = Character.toLowerCase(word.charAt(i));
            int digit;
            switch (ch) {
                case 'a', 'b', 'c' -> digit = 2;
                case 'd', 'e', 'f' -> digit = 3;
                case 'g', 'h', 'i' -> digit = 4;
                case 'j', 'k', 'l' -> digit = 5;
                case 'm', 'n', 'o' -> digit = 6;
                case 'p', 'q', 'r', 's' -> digit = 7;
                case 't', 'u', 'v' -> digit = 8;
                case 'w', 'x', 'y', 'z' -> digit = 9;
                default ->
                    throw new IllegalArgumentException(
                            "The input word must contain only the English alphabet.");
            }
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
