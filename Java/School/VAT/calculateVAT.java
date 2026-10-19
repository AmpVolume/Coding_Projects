package VAT;

public class calculateVAT {

    public static void main(String[] args) {

        // VAT rate is 12%
        final double VAT_RATE = 0.12;

        // Input amount
        double amount = 100.0;

        // Calculate sales tax
        double salesTax = amount * VAT_RATE;

        // Display result
        System.out.println("Sales Tax: " + salesTax);
    }
}