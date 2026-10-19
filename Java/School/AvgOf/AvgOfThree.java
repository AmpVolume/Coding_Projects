/**
* @author: Duncan Doyon
* @course: F91PD Programming and Program Design
* @date: 2024-06-10
* @description: This program calculates the average of three numbers entered by the user.
* @version: 1.0
**/

package AvgOf;

import java.util.Scanner;

public class AvgOfThree {
    public static void main(String[] args) {
        
        //-----------------------Input-----------------------//
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);
        
        // Prompt the user to enter first number
        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();
        
        // Prompt the user to enter second number
        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();
        
        // Prompt the user to enter third number
        System.out.print("Enter the third number: ");
        double num3 = scanner.nextDouble();
        
        //-----------------Processing-----------------//
        // Calculate the average of the three numbers
        double average = (num1 + num2 + num3) / 3;
        
        //-----------------Output-----------------//
        // Display the average to the user
        System.out.println("The average of the three numbers is: " + average);
        
        //-----------------Cleanup-----------------//
        // Close the scanner
        scanner.close();
    }
}