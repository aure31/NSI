import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    /**
     * @param n le nombre de syllabes dans chaque liste
     * @param a les syllabes de début de mot
     * @param b les syllabes de fin de mot
     */
    static void correctionsMinimales(int n, String[] a, String[] b) {
        /* TODO Afficher, sur une ligne, le nombre de corrections minimal pour
        rendre la phrase juste.  */
        
        TreeMap<Integer,Integer> listA = dico(a,n);
        TreeMap<Integer,Integer> listB = dico(a,n);

        TreeMap<Integer,Integer> list = new TreeMap<>();
        for (Integer i : listA.keySet()){
            for (Integer j : listB.keySet()()){
                int id = (i) * (j);
                
            }
        }
        int count = 0;
        while (list.size() != 1) {
            int firstKey = list.firstKey();
            int lastKey = list.lastKey();
            int firstVal = list.get(firstKey);
            int lastVal = list.get(lastKey);
            if (firstVal < lastVal) {
                int A = list.remove(list.firstKey());
                list.merge(firstKey + 1, A, Integer::sum);
            } else {
                int B = list.remove(list.lastKey());
                list.merge(lastKey - 1, B, Integer::sum);
            }
            count++;
        }

        System.out.println(count);
    }

    private static TreeMap<Integer,Integer> dico(String[] list, int n){
        TreeMap<Integer,Integer> map = new TreeMap<>();
        for (int i = 1; i < n; i++){
            map.merge(list[i],1,Integer::sum);
        }
        return map;
    }

    public static void main(String[] args) throws java.io.IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] a = new String[n];
        for (int i = 0; i < n; ++i) {
            a[i] = reader.readLine();
        }
        String[] b = new String[n];
        for (int i = 0; i < n; ++i) {
            b[i] = reader.readLine();
        }

        correctionsMinimales(n, a, b);
    }
}