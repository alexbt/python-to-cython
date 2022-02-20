# build
- `docker-compose build` or
- `docker build -t python2cython .`

# run
- `docker-compose up` or
- `docker run -p 8090:8090 -it python2cython`

then call `curl 0.0.0.0:8090`


# output
```
{
  "filenames_programmatically": {
    "app": "app.py", 
    "my_flask": "/abt/my_flask.cpython-37m-x86_64-linux-gnu.so", 
    "other": "/abt/other.cpython-37m-x86_64-linux-gnu.so"
  }, 
  "files_on_disk": {
    "./": [
      ".dockerenv", 
      "py_to_pyx.sh", 
      "Dockerfile", 
      "docker-compose.yml", 
      ".gitignore", 
      "setup.py", 
      "app.py", 
      "requirements.txt", 
      "README.md"
    ], 
    "./abt": [
      "__init__.c", 
      "my_flask.c", 
      "other.cpython-37m-x86_64-linux-gnu.so", 
      "__init__.cpython-37m-x86_64-linux-gnu.so", 
      "my_flask.cpython-37m-x86_64-linux-gnu.so", 
      "other.c", 
      "my_flask.pyx", 
      "other.pyx", 
      "__init__.pyx"
    ]
  }
}
```
