package com.section7;

public class HealthyBurger extends Hamburger {

    double salmonPrice = 6.00;
    double prawnPrice = 5.40;
    private double basePrice;

    public HealthyBurger(String meat, double basePrice, int lettuce, int tomato, int carrot, int olive) {
        super("brown rye Bread Roll", meat, basePrice, lettuce, tomato, carrot, olive);
        this.basePrice = basePrice;
    }

    public HealthyBurger(String meat, double basePrice) {
        super("brown rye Bread Roll", meat, basePrice);
        this.basePrice = basePrice;

    }

    public double getTotalPriceCharge() {
        return super.getTotalPriceCharge() + salmonPrice + prawnPrice;
    }

    public String getName() {
        return getClass().getSimpleName();
    }

    public void getDetails() {
        System.out.println("\n\n");
        System.out.println("Base Price: R" + this.basePrice);
        System.out.println("Salmon Price: R" + this.salmonPrice);
        System.out.println("Prawn Price: R" + this.prawnPrice);
        System.out.println("Grand total is for: " + getName() + " = R" + this.getTotalPriceCharge());
    }
}
