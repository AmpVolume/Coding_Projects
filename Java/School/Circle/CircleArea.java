package Circle;
import java.util.Scanner;

public class CircleArea {
    public static void main(String[] args) {
        
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);
        
        // Prompt the user to enter the radius of the circle
        System.out.print("Enter the radius of the circle: ");
        double radius = scanner.nextDouble(); // Read the radius from user input
        
        // Calculate the area of the circle using the formula A = πr^2
        double areaOfCircle = Math.PI * Math.pow(radius, 2);
        
        // Display the result
        System.out.println("The area of the circle with radius " + radius + " is: " + areaOfCircle);
        
        // Close the scanner to prevent resource leaks
        scanner.close();

    }
    
}
