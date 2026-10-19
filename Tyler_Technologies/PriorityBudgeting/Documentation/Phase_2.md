Console.WriteLine("\nPriority-Based Budgeting System");
Console.WriteLine("-------------------------------");

Console.Write("Enter Program Name: ");
string programName = Console.ReadLine() ?? "";

Console.Write("Enter Annual Budget: ");
string annualBudgetInput = Console.ReadLine() ?? "";

Console.Write("Enter Amount Spent: ");
string amountSpentInput = Console.ReadLine() ?? "";


if (decimal.TryParse(annualBudgetInput, out decimal annualBudget) &&
    decimal.TryParse(amountSpentInput, out decimal amountSpent))
{
    decimal remainingBudget = annualBudget - amountSpent;

    Console.WriteLine("-------------------------------");
    Console.WriteLine($"Program: {programName}");
    Console.WriteLine($"Annual Budget: ${annualBudget:N2}");
    Console.WriteLine($"Amount Spent: ${amountSpent:N2}");
    Console.WriteLine($"Remaining Budget: ${remainingBudget:N2}");
    
    if(amountSpent > annualBudget)
    {
    Console.WriteLine("WARNING: The program is over budget!");
    }
    else
    {
    Console.WriteLine($"Status: Within budget.");
    }
}
else
{
    Console.WriteLine("-------------------------------");
    Console.WriteLine("Invalid input. Please enter valid numbers for the budget and amount spent.");
}