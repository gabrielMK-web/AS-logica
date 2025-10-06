public class Review {
    private User author;
    private MediaItem item;
    private int rating;
    private String comment;

    public Review(User author, MediaItem item, int rating, String comment) {
        this.author = author;
        this.item = item;
        this.rating = rating;
        this.comment = comment;
    }

    public User getAuthor() { return author; }
    public MediaItem getItem() { return item; }
    public int getRating() { return rating; }
    public String getComment() { return comment; }

    @Override
    public String toString() {
        return "Review{" + author.getUsername() + ": " + rating + " - " + comment + "}";
    }
}
