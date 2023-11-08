import static spark.Spark.*;

import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class app {
    public static void main(String[] args) {

        Logger logger = Logger.getLogger(app.class.getName());
        
        try {
            // Create a file handler to log to "log.txt"
            FileHandler fileHandler = new FileHandler("log.txt");
            SimpleFormatter formatter = new SimpleFormatter();
            fileHandler.setFormatter(formatter);

            // Add the file handler to the logger
            logger.addHandler(fileHandler);
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("Please navigate to http://localhost:4567/hello");
        // Set up a route that responds to HTTP GET requests at the "/hello" endpoint
        get("/hello", (req, res) -> {
            // Set the response type to JSON
            res.type("application/json");

            // Create a JSON response
            String jsonResponse = "{\"message\": \"Hello, World!\"}";

            // Log a warning message
            logger.warning("Hello World API Called.");

            return jsonResponse;
        });
    }
}
