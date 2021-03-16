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
public class Student extends Parents{
    private String name;
    private String idNumber;
 
   public String getName(){
       return name;
//       System.out.println("Rhea");
   }
   
   public String getId(){
       return idNumber;
   }
   
   public void setName(String newName){
       this.name=newName;
   }
   
   public void setId(String newId){
       this.idNumber = newId;
   }
   static void alloWance(){
       System.out.println("500");
   }
   
    @Override
   public void congrats(){
        System.out.println("Congratulations Parents and Thank You so much.");
   }
}
