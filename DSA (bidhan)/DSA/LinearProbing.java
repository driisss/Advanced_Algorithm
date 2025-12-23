public class LinearProbing {
    int keys[];
    int values[];
    int capacity;

    public LinearProbing(int capacity){
        this.capacity=capacity;
        keys=new int[capacity];
        values=new int[capacity];
        for(int i=0;i<keys.length;i++){
            keys[i]=1;
            values[i]=-1;
        }
    }

    void insert(int key, int value){
        int i=hashFunction(key);
        if(keys[i]==-1){
            keys[i]=key;
            values[i]=value;
        }
        else{
            //probing
            int tmp=i;
            do{
                i=(i+1)%capacity;
                if(keys[i]==-1){
                    keys[i]=key;
                    break;
                }
            }
            while(tmp!=i);
        }
    }

    int get(int key){
        int i=hashFunction(key);
        if(keys[i]==key){
            return values[i];
        }
        else{
            int tmp=i;
            do{
                i=(i+1)%capacity;
                if(keys[i]==key){
                    return values[i];
                }
            }
            while(tmp!=i);
        }
    }




    int hashFunction(int key){
        return key%capacity;//example hash function
    }

}
