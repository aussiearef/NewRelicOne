import static spark.Spark.*;

public class app {
    public static void main(String[] args) {

        System.out.println("Please navigate to http://localhost:4567/hello");
        // Set up a route that responds to HTTP GET requests at the "/hello" endpoint
        get("/hello", (req, res) -> {
            // Set the response type to JSON
            res.type("application/json");

            // Create a JSON response
            String jsonResponse = "{\"message\": \"Hello, World!\"}";

            return jsonResponse;
        });
    }
}
