package shangjione;

public class CSS {
			static class Course{
				static String[] cour= {"Java","Python","WebEngineering"};
			}//自定义课程类型
		static class Book{
			String book;
		Book(String m){
				if(m.equals(Course.cour[0])==true) {
					book= "java 8";
			}
				if(m.equals(Course.cour[2])==true) {
					book="WebEngineering 3 and Web 2";
				}
				if(m.equals(Course.cour[1])==true) {
					book="Python 2";
				}
				}
		}//自定义每个课程所需要的书籍
		static class Student{
			long id;
			Student(String i,String a){
				Book m=new Book(a);
				id=Long.parseLong(i);
				System.out.println(id+" select "+a+" with books Thinking in "+a+","+m.book);
			}
			Student(String i,String a,String b){
				id=Long.parseLong(i);
				Book m=new Book(a);
				Book n=new Book(b);
				System.out.print(id+" select "+a+" with books Thinking in "+a+","+m.book);
				System.out.println("; and "+b+" with "+n.book);
			}
			Student(String i,String a,String b,String c){
				id=Long.parseLong(i);
				Book m=new Book(a);
				Book n=new Book(b);
				Book p=new Book(c);
				System.out.print(id+" select "+a+" with books Thinking in "+a+","+m.book);
				System.out.print("; "+b+" with "+n.book);
				System.out.println("; and "+c+" with "+p.book);
			}
		}//学生类
		public static void main(String[] args) {
			int j=args.length;
			if(j==2) {
				Student x=new Student(args[0],args[1]);
			}
			if(j==3) {
				Student y=new Student(args[0],args[1],args[2]);
			}
			if(j==4) {
				Student z=new Student(args[0],args[1],args[2],args[3]);
			}
		}
		}

