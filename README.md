# "Why is my program so slow?!"

This is a beginners' exercise in Python performance.  I wrote it originally for the Client Services group at my company, [Luminoso](http://www.luminoso.com/), but maybe you'll find it interesting.  It's very short.

## HOWTO

All exercises are written for Python 3.  They do not require any libraries outside the Python standard library.  They have been tested on Linux, but probably run anywhere.

1. Clone the repo.

2. Choose an exercise and run it with `python3 ex<number>.py`.  The exercise should report that your output is correct, but that you won no medal.  (You might win a bronze medal accidentally if your machine is significantly faster than my test machine.)

3. Open the exercise file and read the code.  Modify the code between the comments reading `Make me faster!`; don't touch the code outside these comments.

4. Run the exercise file often to check on your progress.  Go for gold!

Rules:

* Your goal is to reproduce the *effect* of the code in the exercise, while (drastically) improving its *speed*.  Making it more concise is a nice bonus!
* Feel free to change the structure of the code in any way.  Maybe you should inline code; maybe you should factor it out; almost inevitably you need to change or remove at least one loop!
* Most refactors are "in bounds"; the only "cheats" I know of at this point, like hard-coding the expected output, are pretty obvious.
* The exercises are designed so that you can get "gold" without heroic efforts.

**NB**: The reference timings were established on a pretty average machine.  The kinds of optimizations I'm trying to teach are the sorts that gain factors of two or more, so I've built in a decent error margin.  That said, if you're on a much older machine and are close to but not at "gold", you might have reached the reference solution.  If you're on a fast machine, don't be surprised if you can beat "gold" by a lot!

## Principles of Optimization

In my experience, the three most important skills a programmer can acquire for performance tuning are:

1. **Think about what the computer is "physically" doing.**

2. **Know how the data structures of your language work.**

3. **Measure everything!**

