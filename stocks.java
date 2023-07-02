import java.util.*;
class stocks {
    public int max(int [] price){
        int minp=Integer.MAX_VALUE;
        int maxp=0;
        for (int i=0;i<price.length; i++){
            if(price[i]<minp){
                minp=price[i];
            else if(peice[i]-minp>maxp){
                maxp= price[i]-minp            }
            }
        }return maxp;
    }
}