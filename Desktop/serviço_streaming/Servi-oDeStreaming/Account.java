import java.util.ArrayList;
import java.util.List;

public class Account {
    private String accountId;
    private User owner;
    private List<Playlist> playlists = new ArrayList<>();

    public Account(String accountId, User owner) {
        this.accountId = accountId;
        this.owner = owner;
    }

    public String getAccountId() { return accountId; }
    public void setAccountId(String accountId) { this.accountId = accountId; }

    public User getOwner() { return owner; }
    public void setOwner(User owner) { this.owner = owner; }

    public void addPlaylist(Playlist p) {
        playlists.add(p);
    }

    public List<Playlist> getPlaylists() { return playlists; }

    @Override
    public String toString() {
        return "Account{" + accountId + ", owner=" + owner.getUsername() + "}";
    }
}
