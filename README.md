# Pwn Gui

Graphical user interface for the pwn tools library.

## How to install

Paste the following code into a shell script (.sh file):
```
git clone http://github.com/treecant/pwn-gui.git
sudo apt install python3-pip
pip3 install pwn
cd pwn-gui
python3 main.py
```
To run the script, paste the following code in the terminal 
```
chmod +x <script name>
./<script name>
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

