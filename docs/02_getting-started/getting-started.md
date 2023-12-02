---
layout: default
title: Getting Started
permalink: /getting-started
has_children: false
has_toc: false
nav_order: 2
---

# Getting Started Guide

Welcome to the Vibe Beyond! This guide will help you get up and running with the project in no time. By following these steps, you'll be able to install the project, configure it, and start using its awesome features.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Python](https://python.org) (3.11.0 preferred)
- [pip](https://pip.pypa.io/en/stable/getting-started/) (22.3 - 23.0.1)
- [Git](https://git-scm.com/downloads)

## Installation

1. Clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/dariustb/VibeBeyond.git
   ```

2. Navigate to the project's directory:

   ```bash
   cd /path/to/VibeBeyond
   ```

3. Create a virtual environment with `venv`:

   ```bash
   python -m venv venv
   source venv/path/to/activate
   ```
   > The path to `activate` depends on your system. I used `venv/Scripts/activate`. For more information, view [Python's venv documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

4. Install dependencies with `pip`
   ```bash
   python -m pip install -r requirements.txt
   ```

🎉 Now your program is ready to run! See [How to Use](../03_usage/how-to-use.md) for steps on using the app.
