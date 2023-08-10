#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class Rectangle{
    // class variables
    int width, height;
    string name;
    bool square;
public:
    // constructors
    Rectangle() {};
    Rectangle(string, int, int);
    // methods
    int area() {
        return width*height;
    }
    void print();
    // overload operators
    Rectangle operator + (const Rectangle&);
    friend ostream& operator <<(ostream& os, const Rectangle&);
};

// main constructor
Rectangle::Rectangle (string name, int width, int height) {
    this->name = name;
    this->width = width;
    this->height = height;
    this->square = width == height;
}

// print the picture of the rectangle
void Rectangle::print(){

    // print top
    cout << endl;
    for(int i = 0; i < width; ++i){
        cout << "* ";
    }
    cout << endl;

    // print middle
    for (int line = 1; line < height -1; ++line){
        cout << "* ";
        for (int i = 0; i < width - 2; ++i){
            cout << "  ";
        }
        cout << "* " << endl;  
    }

    // print bottom
    for(int i = 0; i < width; ++i){
        cout << "* ";
    }
    cout << endl << endl;

}


// overload the + operator. adds height and width of both triangles
Rectangle Rectangle::operator + (const Rectangle& rec){
    Rectangle temp;
    temp.name = name + "-" + rec.name;
    temp.width = width + rec.width;
    temp.height = height + rec.height;
    temp.square = temp.width == temp.height;
    return temp;
}

// overload the << operator. Used for printing out the info on rectangles
ostream& operator <<(ostream& os , const Rectangle& rec){

    os << "Name:   " << rec.name << endl 
       << "Width:  " << rec.width << endl 
       << "Height: " << rec.height << endl 
       << "Area:   " << rec.height*rec.width << endl 
       << "Is it a square? ";
    if(rec.square) {
        os << "yes" << "\n\n";
    } else {
        os << "no" << "\n\n";
    }
    return os;
}

int main () {

    // load file
    ifstream myfile ("rec_data.txt");
    // initialize variables to store the data
    string mystring;
    vector<string> names;
    vector<int> width;
    vector<int> height;

    if(myfile.is_open() ){
        while(myfile){ //while the file still has lines and isnt broken
            // pull a line
            getline(myfile, mystring);
            if(mystring == "="){ // if the line is equal to "=" we can start reading
                // pull first line which is the name of the rectangle
                getline(myfile, mystring);
                names.push_back(mystring);
                // pull second line which has the width of the rectangle
                getline(myfile, mystring);
                width.push_back(stoi(mystring));
                // pull third and last line which has the width of the rectangle
                getline(myfile, mystring);
                height.push_back(stoi(mystring));
            }
        }
    } else {
        cout << "Couldn't open the file" << endl;
        return 1;
    }

    // initialize size and the Rectangle object array.
    int size = names.size();
    Rectangle* rec = new Rectangle[size];
    
    // add the data to the rec object
    for (int i = 0; i < size; ++i){
        rec[i] = Rectangle(names[i], width[i], height[i]);
        // print the data using the overloaded << operator
        cout << rec[i] << flush;
    }

	// Providing a seed value so random number is actually random
	srand((unsigned) time(NULL));

    // use the overloaded + operator for a new Rectangle object 
    // using random numbers because its more fun. 
    Rectangle result = rec[(rand() % size)] + rec[(rand() % size)];
    
    // print it
    cout << result << flush;
    // print it in 3-D
    result.print();

    return 0;
}
