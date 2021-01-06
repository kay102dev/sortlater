package com.section7;

public class Main {

    public static void main(String[] args) {

        int[] arr = {2, 3, 4, 5};

        for (int i = 0; i < arr.length; i++) {
//        System.out.println(i + 23);
            //System.out.println(arr[i]);
        }

        // write your code here
        Hamburger order = new Hamburger("white bun", "beef", 5, 1, 2, 1, 1);
        order.getDetails();

        HealthyBurger order2 = new HealthyBurger("chicken", 10.00);
        order2.getDetails();

        DeluxeBurger order3 = new DeluxeBurger("white bun", "beef", 13.00);
        order3.getDetails();
    }
}
