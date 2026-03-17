# OOP in Python — Animal Hierarchy

## Description
This project demonstrates Object-Oriented Programming concepts in Python
using an Animal class hierarchy.

## Project Structure
lab7/
├── animal.py   # Base class Animal + Child classes Dog, Cat
└── main.py     # Main script demonstrating usage

## Classes
### Animal (Base Class)
- Attributes: name, age, sound
- Methods: speak(), get_info(), __str__()

### Dog (Child Class)
- Inherits from Animal
- Unique attribute: breed
- Unique methods: fetch(), speak()

### Cat (Child Class)
- Inherits from Animal
- Unique attribute: breed
- Unique methods: mour(), speak()

## OOP Concepts Demonstrated
- Inheritance: Dog and Cat inherit from Animal
- Polymorphism: speak() works differently for each class
- Encapsulation: attributes stored inside classes

## How to Run
python main.py

## Output
Dog: Barsik, Breed: Chihuahua, Age: 3
Dog: Pushka, Breed: Retriever, Age: 5
Cat: Scarlet, Breed: British, Age: 4
Cat: Whisker, Breed: Siamskaya, Age: 5