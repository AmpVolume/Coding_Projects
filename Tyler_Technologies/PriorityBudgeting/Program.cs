Console.WriteLine("\nPriority-Based Budgeting System");
Console.WriteLine("-------------------------------");

Console.Write("Enter Program Name: ");
string programName = Console.ReadLine() ?? "";

Console.Write("Enter Annual Budget: ");
string annualBudgetInput = Console.ReadLine() ?? "";

Console.Write("Enter Amount Spent: ");
string amountSpentInput = Console.ReadLine() ?? "";


if (string.IsNullOrWhiteSpace(programName))
{
    Console.WriteLine("Invalid input. Program name cannot be empty. ");
}
else if (!decimal.TryParse(annualBudgetInput, out decimal annualBudget ))
{
    Console.WriteLine("Invalid input. Please enter a valid annual budget.");
}
else if (annualBudget <= 0)
{
    Console.WriteLine("Invalid input. Annual budget must be greater than zero.");
}
else if (!decimal.TryParse(amountSpentInput, out decimal amountSpent))
{
    Console.WriteLine("Invalid input. Please enter a valid amount spent.");
}
else if (amountSpent < 0)
{
    Console.WriteLine("Invalid input, Please enter a valid amount spent.");
}
else
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