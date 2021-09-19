# 1. Introduction to Python
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

In this section we introduce Python programming and present examples illustrating key language features. We can learn the syntax of `Python` in a few days, but learning to use a language is more than just learning the syntax. Building a pool of experience that lets us be an efficient programmer is usually tough -- as it requires working on good quality exercises for months, but it is doable and certainly very useful. 

We assume no prior knowledge of Python, but experience with programming concepts or another programming language will help, but is not required to understand the material. Alhough each programming language is different (though not as different as their designers would like us to believe), they can be related along some dimensions.

- **Low-level versus high-level** refers to whether we program using instructions and data objects at the level of the machine (something like move 64 bits of data from this location to another location) or whether we program using more abstract high level operations (like pop a menu on the screen) that have been provided by the language designer.

- **General versus targeted to an application domain** refers to whether the primitive operations of the programming language are widely applicable or are fine-tuned to a specific domain or machine. For example, `SQL` is designed for extracting information from relational databases, but you would'nt want to use it to build an operating system. SQL would be useless for that!!!

- **Interpreted versus compiled** refers to whether the sequence of instructions written by the programmer, called **source code**, is executed directly by a program called the `interpreter` that reads the code line by line and performs the specified action with code within the interpreter or whether it is first converted (by a `compiler`) into a sequence of machine-level primitive operations. There are adantages to both approaches. It is often easier to debug programs written in languages that are desgined to be interpreted, because then the interpreter can produce error messages that are easy to relate to the source code. 

Python is a **general purpose, interpreted, high-level programming language** that we can use effectively to build almost any kind of program that does not need direct access to the computer's hardware. 
 
```{note}
In this website, we use Python, however, this book is not meant to be about Python. It will certainly help us learn Python, and that's a good thing. But what we would like to focus on is how to write programs that solve problems. Once we figure that out then we can transfer our skill to any programming language.
```

Programming can dramatically improve our ability to collect and analyze information about the world, which in turn can lead to discoveries. In data science, the purpose of writing a program is to instruct a computer to carry out the steps of an analysis. Computers cannot study the world on their own, people must describe precisely what steps the computer should take in order to collect and analyze data, and those steps are expressed through programs. 


```{toctree}
:hidden:
:titlesonly:


workflow_1
workflow_2
workflow_3
```
