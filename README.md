## Introduction to NST
NST is a stack-based language heavily inspired by the set theory - with built-in lazy evaluation, of course.

The core feature set hasn't been implemented yet. My suggestion is to avoid using NST.

Its raison d'etre is to build a stack-based language "component" that is about as competitive as [Husk](https://github.com/barbuz/husk).

* Pyth has CJam as a competitor;
* Jelly has 05AB1E as a competitior;
* Why doesn't Husk have a stack-based language competitor?
## How to run the interpreter
It's quite simple: `python prefix.py [your-file]`. Enter all of your input in STDIN, ending with an EOF character.
## Core goals
* One of the core goals of NST is *accuracy*. The language has to be
capable of expressing the question accurately without abusing the
question's subtleties, 

* The second goal was being high-level. The langauge should be
concise in a high-level way, allowing the user to specify the question 
directly by describing the question to the computer.
