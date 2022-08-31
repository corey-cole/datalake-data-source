"""Patch Python path to allow pytest to find system under test"""
import os
import sys

TEST_DIR = os.path.dirname(__file__)
# Assumes 'tests' directory is at same level as 'src' directory
SRC_DIR = os.path.join(TEST_DIR, '../src')

sys.path.append(SRC_DIR)