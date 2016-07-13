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

Nightwatch example
==================

.. code:: js

  'Test background check' : function (browser) {
    browser
    .waitForElementVisible('input#email', 1000)
    .setValue('input#email', 'nightwatch@jonkeane.com')
    [assert all the things]
    .pause(500) // for safari
    .waitForElementVisible('button#languageBGSubmit', 1000)
    .click('button#languageBGSubmit')
    .waitForElementVisible('button#continue', 10000)
    .assert.containsText('body', 'Now we\'re ready to start the
      experiment, first let\'s try a few practice items.')

----

Testing in R
============

The tidy-verse solution is `testthat` (although there are others). The easiest way is to work within a package-framework.

* tests go in ``tests/testthat/test*.R`` 
* need the file: ``tests/testthat.R``: 

		.. code:: R

		  library(testthat)
		  library([package name])
		  test_check("[package name]")


----

R example
=========

.. code:: R

  context("distance calculationss")
  load(file.path('extractedMarkerData.RData')) # markerDataHead
  load(file.path('dist57.RData')) # dist57head
  load(file.path('meanData.RData')) # meanDataHead

  test_that("calculateDistances returns the correct distances", {
    expect_equal(calculateDistances(markerDataHead, c(5,7)),
                 dist57head)
  })

  test_that("meanOnAxis returns the correct distances", {
    expect_equal(meanOnAxis(markerDataHead,
                            c(0, 1, 2, 3, 4),
                            axis ="Y"),
                 meanDataHead)
  })
  


----

R example (cont.)
=================

.. code:: R

  context("writeCSVsFromData")

  test_that("writeCSVsFromData will overwrite", {
    expect_message(writeCSVsFromData(pureReplication))
  })
  test_that("writeCSVsFromData checks for existing files", {
    expect_error(writeCSVsFromData(pureReplication,
                                   overwrite=FALSE))
  })
  
  context("checkData runs silently")
  test_that("checkData silently returns the data object 
             it was presented",{
    expect_silent(checkData(pureReplication, 
                  modelMd = modelMetadata))
    expect_equal(checkData(pureReplication, 
                 modelMd = modelMetadata),
                 pureReplication)
  })

----


References
==========

* Ned Batchelder, Getting Started Testing, PyCon 2014: https://www.youtube.com/watch?v=FxSsnHeWQBY
* testthat (with R package development backdrop): http://r-pkgs.had.co.nz/tests.html
* Nightwatch(with selenium): http://nightwatchjs.org/guide#running-tests
