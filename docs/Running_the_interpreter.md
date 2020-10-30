To run NST, you specify a template:
```
python prefix.py [your-file]
```
Change `python` to wherever your python interpreter is.
## How do I specify input though?
If you entered like the what template does, you will see the intepreter prompting you for input.

Enter your input on separate lines, end your input with an empty newline.

Each of your lines will be evaluated as Python code, with access to functions defined in `lazy.py`.
## What is the output like?
For every item on the resulting parsing stack, they're outputted after joining with newlines.

For every item *on* the stack (it's always an iterable), it joins them with spaces.

That makes it output like a 2D matrix, which makes it easier to view the items on the stack.
