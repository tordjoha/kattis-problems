import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

/***
 * @author tordjohansson
 */
public class BeenEverywhereMan {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numTestCases = scanner.nextInt();
        for (int i = 0; i < numTestCases; i++){

            int numCities = scanner.nextInt();
            ArrayList cityList = new ArrayList(numCities);
            for (int j = 0; j <= numCities; j++){
                String city = scanner.nextLine();
                cityList.add(city);
            }

            HashSet<String> distinctCities = new HashSet<String>(cityList);
            System.out.println(distinctCities.size()-1);
            cityList.clear(); //clears the list for next case
        }
    }
}
