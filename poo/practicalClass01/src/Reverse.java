//Exercise 3
//
// Read a sequence of N strings and print them in reverse order. Use a method.

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Reverse {
    public void reverseString(){
        Scanner keyboard = new Scanner(System.in);

        ArrayList<String> names = new ArrayList<>();

        System.out.println("Enter the number of names: ");
        int quantity = keyboard.nextInt();

        String name;
        for (int i = 0; i < quantity; i++) {
            System.out.format("Enter the %d name: ", i + 1);
            name = keyboard.next();
            names.add(name);
        }

        System.out.println("\nNames in reverse order:");
        /*for (int i = quantity - 1; i > 0; i--) {
            System.out.println(names.get(i));
        }*/

        Collections.reverse(names);
        System.out.println(names);

        keyboard.close();
    }
}
