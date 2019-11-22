import java.util.Scanner;

public class HangingTerrace {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputs = scanner.nextLine();
        String[] inputSplit = inputs.split(" ");
        int tMax = Integer.parseInt(inputSplit[0]);
        int e = Integer.parseInt(inputSplit[1]);
        int curr = 0;
        int deniedGroups = 0;

        for (int i = 0; i < e; i++){
            String gMove = scanner.nextLine();
            String[] gMoveSplit = gMove.split(" ");
            int gCount = Integer.parseInt(gMoveSplit[1]);
            if (gMoveSplit[0].equals("enter")){
                if ((curr + gCount) <= tMax){
                    curr += gCount;
                }
                else{
                    deniedGroups += 1;
                }
            }
            else{
                curr -= gCount;
            }
        }
        System.out.println(deniedGroups);
    }
}
