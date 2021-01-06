package com.section7;

public class DeluxeBurger extends Hamburger {

    private double drinkPrice = 6.00;
    private double chipsPrice = 5.40;
    private double basePrice;

    public DeluxeBurger(String breadRollType, String meat, double basePrice) {
        super(breadRollType, meat, basePrice);
        this.basePrice = basePrice;
    }

    public double getTotalPriceCharge() {
        return super.getTotalPriceCharge() + drinkPrice + chipsPrice;
    }

    public String getName() {
        return getClass().getSimpleName();
    }

    public void getDetails() {
        System.out.println("\n\n");
        System.out.println("Base Price: R" + this.basePrice);
        System.out.println("Drink Price: R" + this.drinkPrice);
        System.out.println("Chips Price: R" + this.chipsPrice);
        System.out.println("Grand total is for:" + getName() + " = R" + this.getTotalPriceCharge());
    }
}
