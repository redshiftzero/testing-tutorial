:title: Testing
:author: jen, jon
:description: Test Driven Development 
:keywords: testing, development
:css: style.css

----

Testing
=======

----

Why test
========

* You want to verify that your code is correct 

* You want to find sneaky bugs

* You want to be sure you don't break existing functionality as you add new features (regression) 

----

Tests are a safety net
======================

----

Writing tests helps you write good code
=======================================

* Designing good tests 

* Test-Driven Development (TDD) is a style where you first write failing tests, then write the code to get the tests to pass.  

----

Testing in Python
=================

* blah




----

When to run your test suite
===========================

* You should run your tests often

* You should run your tests when a PR is submitted

* Enter Travis!

----

Travis
======



----

Selenium + Nightwatch
=====================

Selenium automates web browsing
* (all the  complicated scraping you could want)
* but can be used for testing web-based interfaces

Nightwatch is a node.js-based browser testing solution

----

Nightwatch code
===============

.. code:: js

  'Test background check' : function (browser) {
    browser
    .waitForElementVisible('input#email', 1000)
    .setValue('input#email', 'nightwatch@jonkeane.com')
    ...
      .pause(500) // for safari
      .waitForElementVisible('button#languageBGSubmit', 1000)
      .click('button#languageBGSubmit')
      .waitForElementVisible('button#continue', 10000)
      .assert.containsText('body', 'Now we\'re ready to start the experiment, first let\'s try a few practice items.')

----

Testing in R
============

* blah

----

References
==========

* Ned Batchelder, Getting Started Testing, PyCon 2014: https://www.youtube.com/watch?v=FxSsnHeWQBY
* testthat (with R package development backdrop): http://r-pkgs.had.co.nz/tests.html
* Nightwatch(with selenium): http://nightwatchjs.org/guide#running-tests
