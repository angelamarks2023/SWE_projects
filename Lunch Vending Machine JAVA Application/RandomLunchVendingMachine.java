import java.util.Random;
import java.util.Scanner;

public class RandomLunchVendingMachine {
    public static void main(String[] args) {
        // Initialize the list of lunches
        String[] lunches = {"Ramen", "Burger", "Sushi", "Chicken Salad", "Sandwhiches"};
        
        //Create a random number generator
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        
        // Display a welcome messages and prompts a buyer to press the number ‘1’, '2' or ‘0’
        System.out.println("Welcome to the Random Lunch Vending Machine!");
        System.out.println("Options: ");
        System.out.println("1 - Get a random lunch");
        System.out.println("2 - View available lunches");
        System.out.println("0 - Exit");
        
        
        // Start the loop 
        while(true){
            System.out.print("Your choice: "); //Prompt a buyer to press the number '1' or '0'
            int choice = scanner.nextInt(); // Get buyer's input
            
            if(choice == 1){
                //Generate a random index to select a lunch
                int randomIndex = random.nextInt(lunches.length);
                //Display selected lunch 
                System.out.println("Your lunch: " + lunches[randomIndex]);
            }
            else if(choice == 0) {
                System.out.println("Thank you for using the lunch vending machine!");
                break;
                
            }
            else if(choice == 2) {
                System.out.println("Lunches serving today: ");
                for(String lunch: lunches) {
                    System.out.println("- " + lunch);
                }
            }
                
            else{
                //Handle invalid input
                System.out.println("Invalid choice. Please press '1', '2', or '0'");
            }
        }
        
        scanner.close();
        
    }
}