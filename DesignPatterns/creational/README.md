# **Creational Design Patterns.**
```text
Creational Design Patterns as one of the simplest sets of Design Patterns.
```
### Advantages
* Object creation can be independent of the class implementation.
* Adding support of new type of object is very easy
* Logic of object creation is hidden
##Creational Design Patterns Include

## 1) Singleton Design Pattern

```text
This Pattern states that at a given time there should be only one `instance` of any given object.
Thus reusing the object over and over again.

Singleton Object creation has only 2 set of rules to be followed.
1) Object Must have only Single Instance Created.
2) There should be global access to the object created.

In Python Singleton is easiest to create for any given class.
Since the `__new__` is always a class method in python (until version 3.8).
You can always modify this method to make your object as an Singleton Object.
```
### Advantages
* Only single instance is created hence low memory usage.
*  Faster Execution Since the Class is Not instantiated multiple time.
* We got the global access to the instance of the object.

### Disadvantages
* Its not easy to use the singleton method in multithread environment, because we have to take care that multithread wouldn’t create singleton object several times.
* As they introduce the global state to the application, it makes the unit testing very hard. 

### 2) Factory Pattern

```text
Factory Pattern Defines a way to delegate the class that may or may not provide similar kind of usage.

For e.g.
Consider car which have a pre-requisites to qualify as car (4 wheels, body etc.)  
Now you need to create a new car which needs to have these predefined sets as well as some extra features.
Then you define an abstract class a car having pre-requisites and derive any new class from this should implement
all the requisites and can add aditional featuers.

Thus you can say that a Factory Design Pattern derives the way for Designing the class.

Factory design pattern is used when we have a super class with multiple subclasses and based on input, we need to return one of the sub-classes.
This pattern takes out the responsibility of instantiation of a class from client program to the factory class.
 In Python it is abstract class in most cases.

```
### Advantages
* Factory pattern provides approach to code for interface rather than implementation. 
* Factory pattern removes the instantiation of actual implementation classes from client code, making it more robust, less coupled and easy to extend. 
* Factory pattern provides abstraction between implementation and client classes through inheritance.

## 3) Abstract Factory Patter

```text
Abstract is a superset of factory.
This set contains a multiple factories which superset a multiple properties for an object where every object an have its multiple properties.
It groups the individual but related/dependent factories together without specifying their concrete classes.

For e.g
Lets continue with the above car example a little more detailed way.
As we said the car has few pre-requisites to qualify as a car like 4 wheels.
However this wheel may have its own set or properties such as type (allow, spokes, etc.) shape, number etc.
Hence in this case each requisite in the car can be it's own factory pattern.
To define the car we may need to have a set of these factories combined to be able to define the car correctly.
As a result the class `Car` becomes a set of multiple factory method having  wheels as it subsets.

Thus Defining Abstract Factory. 
```
### Advantages
* Abstract Factory provides a method to interface multiple groups.
* This method is highly scalable since it allows multiple groups to be used.

## 4) Builder Pattern

```text
Builder pattern allows you to create a complex set of an object when creation of the object is not possible directly.

For e.g. 
Let's Consider a serialization deserialization a complex json Object which consists of list, dictionary and much more.
```
```json
{
    "1st_key" : "some_data",
    "2nd_key" : [
            {
                "abc": "some_data",
                "def": "some_data"
            }, 
            {
               "abc": "some_data",
               "def": "some_data"
            }
          ] 
}
```
```text
So in this case builder pattern would have a class which stores the 1st level of keys with `2nd_key` containing a List 
object having the class a different class for new class object.
Thus these classes can have their independent use and can be used and easily replaced.

The intent of the Builder Pattern is to separate the construction of a complex object from its representation, so that the same construction process can create different representations.
This type of separation reduces the object size. 
The design turns out to be more modular with each implementation contained in a different builder object.
Adding a new implementation (i.e., adding a new builder) becomes easier. The object construction process becomes independent of the components that make up the object.
This provides more control over the object construction process.
```

## Advantages
* Clear separation between the construction and representation of an object.
* Provides better control over construction process.
* Supports to change the internal representation of objects.

## 5) Prototype Pattern

```text
Prototype pattern creates object based on an existing object through cloning.
Prototype pattern is used when the object creation is a costly affair and requires a lot of time and resources and 
you have a similar object already existing. So this pattern provides a mechanism to copy the original object to a new 
object and then modify it according to our needs.

For example, an object is to be created after a costly database operation.
We can cache the object, returns its clone on next request and update the database as and when needed thus reducing database calls.

```

### Advantages
* It reduces the need of sub-classing.
* It hides complexities of creating objects.
* The clients can get new objects without knowing which type of object it will be.
* It lets you add or remove objects at runtime.
