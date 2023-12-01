import java.util.*;

public class CalorieProgram{
    /*** Global Variables ***/
    static int user_age;
    static int user_weight;
    static int user_height;

    // Main Menu 
    public static void main(String[] args) {
        System.out.println("Welcome to the calorie program!");
        System.out.println("This program will help you calculate your calories!");
        System.out.println("To calculate your calories, you will need to enter some details!");

        System.out.println("Please enter your age: ");      // Asks for users age 
        Scanner ageReader = new Scanner(System.in);         
        user_age = ageReader.nextInt();           

        System.out.println("Please enter your weight: ");   // Asks for users weight
        Scanner weightReader = new Scanner(System.in);     
        user_weight = weightReader.nextInt();

        System.out.println("Please enter your height: ");   // Asks for users height
        Scanner heightReader = new Scanner(System.in);     
        user_height = heightReader.nextInt();

        System.out.println("Please choose one of the following options");
        System.out.println("1: Weight gain");
        System.out.println("2: Weight loss");
        Scanner reader = new Scanner(System.in);    
        int input = reader.nextInt();

        if (input == 1){
            weightGain();
        } else if (input == 2){
            weightLoss();
        }
    }

    public static void weightGain(){
        System.out.println("In order, to lose weight we first need to calculate your calorie maintenance");
        System.out.println("These are the details you have entered: ");
        System.out.println("age: " + user_age + " weight: " + user_weight + " height: " + user_height);
    }

    public static void weightLoss(){
        
    }
}