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
public class OOPracticeRefreshers02192021 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //Polymorphism
        Student s1 = new Student();
        Student s2 = new Student();
        //Encapsulation
        s1.setName("Rhea");
        s1.setId("19104859");
        s1.congrats();
        s2.setName("Daryll");
        s2.setId("19104898");
        
        System.out.println(s1.getName()+" "+ s1.getId());
        System.out.println(s2.getName()+" "+ s2.getId());
        
        //Abstract
        Record r1;
        r1 = new Child();
        r1.displayRecord();
        r1.relationship();
        
        Child newChild = new Child();
        newChild.displayRecord();
        newChild.relationship();
        
        
        //Interface
        School newSchool = new Usc();
        School school = new Cnu();
        newSchool.schoolName();
        newSchool.address();
        school.schoolName();
        school.address();
    }
    
}
