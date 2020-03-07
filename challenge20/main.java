import java.io.*;
import java.lang.*;
class main
{
 
    // Check if it is possible to go to (x, y) from current position. The
    // function returns false if the cell has value 0 or already visited
    private static boolean isSafe(int mat[][], int visited[][], int x, int y)
    {
        return !(mat[x][y] == 0 || visited[x][y] != 0);
    }
 
    // if not a valid position, return false
    private static boolean isValid(int N, int M, int x, int y)
    {
        return (x < M && y < N && x >= 0 && y >= 0);
    }
 
    // Find Shortest Possible Route in a Matrix mat from source cell (0, 0)
    // to destination cell (x, y)
 
    // 'min_dist' stores length of longest path from source to destination
    // found so far and 'dist' maintains length of path from source cell to
    // the current cell (i, j)
 
    public static int findShortestPath(int N, int M ,int mat[][], int visited[][],
                     int i, int j, int x, int y, int min_dist, int dist)
    {
        // if destination is found, update min_dist
        if (i == x && j == y)
        {
            return Integer.min(dist, min_dist);
        }
 
        // set (i, j) cell as visited
        visited[i][j] = 1;
 
        // go to bottom cell
        if (isValid(N, M, i + 1, j) && isSafe(mat, visited, i + 1, j)) {
            min_dist = findShortestPath(N, M, mat, visited, i + 1, j, x, y,
                                        min_dist, dist + 1);
        }
 
        // go to right cell
        if (isValid(N, M, i, j + 1) && isSafe(mat, visited, i, j + 1)) {
            min_dist = findShortestPath(N, M, mat, visited, i, j + 1, x, y,
                                        min_dist, dist + 1);
        }
 
        // go to top cell
        if (isValid(N, M, i - 1, j) && isSafe(mat, visited, i - 1, j)) {
            min_dist = findShortestPath(N, M, mat, visited, i - 1, j, x, y,
                                        min_dist, dist + 1);
        }
 
        // go to left cell
        if (isValid(N, M, i, j - 1) && isSafe(mat, visited, i, j - 1)) {
            min_dist = findShortestPath(N, M, mat, visited, i, j - 1, x, y,
                                        min_dist, dist + 1);
        }
 
        // Backtrack - Remove (i, j) from visited matrix
        visited[i][j] = 0;
 
        return min_dist;
    }
 
    public static int[] StringArrToIntArr(String[] s) {
        int[] result = new int[s.length];
        for (int i = 0; i < s.length; i++) {
            result[i] = Integer.parseInt(s[i]);
        }
        return result;
    }
    public static void main(String[] args) throws Exception
    {
        int lines = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            while (reader.readLine() != null) lines++;
            reader.close();
        }
        // M x N matrix
        int M = lines;
        int N = lines;
        int mat[][] = new int [lines][1];
        int count = 0;
        int sourceX = 0;
        int sourceY = 0;
        int targetX = 0;
        int targetY = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(args[0]))) {
            String line;
            line = br.readLine();
            while (line != null) {
                String temp = line.replace("#","0").replace(" ", "1");
                for(int s = 0; s < temp.split("").length; s++) {
                    if(temp.split("")[s].equals("S")) {
                        sourceX = s;
                        sourceY = count;
                    }
                    if (temp.split("")[s].equals("X")) {
                        targetX = s;
                        targetY = count;
                    }
                }
                temp = temp.replace("S","1").replace("X","1");
                mat[count] = StringArrToIntArr(temp.split(""));
                line = br.readLine();
                count++;
            }
        }

        // construct a matrix to keep track of visited cells
        int[][] visited = new int[M][N];
 
        //int min_dist = findShortestPath(mat, visited, 23, 20, 18, 1,
        //                                Integer.MAX_VALUE, 0);
        int min_dist = findShortestPath(N, M, mat, visited, sourceX, sourceY, targetX, targetY,
                                           Integer.MAX_VALUE, 0);
 
        if(min_dist != Integer.MAX_VALUE) {
            try {
                FileWriter myWriter = new FileWriter("team15_ttwins/challenge20/result.txt");
                myWriter.write("Caminho mais curto: " + Integer.toString(min_dist + 2));
                myWriter.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else {
            try {
                FileWriter myWriter = new FileWriter("team15_ttwins/challenge20/result.txt");
                myWriter.write("Impossible");
                myWriter.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
