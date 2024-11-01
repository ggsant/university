
// Exercise 1
//
// Obtain the standard input for weight (int) and height (double), then print the BMI (Body Mass Index).
//
// BMI = weight in kilograms divided by height in meters squared

import java.util.Scanner;

public class CalculateBmi {
    public void calculateBmi(){
        System.out.println("Enter your weight followed by your height to calculate your BMI");
        Scanner keyboard = new Scanner(System.in);

        int weight = keyboard.nextInt();
        double height = keyboard.nextDouble();

        double bmi = weight / (height * height);

        System.out.printf("The BMI is: %.2f ", bmi);

        keyboard.close();
    }
}
