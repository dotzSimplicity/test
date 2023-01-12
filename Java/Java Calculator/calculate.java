import java.util.*;

public class calculate { // W.I.P.
    public static void main(String[] args) {

        // intro
        System.out.println("Console Calculator by dotzSimplicity - Java Edition.");
        System.out.println("Possible Operators: +, -, *, /, %");

        // num1
        System.out.println("Enter your first number: ");
        Scanner input1 = new Scanner(System.in);
        int num1 = input1.nextInt();
        System.out.println(num1 + " Registered");
        input1.close();

        // operator
        System.out.println("Enter your operator: ");
        Scanner input2 = new Scanner(System.in);
        String operator = input2.next();
        System.out.println(num1 + operator + " Registered");
        input2.close();

        // num2
        System.out.println("Enter your second number: ");
        Scanner input3 = new Scanner(System.in);
        int num2 = input3.nextInt();
        System.out.println(num1 + operator + num2 + " Registered");
        input3.close();

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
