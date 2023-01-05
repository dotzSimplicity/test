import java.util.Scanner; // needed for yoinking input

public class cloner {
    public static void main(String[] args) {
        
        System.out.println("hello i am robotoman, say smth bish");
        Scanner input = new Scanner(System.in); // yoinks input

        String robotoman = "robotoman says: ";
        String compiled = robotoman + input.nextLine(); // compiles input with speech

        System.out.println(compiled); // yeets input

}}