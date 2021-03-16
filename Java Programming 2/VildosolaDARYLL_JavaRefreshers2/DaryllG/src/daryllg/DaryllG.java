/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package daryllg;


/**
 *
 * @author 2ndyrGroupA
 */
public class DaryllG {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        int i = 10;
        int n = i++%5;

        
        System.out.println("The value of i is: " + i);
        System.out.println("The value of n is: " + n);
        
        int i_2 = 10;
        int n_2 = ++i%5;
        
        System.out.println("The value of i is: " + i_2);
        System.out.println("The value of n is: " + n_2);
    }
    
}
