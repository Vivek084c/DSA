#include<iostream>
using namespace std;
void swap(int arr[],int n){

    int start = 0;
    int end = n-1;

    while (start < end){
        int temp = arr[end];
        arr[end] = arr[start];
        arr[start] = temp;
        start++;
        end--;
    }

}


int main(){
    // int num[15];
    // cout<<"value at zero index "<<num[0]<<endl;
    // cout<< "running"<<endl;
    // return 0;

    int num[5] = {1,2,3,4,5} ; 
    swap(num,5);
    for (int i = 0;i<5;i++){
        cout<<num[i]<<endl;
    }
    return 0;

    
}