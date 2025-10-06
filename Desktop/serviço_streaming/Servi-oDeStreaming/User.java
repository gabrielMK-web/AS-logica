import java.util.ArrayList;
import java.util.List;

public class User {
    private String username;
    private String email;
    private List<Review> reviews = new ArrayList<>();

    public User(String username, String email) {
        this.username = username;
        this.email = email;
    }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public void addReview(Review r) {
        reviews.add(r);
    }

    public List<Review> getReviews() { return reviews; }

    @Override
    public String toString() {
        return "User{" + username + "}";
    }
}
