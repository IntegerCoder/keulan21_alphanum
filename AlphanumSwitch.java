public class AlphanumSwitch {
    public static int phoneWord2Num(String word) {
        int value = 0;
        for (int i = 0; i < 7; i++) {
            char ch = Character.toLowerCase(word.charAt(i));
            int digit;
            switch (ch) {
                case 'a':
                case 'b':
                case 'c':
                    digit = 2;
                    break;
                case 'd':
                case 'e':
                case 'f':
                    digit = 3;
                    break;
                case 'g':
                case 'h':
                case 'i':
                    digit = 4;
                    break;
                case 'j':
                case 'k':
                case 'l':
                    digit = 5;
                    break;
                case 'm':
                case 'n':
                case 'o':
                    digit = 6;
                    break;
                case 'p':
                case 'q':
                case 'r':
                case 's':
                    digit = 7;
                    break;
                case 't':
                case 'u':
                case 'v':
                    digit = 8;
                    break;
                case 'w':
                case 'x':
                case 'y':
                case 'z':
                    digit = 9;
                    break;
                default:
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
