import java.io.FileWriter; // Import the File class
import java.io.IOException; // Import the IOException class to handle errors
import java.nio.file.Files;
import java.nio.file.*;
import java.util.*;

class main 
{ 

    // Your program begins with a call to main().
    // Prints "Hello, World" to the terminal window. 
    public static void main(String args[]) throws IOException 
    { 
        String filename=args[0];
        

        


        Path path = Paths.get(filename);
         
        List<String> contents = Files.readAllLines(path);
        
        
        
        int result=Integer.parseInt(contents.get(0))*2;

 
        Path path2 = Paths.get("team1_teste/challenge01/result.txt");
        byte[] strToBytes = String.valueOf(result).getBytes();

        
        
        Files.write(path2, strToBytes);
        
    

        


    } 
}