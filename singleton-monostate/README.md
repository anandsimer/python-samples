Hi, In above two examples of python design pattern we are looking at Singleton class example and Monostate class example.

- The Singleton design pattern is all about ensuring that just one instance of a certain class is ever created. All the 
objects references points to the one instance of the class. In the Singleton example we can see the state of object 
remains unchanged in the second object instantiation.

- The Monostate as 'Alex Martelli' named it is anti-singleton pattern or in a way solves the problem 
that Singleton class usage. Monostate class is about sharing the state and behaviour of the Monostate class.
In the example, second instance of the Monostate class can change the state of the 
first instance of the Monostate class which is totally opposite of Singleton pattern.
