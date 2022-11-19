Think as a tester
=================

Learning Goals
--------------

* Have an idea how different mindsets affects what 
  tests are written
* Experience how to add new test cases by thinking in new patterns

Session Outline
---------------

* 5 min Connect: Developers compared to developers
* 10 min concept: Testing mindset
* 35 min concrete: Create test cases for weigh station
* 5 min conclusions: How does the mindset make you find new issues


Connect
-------

How would a user use software differently from the developer that
created it? 


Consept
-------

Explain the idea behind exploratory testing, how you as a tester
could learn about how the software works. How this way of testing
is a intellectual exersice in learning about the product. How one
can combine this with adding scripted testing or using scripts to
learn the behaviour of the code. Why this could be more described
as a mind-set of the tester than a methodology.

Talk about the role of a tester, question how the application
works for the users. The need for the software to prove its
working that it has bug unless it can prove it self free
of issues. The need to get your self into the mind of the user,
and not only on the level of the user would like to order a book
so I make a test that orders a book. I like to refer to Blake
Norris [article](https://medium.com/@blakenorrish/how-to-think-like-a-tester-7a174ff6aeaf).


Concrete
--------

Using the kata [weight station](https://github.com/balp/weigh_station),
I'm pairs work on finding issues with the current implementation.

One can find the issues either using mostly exploratory testing on
with the web-interface and a rest api client. There is a simple python
applications that can call the API and .http files that can be used form
inside PyCharm or Visual Studio Code with the extension REST Client,
suggested when one open a .http file the first time.

Or adding more tests to the unit tests. Mostly these can be added in the
`tests/test_view_default.py` file.

If needed ask some questions:

* What should happen if a lorry have negative load?
* Can there be a half lorry?
* How do we change the name of a weigh station?
* What happens when a second weigh station starts to report lorries?


Conclusions
-----------

* What kind of issues have you found?
* Did you learn anything new?
* How does this reflect to your normal writing of unit-tests?
