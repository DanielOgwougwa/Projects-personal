import java.util.*;

public class CalorieProgram{
    /*** Global Variables ***/
    int user_weight;
    int user_height;
    int user_age;

    // Main Menu 
    public static void main(String[] args) {
        System.out.println("Welcome to the calorie program!");
        System.out.println("This program will help you calculate your calories!");
        System.out.println("To calculate your calories, you will need to enter some details!");

        System.out.println("Please enter your age: ");      // Asks for users age 
        Scanner ageReader = new Scanner(System.in);         
        int user_age = ageReader.nextInt();           

        System.out.println("Please enter your weight: ");   // Asks for users weight
        Scanner userinput = new Scanner(System.in);     
        int user_weight = userinput.nextInt();

        System.out.println("Please choose one of the following options");
        System.out.println("1: Weight gain");
        System.out.println("2: Weight loss");
        Scanner reader = new Scanner(System.in);    // Creates a Scanner object
        String input = reader.nextLine();
    }
}