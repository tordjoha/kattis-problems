import java.util.Scanner;

/***
 * @author tordjohansson
 */
public class Faktor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String numInputs = scanner.nextLine();
        String[] numArray = numInputs.split(" ");
        int numArt = Integer.parseInt(numArray[0]);
        int impFactor = Integer.parseInt(numArray[1]);
        int sciToBribe = numArt * (impFactor - 1) + 1;
        System.out.println(sciToBribe);
    }
}
