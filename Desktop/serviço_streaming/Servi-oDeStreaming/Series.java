import java.util.ArrayList;
import java.util.List;

public class Series extends MediaItem {
    private int seasons;
    private List<Episode> episodes = new ArrayList<>();

    public Series(int id, String title, int durationPerEpisode, String genre, int seasons) {
        super(id, title, durationPerEpisode, genre);
        this.seasons = seasons;
    }

    public int getSeasons() { return seasons; }
    public void setSeasons(int seasons) { this.seasons = seasons; }

    public Episode addEpisode(int episodeNumber, String epTitle) {
        Episode ep = new Episode(getId()*100 + episodeNumber, getTitle(), getDuration(), getGenre(), episodeNumber, epTitle, this);
        episodes.add(ep);
        return ep;
    }

    public List<Episode> getEpisodes() { return episodes; }

    @Override
    public void play() {
        System.out.println("Série: " + getTitle() + " - escolha um episódio para reproduzir.");
    }

    @Override
    public String toString() {
        return "Series{" + getId() + ", '" + getTitle() + "', eps=" + episodes.size() + "}";
    }
}
