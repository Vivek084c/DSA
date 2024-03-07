#include<iostream>
using namespace std;

int main(){
    int c;
    cin>>c;
    cout<<"hellow world"<<endl;

    if (c>0){
        cout<<"a is positive"<<endl;
    }
    else{
        cout<<" a is a negative number"<<endl;
    }
   
    int a,b;
    cin>>a>>b;
    cout<<"the value of a is : "<<a<<"the value of b is :"<<b<<endl;

    int a,b;
    cout<<"enter the value of a"<<endl;
    cin>>a;
    cout<<"enter the value of b"<<endl;
    cin>>b;
    cout<<"the value of a and b is "<<a <<b<<endl;

    int n;
    cin>>n;
    int i=1;
    while (i<n){
        cout<<i<<endl;
        i+=1;
    }

}