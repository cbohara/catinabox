# catinabox - Intro to Testing and Test Automation in Python
[![Build Status](https://travis-ci.org/keeppythonweird/catinabox.svg?branch=master)](https://travis-ci.org/keeppythonweird/catinabox)

Coverage status:
* Master (test stubs only): [![Coverage Status (Pre tests)](https://coveralls.io/repos/keeppythonweird/catinabox/badge.svg?branch=master&service=github)](https://coveralls.io/github/keeppythonweird/catinabox?branch=master)
* [Solutions branch](https://github.com/keeppythonweird/catinabox/tree/solutions) (all tests added): [![Coverage Status (Post tests)](https://coveralls.io/repos/keeppythonweird/catinabox/badge.svg?branch=solutions&service=github)](https://coveralls.io/github/keeppythonweird/catinabox?branch=solutions)

Accompanies the [Intro to Testing and Test Automation in Python slide deck](https://docs.google.com/presentation/d/1cNgZdkw2cik4i4Mc1Ka7frPAdZky3hwpq0vycBDMufE/edit). Aesthetic inspired by [@sailorhg](https://twitter.com/sailorhg).

![catinabox](pics/catinabox.png)

This repo holds a tutorial which will walk you through adding unit tests,
exploring these features of unit testing in general and pytest in particular:
- Basic unit testing
- Observing test success and coverage using
  [Travis CI](https://travis-ci.org/) and [coveralls](https://coveralls.io/).

# Requirements

1. Github accounts
2. Python (2.7 or 3.x) with:
  - pip
  - virtualenv
5. Git (either Github for Windows or command-line git)
6. Text editor or IDE (e.g. Pycharm)

# Tutorial Steps

1. [Setup and run tests](./steps/1-run_tests.md)
2. [Test a simple function](./steps/2-simple_function.md)
3. [Create and build a pull request](./steps/3-pull.md)
4. [Testing incorrect input](./steps/4-input.md)
5. [Testing classes with fixtures](./steps/5-classes.md)
6. [Using mock and patch](./steps/6-mock.md)
7. [Parameterized tests](./steps/7-params.md)
8. [Refactoring for unit testability](./steps/8-refactor.md)

Solutions are visible by viewing [the solutions branch](https://github.com/keeppythonweird/catinabox/tree/solutions).

![cattery](pics/cattery.png)


coverage
    * statement coverage
        was this line executed?
        ex: were all the lines in the function executed?
    decision coverage
        was every code path executed?
        ex: if there are lots of conditionals, want to make sure all the conditionals are checked
    condition
        was every part of the decision executed?
        ex: if there are 2 conditions within 1 if statement, make sure both conditions are executed

what are unit tests good for?
    find bugs WHILE your developing
    design tool = TDD
    more maintainable code
    documents intentions
    run quickly

what are unit tests not good for?
    document what you thought your code should do
    can only catch the bugs you are aware of
    only test in isolation
    unit tests are not best suited for glue code! aka automation

unit test structure
    1. define your inputs and any preconditions
    2. invoke the function
    3. vertify that the function worked as expected

fixtures
    setup and teardown
    provide fresh fixture for each test
    ex: pass a list to each test - provide a fresh version of the list to each test - not modifying the same list

mocking
    create "mock" object that behaves like the one you are calling

    stop unit tests from doing costly operations
    ex: pretend to sleep and not have to wait for the sleep() to happen

    use mocking for unit test but supplement with system tests to ensure the system actually works

patching
    setup mocks and clean up when done
    mocker.patch.object(autospec=True) will raise exception if used incorrectly

parameterization
    allows you to pass in a bunch of inputs into 1 test to avoid building out a bunch of separate tests

* if it is hard to write a unit test for the code it usually means the code should be refactored
* if the code can be tested with a unit test = higher quality code
