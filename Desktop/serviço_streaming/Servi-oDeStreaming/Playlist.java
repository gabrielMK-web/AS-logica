import java.util.ArrayList;
import java.util.List;

public class Playlist {
    private String name;
    private List<MediaItem> items = new ArrayList<>();

    public Playlist(String name) {
        this.name = name;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    // Sobrecarga de método
    public void add(MediaItem item) {
        items.add(item);
    }

    public void add(MediaItem item, int position) {
        if (position < 0 || position > items.size()) {
            items.add(item);
        } else {
            items.add(position, item);
        }
    }

    public List<MediaItem> getItems() { return items; }

    public void playAll() {
        for (MediaItem m : items) {
            m.play();
        }
    }

    @Override
    public String toString() {
        return "Playlist{" + name + ", size=" + items.size() + "}";
    }
}
