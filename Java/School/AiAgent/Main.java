package AiAgent;

import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // ---------------- MEMORY ----------------
        String userName = null;
        Map<String, String> preferences = new HashMap<>();
        List<String> chatHistory = new ArrayList<>();

        System.out.println("AI Agent: Hello! I am your assistant. Type 'exit' to quit.");

        while (true) {

            System.out.print("You: ");
            String input = scanner.nextLine().trim();
            String lowerInput = input.toLowerCase();

            // Store ALL inputs
            chatHistory.add(input);

            // ---------------- EXIT ----------------
            if (lowerInput.equals("exit")) {
                System.out.println("AI Agent: Goodbye " + (userName != null ? userName : "friend") + "!");
                break;
            }

            // ---------------- NAME MEMORY ----------------
            if (lowerInput.startsWith("my name is ")) {
                userName = input.substring(11);
                System.out.println("AI Agent: Nice to meet you, " + userName + "!");
                continue;
            }

            if (lowerInput.equals("what is my name")) {
                System.out.println("AI Agent: Your name is " + (userName != null ? userName : "unknown"));
                continue;
            }

            // ---------------- PREFERENCES ----------------
            if (lowerInput.contains("i like ")) {
                String pref = input.substring(lowerInput.indexOf("i like ") + 7);
                preferences.put(pref, "like");
                System.out.println("AI Agent: Got it, you like " + pref);
                continue;
            }

            if (lowerInput.equals("what do i like")) {
                if (preferences.isEmpty()) {
                    System.out.println("AI Agent: I don't know yet.");
                } else {
                    System.out.println("AI Agent: You like:");
                    for (String key : preferences.keySet()) {
                        System.out.println("- " + key);
                    }
                }
                continue;
            }

            // ---------------- CHAT RESPONSE ----------------
            if (lowerInput.contains("hello")) {
                System.out.println("AI Agent: Hey " + (userName != null ? userName : "there") + "!");
            }
            else if (lowerInput.contains("how are you")) {
                System.out.println("AI Agent: I'm running smoothly!");
            }
            else if (lowerInput.contains("history")) {
                System.out.println("AI Agent: You said:");
                for (String msg : chatHistory) {
                    System.out.println("- " + msg);
                }
            }
            else {
                System.out.println("AI Agent: I’m not sure yet, but I’m learning.");
            }
        }

        scanner.close();
    }
}