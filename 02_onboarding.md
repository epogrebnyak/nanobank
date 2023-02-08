# Ask for the input and print the output

`input()` and `print()` are standard library functions that allow dialog interfaces:
your program asks for some input from a user, processes it and prints an output.

Here is a minimal code that will prompt you to type a string, save a string
to variable `name`, change this variable by capitalizing first letters
in each word and print the resulting variable to screen.

```python
name = input("What is your name?")
name = name.capitalize()
print("Name:", name)
```

Technical note

`input()` is just one of the ways a user can enter data into a program. Using this function is popular for teaching programming, as it allows to quickly see the results and encourages experimention. However, in actual programs, other methods such as command line arguments, reading from files or internet sources, or connecting to a database are often more practical.

You may consider `input()` a step in your learning that you are not likely to use very often in the future. On the contrary `print()` is used extensively in programs -- you are likely to write it a lot in your programs.

## Code excercises

### Easy to start (beginner)

1. Is there a greeting that a system may print at start of the program?
   Can you implement such a greeting?

2. Ask a new bank customer for name, city and deposit amount and print the result to screen.

### Requires planning and research (intermediate)

3. Would you know how to account for different spelling of city names? Consider restricting
   a city name to a fixed list of cities. Depending on a bank that you envisage
   the cities may be the country largest cities, smaller cities in some region,
   city districts or maybe some international offices. Keep it a short list of up to 5-7 cities.

4. Add a signup bonus for the customer that increases the deposit amount
   by a small percentage (for example 0.01%) or a fixed sum or a combination of the two.
   Note that you would need to convert a string to a number for this calculation.

5. The reverse of a bonus is an account fee, applied much more frequently than giving a bonus.  
   Calculate and print monthly or annual fee estimate. The fee may be flat or vary based
   on amount deposited into account, for example -- there is no fee up to some threshold or no fee if a minimum account balance is maintained.

6. You may add an encouraging note that paying a fee gives some privileges or extra services --
   placing a small advertisement in the program output.

### A bit more demanding (one notch above)

7. Prompt a user about close matches of a city name if it is not exact.
   For example you may use [diff.get_close_matches](https://docs.python.org/3/library/difflib.html#difflib.get_close_matches) for this.

8. Consider a policy where the signup bonus or fee differs by city. Is this legally allowed?
   How it can be implemented in code?

9. Bonus points if you match fee policy to a real bank and provide a fee schedule found on  
   a bank website. Provide a link to a fee schedule together with your code. If the schedule is too complex, implement just a part of it.

10. You may want to colorize the prompt or output or hide the input when entering secret information
    such as passwords. You can use [rich](https://github.com/Textualize/rich) library.

11. What name should we use in an example? What is we are out of imagination? Let's generate it with [faker](https://faker.readthedocs.io/en/master/) library.
