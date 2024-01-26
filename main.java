import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Stream;

class Main {
    /**
     * @param n le nombre de clients
     * @param charges la liste des poids du matériel de chaque soldat, en kilogrammes
     */
    static void attenteMinimale(int n, int[] charges) {
        /* TODO Afficher le temps d'attente cumulé total minimal après avoir
        réordonné les soldats.  */
        Arrays.sort(charges);
        int delay = 0;
        for( int i = 0; i < n-1; i++){
            int e = charges[i]+delay;
            delay += e;
        }
        System.out.println(delay);
    }

    public static void main(String[] args) throws java.io.IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int[] charges = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        attenteMinimale(n, charges);
    }
}