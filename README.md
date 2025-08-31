## Tower-of-Hanoi

This Python script solves the classic Tower of Hanoi puzzle using an iterative approach with a stack. It simulates the recursive algorithm without using actual recursion, making it easier to understand stack behavior in problem-solving.

---

## Problem Statement

The Tower of Hanoi is a mathematical puzzle where you have three rods and N disks of different sizes which can slide onto any rod. The puzzle starts with the disks stacked in ascending order of size on one rod. The goal is to move the entire stack to another rod, obeying the following rules :

- Only one disk may be moved at a time.

- Each move involves taking the top disk from one stack and placing it on another stack.

- No disk may be placed on top of a smaller disk.

---

## How This Works

Instead of solving the problem recursively, this program uses a manual stack to simulate recursion. Each stack frame holds the following :

- n : Number of disks to move

- source : The source peg

- destination : The destination peg

- auxiliary : The auxiliary peg

- state : A marker to determine what part of the process we’re in (before or after the main disk move)

---

## Why Use Iterative Approach?

- Avoids recursion limits

- Great for understanding how recursion works behind the scenes

- Reinforces how stack data structures simulate function calls

---

## Author

Abhinav Dixit

---

## License

This project is licensed under the MIT License

---
