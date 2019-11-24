import java.util.Scanner;

public class LastFactorialDigit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nInp = scanner.nextInt();
        for (int i = 0; i < nInp; i++){
            int nToFact = scanner.nextInt();
            int factorial = 1;
            for (int j = 1; j <= nToFact; ++j){
                factorial *= j;
            }
            System.out.println(factorial % 10);
        }
    }
}
