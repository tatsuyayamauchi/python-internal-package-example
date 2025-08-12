# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python internal package distribution example that demonstrates how to create and distribute internal Python packages. The planned structure includes:

- **example/main.py**: Main application code that imports and uses pkgfoo and pkgbar packages
- **pkgfoo**: Internal package providing `foo(val: string)` function 
- **pkgbar**: Internal package providing `bar()` function, which internally uses pkgfoo's foo function

## Python Environment

- Python version: 3.13.6 (managed via .tool-versions file, likely using asdf or similar)
- This appears to be a fresh repository with planned package structure but no implementation yet

## Development Setup

Since this is an internal package distribution example, future development will likely involve:

1. Creating package directories (pkgfoo/, pkgbar/, example/) 
2. Setting up proper Python package structure with __init__.py files
3. Configuring package dependencies and installation via setup.py or pyproject.toml
4. Implementing the cross-package dependency (pkgbar using pkgfoo)

## Repository Context

- Language: Primarily Japanese documentation
- Purpose: Educational/example repository for internal Python package distribution
- Status: Initial setup phase - core implementation not yet present