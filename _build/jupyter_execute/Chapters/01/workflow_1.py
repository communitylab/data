# Basic Python Data Types
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

One of the most basic feature of Python is that it is a [**Object-oriented programming language**](https://en.wikipedia.org/wiki/Object-oriented_programming), which means everything inside Python is an **object**. When we write programs, we essentially specify a set of actions to perform that manipuates the **object** in some capacity. Sometimes we even call the object as `value`, and each value is a piece of data that a computer program works with such as a number or text. There are different **types** of values: 42 is an integer and "Hello!" is a string. 

A **variable** is a just name that refers to a value, it gives us a way to associate names with objects. In mathematics and statistics, we usually use variable names like $x$ and $y$. In Python, we can use any word as a variable name as long as it starts with a letter or an underscore. However, it should not be a [reserved word](https://docs.python.org/3.3/reference/lexical_analysis.html#keywords) in Python such as `for`, `while`, `class`, `lambda`, etc. as these words encode special functionality in Python that we don't want to overwrite!

```{note}

Although we mentioned that a variable is just a name, its not that simple. Programming languages let us describe computations so that computers can execute them, but this does not mean only computers have to read programs. It's often best to write programs that are easy to read and an apt choice of variable names plays an important role in enhancing readability. You can read more about them [here](https://towardsdatascience.com/data-scientists-your-variable-names-are-awful-heres-how-to-fix-them-89053d2855be).

```

It can be helpful to think of a variable as a box that holds some information (a single number, a vector, a string, etc). We use the **assignment operator** `=` to assign a value to a variable. An [assignment statement](https://en.wikipedia.org/wiki/Assignment_(computer_science)) associates the name to the left of the = symbol with the object denoted by the expression to the right of the = symbol. 

```{figure} box.png
---
width: 75%
name: Variables
alt: Python Variables.
---
Python Variables.
```

Image taken from: [medium.com](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40stevenpcurtis.sc%2Fwhat-is-a-variable-3447ac1331b9&psig=AOvVaw3YbYfgb7XFOJ_sHP5eliob&ust=1595365663851000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCMi8nrfe3OoCFQAAAAAdAAAAABAZ)


```{admonition} Common built-in Python data types 
---
class: dropdown
---
See the [Python 3 documentation](https://docs.python.org/3/library/stdtypes.html) for a summary of the standard built-in Python datatypes (`dtype` for short). In later chapters we will look into all of them as we use them to build simple programs.
$\qquad$

| English name          | Type name  | Type Category  | Description                                   | Example                                    |
| :-------------------- | :--------- | :------------- | :-------------------------------------------- | :----------------------------------------- |
| integer               | `int`      | Numeric Type   | positive/negative whole numbers               | `42`                                       |
| floating point number | `float`    | Numeric Type   | real number in decimal form                   | `3.14159`                                  |
| boolean               | `bool`     | Boolean Values | true or false                                 | `True`                                     |
| string                | `str`      | Sequence Type  | text                                          | `"I Can Have KFC?"`                 |
| list                  | `list`     | Sequence Type  | a collection of objects - mutable & ordered   | `['Ali', 'Sophia', 'Meghan']`               |
| tuple                 | `tuple`    | Sequence Type  | a collection of objects - immutable & ordered | `('Thursday', 14, 4, 2021)`                 |
| dictionary            | `dict`     | Mapping Type   | mapping of key-value pairs                    | `{'name':'Harry', 'code':007, 'credits':9}` |
| none                  | `NoneType` | Null Object    | represents no value                           | `None`                                     |
$\qquad$
**This table shows some of the built-in data types in Python along with examples of using them.**

```

## Numeric data types

There are three distinct numeric types: **integers, floating point numbers**, and **complex numbers** (not covered here). We can determine the type of an object by using Python's in-built function `type()`. We can print the value of the object using another in-built function `print()`. You can find Pythons inbuilt functions [here](https://docs.python.org/3/library/functions.html). A [function](https://www.w3schools.com/python/python_functions.asp) is simply a set of code lines which can take some input, do processing on it and return some output. We will learn more about functions later on, but for now...

Let's create a variable named x that stores the integer 7, which is the variable's value:

x = 7
type(x)

The snippet **$x$=7** is a statement. Each statement specifies a task to perform. The preceding statement creates **$x$** and uses the `assignment symbol` **(=)** to give **$x$** a value. The entire statement is an assignment variable that we read as "x is assigned the value 7". The following statement creates a variable $y$ and assigns to it the value 42. We will even use the print() function to see what its value is:

y = 42
print(y)

In Jupyter/IPython (an interactive version of Python, through which this content was written), the last line of a cell will automatically return as an output and so we don't actually need to explicitly state print().

y # Anything after the pound/hash symbol is a comment and will not be run

Python allows multiple assignment as well. The statement

```python
x, y = 1, 2
```
binds x to 1 and y to 2. All of the expressions on the right-hand side of the assignment are evaluated before any bindings are changed. This is convenient since it allows us to use multiple assignment to swap the bindings of two variables.

For examples, the code

```python
x, y = 1, 2
x, y = y, x
print('x =', x)
print('y =', y)
```
will print

```python
x = 2
y = 1
```

pi = 3.14 # assigning a decimal point number results in a float type
type(pi)



````{admonition} Consider the code

``` python
pi = 3
radius = 11
area = pi * (radius**2)
radius = 14
```

````

The code first `binds` the names **pi** and **radius** to different objects of type int. It then binds the name **area** to a third object of type int. This is depicted on the left side of figure below.


```{figure} binding.png
---
width: 75%
name: Variable Assignment
alt: Variable Assignment.
---
Variable Assignment.
```

If the program then executes **radius = 14**, the name radius is rebound to a different object of type int as shown on the right side. 

```{note}
This assignment has no effect on the value to which area is bound, it will still keep denoting the object by the expression `3*(11**2)`
```

## Arithmetic Operators

The code above showed example of arithmetic operator, below is a table of the syntax for common arithmetic operations in Python:

| Operator |   Description    |
| :------: | :--------------: |
|   `+`    |     addition     |
|   `-`    |   subtraction    |
|   `*`    |  multiplication  |
|   `/`    |     division     |
|   `**`   |  exponentiation  |
|   `//`   | integer division / floor division |
|   `%`    |      modulo      |

Let's have a go at applying these operators to numeric types and observe the results.

1 + 2 + 3 + 4 + 5  # add

11 * 3.14159  # multiply

2 ** 10  # exponent

```{caution} 
Division may produce a differnt dtype than expected, it will change int to float
```

num = 5
type(num)

num / num  # divison

When we use the syntax `//`, it allows us to do "integer division" and retain the int data type. It gives us the quotient after division. 

50 / 3

50 // 3

type(50 // 3)

We call this the `integer division` because its like calling the int function on the result of the division.

int(50 // 3)

```{margin}
Watch the following video to learn more about Casting
```

```{admonition} **Casting in Python**
---
class: dropdown
---
<iframe width="640" height="360" src="https://www.youtube.com/embed/ALvbltAPOcI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


The `%` is called the `"modulo"` operator and this gives us the remainder after doing the division. In case you are wondering how its spelled, we call the below operation as `50 mod 3`

50 % 3

We can also perform the modulo operation on objects of `float` type.

50.5 % 3

## Strings

Much of data is not stored in the form of numbers, but as text, which is represented in a computer in the form of a string. We can think of string as a sequence of characters, that can represent a word, a sentence, or even the contents of every book in a library. 

We write strings as characters enclosed with either:
  - single quotes, e.g., `'Data'` 
  - double quotes, e.g., `"Science"`
  
There is no difference between the two methods, but there are some cases where it's useful to have them both.

We can even add two strings together and the result will also be a string, for instance, adding two strings together produces another string. This expression is still an addition expression, but it is combining a different type of value.

'Data' + "Science"

The addition operator + is said to be **overloaded** as it carries different meaning depending on the type of object it works on. When its used on numeric type it means addition, but when used for strings it means concantenation. In the above example it combines these two strings without regard for their contents. It doesn’t add a space because these are different words; that’s up to the programmer (you) to specify. We can add space between words by using an empty string with space.

'Data' + ' ' + 'Science'

"""
Everything enclosed inside triple quotes is considered to be a multi-line
comment and will not be executed
"""
'Python' + 3

````{note}

We cannot concatenate an integer to string, we will first need to cast the integer into a string by using str() or enclosing the integer inside quotes, for example,

```md
'Python' + str(3) 
```  

or

```md
'Python' + '3'
```
````

Double-quoted strings could be useful in certain situations like

"I can't use single-quoted strings here"

quote = 'Tony Stark: "I am Iron Man."'
print(quote)
type(quote)

## None

There are special object in Python that has no value, we call this type as `NoneType`. This type has only one possible value - `None`

x = None

print(x)

type(x)