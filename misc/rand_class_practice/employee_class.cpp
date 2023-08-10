#include <iostream>
using namespace std;


class Employee {
    string name;
    int age;
  public:
    void set_values(string,int);
    void print_everything ();
};

void Employee::set_values(string name, int age){
    this->name = name;
    this->age = age;
}


void Employee::print_everything(){
    cout << "This employees name is " << this->name << " theyre " << this->age << " years old" << endl;
}

int main(){
    Employee emp1, emp2;

    emp1.set_values("gavin", 22);
    emp2.set_values("nathan", 19);

    emp1.print_everything();
    emp2.print_everything();

}