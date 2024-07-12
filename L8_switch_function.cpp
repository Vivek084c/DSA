#include <iostream>
using namespace std;

int pow(int a,int b){
int ans = 1;
for (int k=1; k<=b; k++){
    ans = ans*a;
}
return ans;
}


int main(){
    int num = 1;

    // cout<<endl;
    // switch (num)
    // {
    //     case 1: cout<<"firsafasst"<<endl;
    //         break;
    //     case 2: cout<<"secosafasnd"<<endl;
    //         break;
    //     default: cout<<"default"<<endl;
    // }
    // return 0 ;



    // calculator program
    // int a,b;
    // cout<<"enter the value of a "<<endl;
    // cin>>a;
    // cout<<"enter the value of b"<<endl;
    // cin>>b;
    // cout<<"the sum of the number is "<< (a+b) <<endl;
    // return 0;


    // functioin
    // int a,b;
    // cout<<"enter the value of a "<<endl;
    // cin>>a;
    // cout<<"enter the value of b "<<endl;
    // cin>>b;
    // int ans=1;
    // for (int i=1; i<=b; i++){
    //     ans = ans * a;
    // }
    // cout<<"the value of a to pow of b is "<<ans<<endl;
    // return 0 ; 

    int a,b;
    cout<<"enter the value of a "<<endl;
    cin>>a;
    cout<<"enter the valeu of b"<<endl;
    cin>>b;

    cout<<pow(a,b)<<endl;
}
