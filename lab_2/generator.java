import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class generator {
    public static void main(String[] args) {
        Random random = new Random();
        StringBuilder bits = new StringBuilder(129);

        for (int i = 0; i < 128; i++) {
            bits.append(random.nextInt(2));
        }

        System.out.println("Random binary sequence: " + bits.toString());

        try (FileWriter fileWriter = new FileWriter("random_bits_java.txt")) {
            fileWriter.write(bits.toString());
        } catch (IOException e) {
            System.err.println("Error when entering a file: " + e.getMessage());
        }
    }
}
