Function Notes
   
   
       
Functions
       
A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

       
As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called user-defined functions.

       
Defining a Function
       
       
You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

       
           
Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
           
Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
           
The first statement of a function can be an optional statement - the documentation string of the function or docstring.
           
The code block within every function starts with a colon (:) and is indented.
           
The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
       
       
       
Syntax:

       
           
def functionname( parameters ):

           
"function_docstring"

           
function_suite

           
return [expression]

       
       
By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

       
example:

       
The following function takes a string as input parameter and prints it on the standard screen.

       
           
def printme( str ):

           
"This prints a passed string into this function"

           
print (str)

           
return

       
   
   
       
Calling a Function
       
Defining a function gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

       
Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is an example to call the printme() function-

       
           
def printme( str ):

           
"This prints a passed string into this function"

           
print (str)

           
return

           
printme("This is first call to the user defined function!")

           
printme("Again second call to the same function")

           
           
This is first call to the user defined function!

           
Again second call to the same function

       
               
Pass by Reference vs Value
       
       
       
All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example-

       
       
           
def changeme( mylist ):

           
"This changes a passed list into this function"

           
print ("Values inside the function before change: ", mylist)

           
mylist[2]=50

           
print ("Values inside the function after change: ", mylist)

           
return

           
mylist = [10,20,30]

           
changeme( mylist )

           
print ("Values outside the function: ", mylist)

           
           
OUTPUT:

           
Values inside the function before change: [10, 20, 30]

           
Values inside the function after change: [10, 20, 50]

           
Values outside the function: [10, 20, 50]

           
       
   
   
       
Function Arguments
       
       
You can call a function by using the following types of formal arguments-

       
           
Required arguments
           
Keyword arguments
           
Default arguments
           
Variable-length arguments
       
       
       
Required Arguments
       
       
Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.

       
To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error

       
       
Keyword Arguments
       
       
Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.

       
This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the printme() function

       
       
Default Arguments
       
       
A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

       
       
Variable-length Arguments
       
       
You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

       
       
   
   
       
The Anonymous Functions
       
       
These functions are called anonymous because they are not declared in the standard manner by using thedefkeyword. You can use thelambdakeyword to create small anonymous functions.

               
           
Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
           
An anonymous function cannot be a direct call to print because lambda requires an expression.
           
Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.
           
Although it appears that lambdas are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is to stack allocation by passing function, during invocation for performance reasons.
       
       
Syntax:

       
           
lambda [arg1 [,arg2,.....argn]]:expression

           
           
example:

           
sum = lambda arg1, arg2: arg1 + arg2

           
print ("Value of total : ", sum( 10, 20 ))

           
print ("Value of total : ", sum( 20, 20 ))

           
OUTPUT:

           
Value of total :  30

           
Value of total :  40

       
   
     