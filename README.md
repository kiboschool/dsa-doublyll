# Doubly Linked List

In this practice, you will write a method to initialize the `prev` pointers of a doubly linked list.

## Starter Code

You are given the file `doublyll.py`, which includes the implementation of `DoublyLL` class that represents a string in a doubly linked list. Each node in the linked list contains a character `val`, a `next` pointer, and a `prev` pointer. It also includes:

* A constructor (`__init__`) for creating a doubly linked list that holds a string
* A `to_string()` method, which returns a string version of the `DoublyLL`
* A `reverse_string()` method, which returns a reversed version of the string represented by the `DoublyLL`

***You should not change any of the existing methods in the `LLString` class.***

## Steps to Complete

Your task is to implement the `init_prevs()` method. This method is expecting `self.head` to reference a doubly linked list in which all of the `next` pointers have been correctly initialized, but all of the `prev` pointers are `None`.

It is your task to initialize all the `prev` pointers of the list correctly: the first node's `prev` pointer should be `None`, the second node's `prev` pointer should reference the first node, etc.

Note: you don't need to call `reverse_string()` or `to_string()` as a part of your implementation of your method. They won't help you initialize the `prev` pointers -- they are there to test the result of your `init_prevs()` function after you're done.

## Testing

There are no unit tests, but there are some sample calls at the bottom of the `DoublyLL` class that you ran run by simply executing the `doublyll.py` file.

The sample calls show what the string version and reversed string version of the doubly linked list look like, both before and then after `init_prevs()` is called. To begin with, the output will look like this:

```
before calling init_prevs():
  original string: hello
  reversed string: o
after calling init_prevs():
  original string: hello
  reversed string: o
```

The reversed version of the string in each case only shows the last character because the `prev` pointers are not yet correctly initialized. Once they are correctly initialized, the output should be:

```
before calling init_prevs():
  original string: hello
  reversed string: o
after calling init_prevs():
  original string: hello
  reversed string: olleh
```
