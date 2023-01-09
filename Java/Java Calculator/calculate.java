import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class calculate { // W.I.P.
    public static void main(String[] args) throws IOException {
        
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input);

        // intro
        System.out.println("hello i am calculator, i can do math");
        System.out.println("calculating time poggers");
        System.out.println("Possible Operators: +, -, *, /, %");

        // num1
        System.out.println("Enter your first number: ");
        int num1 = reader.readLine();
        System.out.println(num1);

        // operator
        System.out.println("Enter your operator: ");
        String operator = reader.readLine();
        System.out.println(num1 + operator + "Registered");

        // num2
        System.out.println("Enter your second number: ");
        int num2 = reader.readLine();
        System.out.println(num1 + operator + num2 + "Registered");
        
        // calculation
        if (operator == "+") {
            System.out.println(num1 + num2);
        } else if (operator == "-") {
            System.out.println(num1 - num2);
        } else if (operator == "*") {
            System.out.println(num1 * num2);
        } else if (operator == "/") {
            System.out.println(num1 / num2);
        } else if (operator == "%") {
            System.out.println(num1 % num2);
        } else {
            System.out.println("Invalid Operator, please try again.");
            System.exit(0);
        }

    };
}
