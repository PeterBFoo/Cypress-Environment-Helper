## About code signing the executable

---

If you ever want to distribute and use this script in your business or share it with your co-workers, you will have to sign the executable that you compile after running pyinstaller.

¿Why's that so important? For the operative system, it really do. This is one of the ways to make the operative system think that this file is not malicious, otherwise will likely block the script and put it under quarentine. To code sign are used some tools as **codesign** in macOS and **signtool** for Windows.

You will need to generate a certificate with the data of the company or yourself if you are a certificated developer, then use one of the tools depending on which OS you are going to distribute. ¡Then you are ready to roll!

I will leave you some code that will help you, to at least, generate the certificate using Python, you can check it [here](/doc/code_sign/CreateCert.py)