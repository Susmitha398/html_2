class fita{

    
   private int age=20;
   private String name;
   private int mark;

   
   public int getAge() {
    return age;
   }
   public void setAge(int age) {
    this.age = age;
   }
   public String getName() {
    return name;
   }
   public void setName(String name) {
    this.name = name;
   }
   public int getMark() {
    return mark;
   }
   public void setMark(int mark) {
    this.mark = mark;
   }


   
}

class Sec{

    public static void main(String[] args) {

        fita f1=new fita();
       


       // f1.a=50;
      System.out.println(f1.age);

      
        
    }
}