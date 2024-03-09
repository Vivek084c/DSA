// 1)--encasulation- wraping up data members and functions into a single class 
// why we do encasulation, we do this to perform data hiding, advantage is that if we mark a data as private we cannot directly access that data outside the class, we can 
// read this data using the detter method,

// implementing encasulation

// code start___________________________
// #include<iostream>
// using namespace std;

// class student{
//     private:
//     string name;
//     int age;
//     int height;

//     public :
//     int getAge(){
//         return this->age;
//     }
// };

// int main(){
//     //creating objext of class studnet
//     student vivek;
//     cout<<"everything is running fine"<<endl;
//     return 0;
    

// };
// code end___________________________-


// 2)-- inheritance : the ability of child class to inherity the probperty of its parent class 

// code starts-------------------------------
// #include<iostream>
// using namespace std;

// class Human{
//     public:
//     int height;
//     int weight; 
//     int age;

//     public:
//     int getAge(){
//         return this->age;
//     }
//     void setWeight(int inputWeight){
//         this->weight=inputWeight;
//     }
// };

// // creating male class form human class 
// class male:public Human{
// public:
// string color;

// void sleep(){
//     cout<<"its sleeping time"<<endl;
// }
// };


// int main(){
//     // creating object of male class
//     male obj1;
//     cout<<obj1.weight<<endl;
//     cout<<obj1.age<<endl;
//     cout<<obj1.height<<endl;
//     //from above we can observe that male class can inherit weight, age and height

//     return 0;
// }

// code ends-------------------------------


// IMPLEMENTING SINGLE INHERITANCE
// #include<iostream>
// using namespace std;

// class animanls{
//     public:
//     int age;
//     int speed;
//     string name;
// };

// class dog: public animanls{

//     public:
//     string breed;

//     public:
//     void bark(){
//         cout<<"dogs class"<<endl;
//     }
// };

// // Implementing multilevel inheritance
// class germanShepard: public dog{
//     public:
//     string dogname;

//     public:
//     void dance(){
//         cout<<"the dog is danceing"<<endl;
//     }
// };

// int main(){
//     dog d1;
//     d1.bark();
//     cout<<d1.age<<endl;
//     cout<<d1.name<<endl;

//     germanShepard g1;
//     g1.dance();
//     cout<<g1.age<<endl;
//     return 0;
// }


// implementing polymorphism

#include<iostream>
using namespace std;

class a{
    public:
    void sayhellow(){
        cout<<"hellow world"<<endl;
    }

    void sayhellow(string name){
        cout<<"hellow "<< name<<endl;
    }
};


int main(){
    a ob;
    ob.sayhellow("vivek");
    return 0;

}





