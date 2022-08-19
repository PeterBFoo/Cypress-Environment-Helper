# Cypress Environment Helper

---

## **_¿What's this?_**

I made a script ready to run in Mac (soon able in Linux and Windows distributions), it's just as easy as it gets: download the executable and fill the information that the program needs.

This program configures the environment variables you need to use Cypress without having so much trouble, there are 5 of those:

- **CYPRESS_RUN_BINARY**: You tell Cypress to use the Cypress.exe that you have in your machine, instead of installing via npm (useful for strong network restrictions if you are in an enterprise).
- **CYPRESS_INSTALL_BINARY**: You can decide if you want to install Cypress or not, that value is "0 npm install", recomended to set it when you want to declare the CYPRESS_RUN_BINARY variable.
- **CYPRESS_CACHE_FOLDER**: If you are using an user that doesn't have administrator permissions, you can have trouble with accessing the cache folder that your OS uses for installing Cypress. You can set another folder for Cypress to run there the files that would put in the other cache directory, here you have to put the path to that directory.
- **HTTP_PROXY**: Here you set the URL of your proxy.
- **NODE_EXTRA_CA_CERTS**: Here you have to put the the path to the certificate file that the proxy needs to access, download files, etc.

<br>

## **_¿How do I run it?_**

You can run it via Python shell or via the executable that is in the release section (no worries, if it's not there... It will be there soon!).

Python (in the root of the project)

    python3 CypressEnvironmentHelper.py

But I recommend you to run it with the executable, the program detects the path where the executable Is and (if you need It) creates the cache folder there.

In order to run the executable, is better to compile it in your machine and then place it in a project where you use Cypress, so let's get to it:

- First of all, create an virtual environment with Python:

    python3 -m venv venv

- Activate the virtual environment

    source venv/bin/activate

- Then, install the dependencies that the Python script needs with pip:

    pip install -r requirements.txt

- And last, use Pyinstaller to generate the executable

    pyinstaller --onefile --windowed CypressEnvironmentHelper.py

This last command will create two folders (build and dist) and a .spec file. Go to the dist directory and there you will have your executable (CypressEnvironmentHelper).

<br>

## **_How the program works_**

The program starts asking to the user what information wants to set to each environment variable. After that, the program detects the OS of the user (via the platform library) and runs the appropiate modules that have the configuration for that OS, in Windows is actually pretty simple:

You just have to type a command that indicates the scope of the environment variable, it's name and value; but in Mac or Linux, things changes.

First of all, I had to check which shell the OS uses by default, because in macOS 10.15 Catalina the default shell changed from bash to zsh. This causes that the program has to write in diferent files depending on that (on bash is the .bash_profile, and in zsh .zshrc).

Then, when the program runs has to check if that variable is already setted in the file, in case that is already setted it does change it. Imagine that you are just configuring 3 of them, so the program will write all the variables that are available and put an empty value to those that are "Not Configured".

And last, displaying the current state of the applied configurations.

<br>

### **About distribution and use**

Feel free to use and distribute the program, I would be honored to see that someone wants to improve the program, so please do it without hesitation!
