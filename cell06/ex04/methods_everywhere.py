


• You must create two different methods in this program:
• The method shrink takes a string as a parameter and displays the first eight
characters of that string.
Use slices.
• The method enlarge takes a string as a parameter and appends ’Z’ characters to
make it a total of eight characters. Then, it displays the resulting string.
Similar to arrays, you can add characters to a string using the
concatenation operator.
• For each argument of the program: if the argument has more than eight characters,
call the shrink method on it; if the argument has less than eight characters, call
the enlarge method on it; and if the argument has exactly eight characters, display
it directly followed by a new line.
• If the number of parameters is less than 1, display ’none’ followed by a new line.

?> ./methods_everywhere.py | cat -e
none$
?> ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e
lolZZZZZ$
physical$
backpack$
?>