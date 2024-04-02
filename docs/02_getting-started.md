---
layout:       default
title:        Getting Started
permalink:    /getting-started
has_children: false
has_toc:      false
nav_order:    2
---

# Getting Started Guide
This guide will allow you to start running the project on your machine.

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- Git (2.34.1)
- Cmake (3.29.0-rc2)
- Ubuntu Linux (or any official flavor)

## Installation
1. Clone the repository to your local machine using Git:
    ```sh
    git clone https://github.com/dariustb/VibeBeyond.git
    ```
2. Navigate to the project directory:
    ```sh
    cd /path/to/VibeBeyond
    ```
3. Build the executable using cmake:
    ```sh
    mkdir build
    cd build
    cmake .. && make
    ```
4. Run executable
    ```sh
    src/vibebeyond
    ```
Now your program is ready to run! See [How to Use](03_how-to-use.md) for steps on using the app.
