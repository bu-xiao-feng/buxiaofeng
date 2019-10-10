package balloon;
import java.util.*;
import java.util.Scanner;
public class Main {
public static void main(String[] arr) {
	Scanner cin=new Scanner(System.in);
	int N=0;
	List<String>v=new ArrayList<String>();
	do {
	N=cin.nextInt();
	if(N<0 || N>1000)
		return;
	Map<String,Integer> m=new HashMap<String,Integer>();
    String color;
    int j=0;
	while(j<=N) {
		color=cin.nextLine();
		if(color.length()>15)
			return;
		m.put(color, m.containsKey(color)?m.get(color)+1:1);
		j++;
	}
	int maxx=Collections.max(m.values());
	for(Map.Entry<String, Integer>e:m.entrySet())
		if(e.getValue()==maxx)
			v.add(e.getKey());
	}while(N!=0);
	for(int i=0;i<v.size();i++) {
		System.out.println(v.get(i));
	}
}
}