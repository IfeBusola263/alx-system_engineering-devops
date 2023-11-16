# Web stack debugging
I have an ubuntu 14.04, with a web server (ngixx) running on it.
I use the ApacheBench commandline tool to test the number of requests, it
can handle at a go, the `/var/log/nginx/error.log` log a `open() "/usr/share/nginx/html/index.html" failed (24: Too many open files)`
0-the_sky_is_the_limit_not.pp sorts the file descriptor issue in the nginx
default configuration file.

1-user_limit.pp configures the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

