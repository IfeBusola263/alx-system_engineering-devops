#Configuration Management
===
<h5>This is a project on configuration management.<h5>
* 0-create_a_file.pp :
```
This manifest creates a file in /tmp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet
```
<br>
* 1-install_a_package.pp:
```
Using Puppet, this manifest installs flask from pip3.

Requirements:

Install flask
Version must be 2.1.0
```
<br>
* 2-execute_a_command.pp:
```
Using Puppet, this manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill
```