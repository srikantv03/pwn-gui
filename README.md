# Pwn Gui

Graphical user interface for the pwn tools library.

## How to install
Run the following command into your command line to install:

```
sh <(wget -qO- https://raw.githubusercontent.com/treecant/pwn-gui/master/init.sh)
```

If you already have any of the dependencies that are being installed in the script, you won't run into errors by attempting to "reinstall" them through the script

## How to use

Features are constantly being added to this project, and this readme will also be updated accordingly

- Basic Interactive Connection

To enable interactive mode (just as you would by using netcat in your terminal), click the checkbox labeled "interactive", type the hostname in the "hostname" textbox and the port number in the "port" text box. 

The gui will print all the outputs from the server and you will be able to input anything back until the process is terminated

- Basic Code Injection

To inject code as your input, click the checkbox labeled "code injection" and input your hostname and port number as with interactive mode

Before the connection is made, you will be asked to define a function named "return_value()"

In this function, you will have to return whatever value you want to send back through the socket (it will be converted before it is sent)

## Coming Soon

Currently working on the following features:
 
- Python shell functionality

With basic python shell functionality in this gui, this gui can act as an all in one hub for testing and injecting code into ctf challenge servers

- Combinantion (injection and interactive) mode

This will allow you to test string inputs as well as send cached code outputs directly to the server

- Flag Detection

Using the tools given with the pwn library, this gui will have flag detection at the user's fingertips, allowing them to recursively search for the flag string at the click of a buttton.
