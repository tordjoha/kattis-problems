import java.util.Scanner;

public class Bijele {
    public static void main(String[] args) {
        Scanner scanner = new Scanner((System.in));
        String piecesIn = scanner.nextLine();
        String[] pieces = piecesIn.split(" ");

        int king = Integer.parseInt(pieces[0]);
        king = 1 - king;

        int queen = Integer.parseInt(pieces[1]);
        queen = 1 - queen;

        int rook = Integer.parseInt(pieces[2]);
        rook = 2 - rook;

        int bishop = Integer.parseInt(pieces[3]);
        bishop = 2 - bishop;

        int knight = Integer.parseInt(pieces[4]);
        knight = 2 - knight;

        int pawn = Integer.parseInt(pieces[5]);
        pawn = 8 - pawn;

        System.out.println(king + " " + queen + " " + rook + " " + bishop + " " + knight + " " + pawn);
    }
}
