import java.util.Scanner;

//  - Leonidas is constantly asked about how many soldiers his 300 Spartans will face.
//
//   - Help Leonidas by creating a small guessing game in which the player must make a guess. If the guess is below or above the correct value, print appropriate messages informing the player.
//
//   - Correct value: 10,000
public class GuessingGame {
    public void play(){
        int guessNumber = 0;
        System.out.println("What is your guess about how many soldiers the 300 Spartans will face?");
        Scanner keyboard = new Scanner(System.in);

        while (guessNumber != 10000) {

            guessNumber = keyboard.nextInt();
            if (guessNumber == 10000) {
                System.out.println("Congratulations! You are right, the Spartans will face 10,000 Persians.");
            } else {
                System.out.println("Oh no! Your guess is incorrect! Try again!");
            }
        }

        keyboard.close();
    }
}
