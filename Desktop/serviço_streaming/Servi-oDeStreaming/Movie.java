public class Movie extends MediaItem implements Streamable {
    private String director;

    public Movie(int id, String title, int duration, String genre, String director) {
        super(id, title, duration, genre);
        this.director = director;
    }

    public String getDirector() { return director; }
    public void setDirector(String director) { this.director = director; }

    @Override
    public void play() {
        System.out.println("Tocando filme: " + getTitle() + " (diretor: " + director + ")");
    }

    @Override
    public void stream() {
        System.out.println("Stream do filme: " + getTitle());
        play();
    }

    @Override
    public String toString() {
        return "Movie{" + getId() + ", '" + getTitle() + "'}";
    }
}
