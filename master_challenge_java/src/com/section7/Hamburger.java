package com.section7;

public class Hamburger {

    private String breadRollType;
    private String meat;

    private double basePrice;

    private int lettuce;
    private int tomato;
    private int carrot;
    private int olive;

    private double lettucePrice = 1.00;
    private double tomatoPrice = 2.00;
    private double carrotPrice = 2.50;
    private double olivePrice = 3.00;


    public Hamburger(String breadRollType, String meat, double basePrice, int lettuce, int tomato, int carrot, int olive) {
        this.breadRollType = breadRollType;
        this.meat = meat;
        this.basePrice = basePrice;
        this.lettuce = lettuce;
        this.tomato = tomato;
        this.carrot = carrot;
        this.olive = olive;
    }

    public Hamburger(String breadRollType, String meat, double basePrice) {
        this.breadRollType = breadRollType;
        this.meat = meat;
        this.basePrice = basePrice;
    }

    public String getName() {
        return getClass().getSimpleName();
    }


    public double getTotalPriceCharge()  {
        return this.basePrice + getLettucePrice() + getTomatoPrice() + getCarrotPrice() + getOlivePrice();
    }

    private double getLettucePrice() {
        return this.lettuce * this.lettucePrice;
    }
    private double getTomatoPrice() {
        return this.tomato + this.tomatoPrice;
    }

    private double getCarrotPrice() {
        return this.carrot * this.carrotPrice;
    }
    private double getOlivePrice() {
        return this.olive * this.olivePrice;
    }

    public void getDetails() {
        System.out.println("\n\n");
        System.out.println("Base Price: R" + basePrice);
        System.out.println("lettuce *" + this.lettuce + " = " + this.getLettucePrice());
        System.out.println("tomato *" + this.tomato + " = " + this.getTomatoPrice());
        System.out.println("olive *" + this.olive + " = " + this.getOlivePrice());
        System.out.println("carrot *" + this.carrot + " = " + this.getCarrotPrice());
        System.out.println("Grand total is for: " + getName() + " = R" + this.getTotalPriceCharge());
    }


}
