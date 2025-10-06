public class Episode extends Series implements Streamable {
    private int episodeNumber;
    private String episodeTitle;
    private Series parentSeries;

    public Episode(int id, String seriesTitle, int duration, String genre, int episodeNumber, String episodeTitle, Series parent) {
        super(id, seriesTitle, duration, genre, 1);
        this.episodeNumber = episodeNumber;
        this.episodeTitle = episodeTitle;
        this.parentSeries = parent;
    }

    public int getEpisodeNumber() { return episodeNumber; }
    public void setEpisodeNumber(int episodeNumber) { this.episodeNumber = episodeNumber; }

    public String getEpisodeTitle() { return episodeTitle; }
    public void setEpisodeTitle(String episodeTitle) { this.episodeTitle = episodeTitle; }

    public Series getParentSeries() { return parentSeries; }

    @Override
    public void play() {
        System.out.println("Reproduzindo episódio: " + parentSeries.getTitle() + " - Ep" + episodeNumber + ": " + episodeTitle);
    }

    @Override
    public void stream() {
        System.out.println("Stream do episódio: " + episodeTitle);
        play();
    }

    @Override
    public String toString() {
        return "Episode{" + getId() + ", '" + episodeTitle + "'}";
    }
}
