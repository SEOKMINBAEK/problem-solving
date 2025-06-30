import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line = br.readLine();

        int n = Integer.parseInt(line);

        for (int i = 0; i < n; i++) {
            String[] testcase = br.readLine().split(" ");
            int a = Integer.parseInt(testcase[0]);
            int b = Integer.parseInt(testcase[1]);

            bw.write((a + b) + "\n");

        }
        bw.flush();
        bw.close();
    }
}