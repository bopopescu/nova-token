begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Maintainer: Jonathan Lange'
nl|'\n'
nl|'\n'
string|'"""\nAsynchronous unit testing framework.\n\nTrial extends Python\'s builtin C{unittest} to provide support for asynchronous\ntests.\n\nMaintainer: Jonathan Lange\n\nTrial strives to be compatible with other Python xUnit testing frameworks.\n"Compatibility" is a difficult things to define. In practice, it means that:\n\n - L{twisted.trial.unittest.TestCase} objects should be able to be used by\n   other test runners without those runners requiring special support for\n   Trial tests.\n\n - Tests that subclass the standard library C{TestCase} and don\'t do anything\n   "too weird" should be able to be discoverable and runnable by the Trial\n   test runner without the authors of those tests having to jump through\n   hoops.\n\n - Tests that implement the interface provided by the standard library\n   C{TestCase} should be runnable by the Trial runner.\n\n - The Trial test runner and Trial L{unittest.TestCase} objects ought to be\n   able to use standard library C{TestResult} objects, and third party\n   C{TestResult} objects based on the standard library.\n\nThis list is not necessarily exhaustive -- compatibility is hard to define.\nContributors who discover more helpful ways of defining compatibility are\nencouraged to update this document.\n\n\nExamples:\n\nB{Timeouts} for tests should be implemented in the runner. If this is done,\nthen timeouts could work for third-party TestCase objects as well as for\nL{twisted.trial.unittest.TestCase} objects. Further, Twisted C{TestCase}\nobjects will run in other runners without timing out.\nSee U{http://twistedmatrix.com/trac/ticket/2675}.\n\nRunning tests in a temporary directory should be a feature of the test case,\nbecause often tests themselves rely on this behaviour. If the feature is\nimplemented in the runner, then tests will change behaviour (possibly\nbreaking) when run in a different test runner. Further, many tests don\'t even\ncare about the filesystem.\nSee U{http://twistedmatrix.com/trac/ticket/2916}.\n"""'
newline|'\n'
endmarker|''
end_unit
