#include <pybind11/embed.h>
#include <iostream>

namespace py = pybind11;

int main() {
    py::scoped_interpreter guard{};  // Start the Python interpreter

    // Import the Python module and retrieve the Rectangle class
    py::module rectangle_module = py::module::import("rectangle");
    py::object Rectangle = rectangle_module.attr("Rectangle");

    // Create an instance of the Rectangle class
    py::object my_rectangle = Rectangle("MyRectangle", 4, 5);

    // Call the area method
    py::object area = my_rectangle.attr("area")();
    std::cout << "The area of " << my_rectangle.attr("name").cast<std::string>() << " is " << area.cast<int>() << std::endl;

    // Print the rectangle details
    py::print(my_rectangle);

    return 0;
}
