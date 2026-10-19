
string programName = "Road Maintenance";

decimal annualBudget = 250000m;
decimal amountSpent = 180000m;

decimal remainingBudget = annualBudget - amountSpent;

Console.WriteLine("Priority-Based Budgeting System");
Console.WriteLine("-------------------------------");
Console.WriteLine($"Program: {programName}");
Console.WriteLine($"Annual Budget: ${annualBudget:N2}");
Console.WriteLine($"Amount Spent: ${amountSpent:N2}");
Console.WriteLine($"Remaining Budget: ${remainingBudget:N2}");

if (amountSpent > annualBudget)
{
    Console.WriteLine("WARNING: The program is over budget!");
}
else
{
    Console.WriteLine("Status: Within budget.");
}