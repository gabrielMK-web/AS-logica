import java.util.List;

public class Main {
    public static void main(String[] args) {
        User gabriel = new User("gabriel", "gabriel@email.com");
        Account acc = new Account("acc001", gabriel);

        Movie movie1 = new Movie(1, "A Viagem", 120, "Drama", "Ana Direto");
        Series series1 = new Series(2, "Mistérios da Sala", 45, "Suspense", 2);

        Episode ep1 = series1.addEpisode(1, "O Começo");
        Episode ep2 = series1.addEpisode(2, "A Reviravolta");

        Playlist p1 = new Playlist("Favoritos");
        p1.add(movie1);
        p1.add(ep1);
        p1.add(ep2, 1);

        acc.addPlaylist(p1);

        Review r = new Review(gabriel, movie1, 5, "Ótimo filme!");
        gabriel.addReview(r);

        Streamable s1 = movie1;
        Streamable s2 = ep1;

        System.out.println("--- Execução de demonstração ---");
        System.out.println(acc);
        System.out.println(p1);

        s1.stream();
        s2.stream();

        System.out.println("\nTocando playlist:");
        p1.playAll();

        List<Episode> eps = series1.getEpisodes();
        System.out.println("\nEpisódios da série: " + series1.getTitle());
        for (Episode e : eps) System.out.println(e);

        System.out.println("\nReviews do usuário:");
        for (Review rev : gabriel.getReviews()) System.out.println(rev);
    }
}
