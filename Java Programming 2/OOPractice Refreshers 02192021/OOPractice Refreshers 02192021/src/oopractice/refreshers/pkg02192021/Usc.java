/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package oopractice.refreshers.pkg02192021;

/**
 *
 * @author 2ndyrGroupA
 */ 
class Usc implements School {

    @Override
    public void schoolName() {
        System.out.println("University of San Carlos");
    }

    @Override
    public void address() {
        System.out.println("Talamban, Cebu City");
    }
    
}

class Cnu implements School{
    @Override
    public void schoolName() {
        System.out.println("Cebu Normal University");
    }

    @Override
    public void address() {
        System.out.println("Colon, Cebu City");
    }
    
}
