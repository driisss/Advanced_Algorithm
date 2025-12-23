import java.util.ArrayList;
import java.util.List;

public class AdjMatrix{
    int vertices;
    int matrix[][];
    AdjMatrix(int vertices){
        this.vertices=vertices;
        matrix=new int[vertices][vertices];
    }
    void addEdge(int u,int v){
        matrix[u][v]=1;
        matrix[v][u]=1;
    }
    void printGraph(){
        for(int i=0;i<vertices;i++){
            System.out.println(i+" is connected to ");
            for(int j=0;j<vertices;j++){
                if(matrix[i][j]!=0){
                    System.out.print(j+", ");
                }
            }
            System.out.println("");
        }
    }
    //write function to print matrix
    List<Integer> getAdjNodes(int i){
        List<Integer> adjlist=new ArrayList<>();
        for(int j=0;j<vertices;j++){
            if(matrix[i][j]!=0){
                System.out.print(j+", ");
            }
        }
        return adjlist;

    }
    public static void main(String[] args) {
        AdjMatrix a=new AdjMatrix(5);
        a.addEdge(0, 1);
        a.addEdge(0,2);
        a.addEdge(0, 3);
        a.addEdge(1,3);
        a.addEdge(2,3);
        a.addEdge(3,4);
        a.printGraph();
    }
}
