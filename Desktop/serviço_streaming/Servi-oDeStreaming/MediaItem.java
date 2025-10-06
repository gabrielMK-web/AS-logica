public abstract class MediaItem {
    private int id;
    private String title;
    private int duration; // minutos
    private String genre;

    public MediaItem(int id, String title, int duration, String genre) {
        this.id = id;
        this.title = title;
        this.duration = duration;
        this.genre = genre;
    }

    // Encapsulamento
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public int getDuration() { return duration; }
    public void setDuration(int duration) { this.duration = duration; }

    public String getGenre() { return genre; }
    public void setGenre(String genre) { this.genre = genre; }

    // Polimorfismo
    public abstract void play();
}
