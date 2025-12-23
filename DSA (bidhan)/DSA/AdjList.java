import java.util.ArrayList;
import java.util.List;

public class AdjList {
    int vertices;
    SingleLinkedList adjList[];

    AdjList(int vertices){
        this.vertices=vertices;
        adjList=new SingleLinkedList[vertices];

        for(int i=0;i<vertices;i++){
            adjList[i]=new SingleLinkedList();
        }
    }
    void addEdge(int u,int v){
        adjList[u].addNode(v);
        adjList[v].addNode(u);
    }
    List<Integer> getAdjNodes(int i){
        List<Integer> adjnodes=new ArrayList<>();
        SingleLinkedList.Node current=adjList[i].head;
            while (current!=null) {
                System.out.print(current.data+", ");
                current=current.next;
            }
        return adjnodes;
    }

    void printGraph(){
        for(int i=0;i<vertices;i++){
            System.out.println(i+" is connected to ");
            SingleLinkedList.Node current=adjList[i].head;
            while (current!=null) {
                System.out.print(current.data+", ");
                current=current.next;
            }
            System.out.println("");
        }
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
