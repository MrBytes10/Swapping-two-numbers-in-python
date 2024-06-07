# Swapping Two Numbers in Python

This repository contains three Python scripts that demonstrate different methods to swap the values of two numbers.

## Method 1: Swapping with a Temporary Variable

The `method1_swapping_two_numbers.py` script uses a temporary variable to swap the values of two numbers. It follows these steps:

1. Declare the initial values of `num1` and `num2`.
2. Print the values of `num1` and `num2` before swapping.
3. Store the value of `num1` in a temporary variable `temp`.
4. Assign the value of `num2` to `num1`.
5. Assign the value stored in `temp` (the initial value of `num1`) to `num2`.
6. Print the swapped values of `num1` and `num2`.

## Method 2: Swapping with User Input

The `method2_swapping_two_numbers.py` script allows the user to input the values of `num1` and `num2` at runtime. It follows these steps:

1. Prompt the user to enter the values of `num1` and `num2` using the `input()` function.
2. Print the values of `num1` and `num2` before swapping.
3. Store the value of `num1` in a temporary variable `temp`.
4. Assign the value of `num2` to `num1`.
5. Assign the value stored in `temp` (the initial value of `num1`) to `num2`.
6. Print the swapped values of `num1` and `num2`.

## Method 3: Swapping without a Temporary Variable

The `method3_swapping_two_numbers.py` script swaps the values of `num1` and `num2` without using a temporary variable. It follows these steps:

1. Prompt the user to enter the values of `num1` and `num2` using the `input()` function.
2. Print the values of `num1` and `num2` before swapping.
3. Use tuple unpacking to swap the values of `num1` and `num2` in one line: `num1, num2 = num2, num1`.
4. Print the swapped values of `num1` and `num2`.

All three scripts demonstrate different approaches to swapping the values of two numbers in Python, with the third method using a more concise technique without a temporary variable.
