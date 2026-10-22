/*class FoodOrder extends Thread {

    //FoodOrder()

    String item;

    FoodOrder(String item) {
        this.item = item;
    }

    public void run() {
        System.out.println(item + " Preparation Started");

        try {
            Thread.sleep(3000);
        } 
        catch (Exception e) {
            System.out.println(e);
        }

        System.out.println(item + " Ready to Serve");
    }
}

public class First {
    public static void main(String[] args) {

        FoodOrder f1 = new FoodOrder("Pizza");

        FoodOrder f2 = new FoodOrder("Burger");

        FoodOrder f3 = new FoodOrder("Dosa");

        f1.start();    //thread //auto function jvm
        f2.start();//thread  //auto functio
        f3.start();  // thread
    }
}*/



class MyTask implements Runnable {

    public void run() {

        for (int i = 1; i <= 5; i++) {

            System.out.println(Thread.currentThread().getName()+ " : " + i);
            
        }
    }
}





public class First {

    public static void main(String[] args) {




        MyTask task = new MyTask();

        Thread t1 = new Thread(task, "Thread-1  user gopi");
        Thread t2 = new Thread(task, "Thread-2 user maha");

        t1.start();
        t2.start();
    }
}



