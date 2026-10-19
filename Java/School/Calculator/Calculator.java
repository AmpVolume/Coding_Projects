package Calculator;

import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        boolean running = true;

        System.out.println("=== JAVA CALCULATOR ===");

        while (running) {

            // Get first number
            System.out.print("\nEnter first number: ");
            double num1 = scanner.nextDouble();

            // Get operator
            System.out.print("Enter operator (+, -, *, /): ");
            char operator = scanner.next().charAt(0);

            // Get second number
            System.out.print("Enter second number: ");
            double num2 = scanner.nextDouble();

            double result = 0;

            // Perform calculation
            switch (operator) {

                case '+':
                    result = num1 + num2;
                    break;

                case '-':
                    result = num1 - num2;
                    break;

                case '*':
                    result = num1 * num2;
                    break;

                case '/':

                    if (num2 != 0) {
                        result = num1 / num2;
                    } else {
                        System.out.println("Cannot divide by zero.");
                        continue;
                    }

                    break;

                default:
                    System.out.println("Invalid operator.");
                    continue;
            }

            // Display result
            System.out.println("Result: " + result);

            // Ask to continue
            System.out.print("\nDo another calculation? (y/n): ");

            char choice = scanner.next().charAt(0);

            if (choice != 'y' && choice != 'Y') {
                running = false;
            }
        }

        System.out.println("\nCalculator Closed.");

        scanner.close();
    }
}