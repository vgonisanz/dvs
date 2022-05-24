#!/usr/bin/env python

"""Tests for `dvs` package."""

import dvs

def test_package_publishes_version_info():
    """Tests that the `dvs` publishes the current version"""

    assert hasattr(dvs, '__version__')
