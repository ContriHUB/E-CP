# E-CP

A **CLI tool** with a variety of features to help in practicing competitive programming problems.

### Features: 

+ Create dedicated folders for a specific problem, with output and expected files
+ Create test sessions for a specific problem
+ Default code template can be added
+ Cpp and Python supported

## Getting Started

## How to run locally?

* [Install Python](https://www.wikihow.com/Install-Python) with version >= 3.9.13
* [Install virtualenv](https://pypi.org/project/virtualenv/) globally
    ```
    pip install virtualenv
    ```
* Clone this repository
    ```
    git clone https://github.com/ContriHUB/E-CP.git
    ```
* Create Virtual Environment
    ```
    virtualenv <env_name>
    ```
* Activate the environment
    * On Windows, run: `<env_name>\Scripts\activate`
    * On Linux/Mac, run: `source <env_name>/bin/activate`    
* Install the dependencies
    ```
    pip install -r requirements.txt
    ```
* Change directory to *E-CP*
    ```
    cd E-CP
    ```
* To install the CLI tool in your local computer (in editable mode). This will use setuptools module to install the cli tool in the current virtual environment. Read more about setuptools and editable mode from [here](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
    ```
    pip install --editable .
    ```
* Now, you can use the CLI tool in the current environment. Try some commands:
    ```
    ecp problem https://codeforces.com/contest/1739/problem/A .
    ```

## Steps to contribute -
* Fork this repo and clone it to your system.
* Get the issue assigned to you on the ContriHUB website. 
* Make the required changes. Please keep your changes relevant only to the issue specified.
* Add your name to [CONTRIBUTORS.md](CONTRIBUTORS.md).
* Create a PR with your changes and a detailed description of the changes you have made. 
* Submit the PR link on the ContriHUB website.

## Contributors

A list of contributors can be found in [CONTRIBUTORS.md](CONTRIBUTORS.md).

## Maintainer

- [Alok Kumar Singh](https://github.com/akstron)