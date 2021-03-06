# Flasknado! #

A trivial demonstration of using [Tornado][] and [Flask][] together.

[Tornado]: http://www.tornadoweb.org
[Flask]: http://flask.pocoo.org/

## Why? ##

Tornado is a very powerful and flexible asynchronous HTTP server with
support for things like websockets. Meanwhile, Flask is a fantastic
web microframework that makes writing web applications fun and
easy. Flasknado! then demonstrates how to use Tornado to run a Flask
WSGI app to exploit the strengths of both.

## Install ##

* **$** `sudo pip install virtualenv`
* Clone repo
* **$** `cd flasknado`
* **$** `virtualenv venv`
* **$** `. venv/bin/activate`
* **$** `pip install -r pipfile`

## Use ##

* Note: Your shell must be in the `venv` environment to run.
* **$** `python flasknado.py`
* http://localhost:8080
* `Ctrl/Cmd + c` to shut down server
* **$** `deactivate` to leave virtualenv

## Trouble? ##

### "WARNING: The tornado.speedups extension module could not be compiled." ###

* **$** `sudo apt-get install build-essential python-dev`
* **$** `sudo yum install gcc python-devel`
* **$** `pip install -I --ignore-installed -r pipfile`

## Inspiration ##

Some links that got me started:

* http://stackoverflow.com/questions/13163990/why-use-tornado-and-flask-together
* https://github.com/regadas/flask-tornado-websocket

## License ##

Copyright (c) 2014, Michael V. DePalatis
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

