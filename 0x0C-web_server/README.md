# WEB SERVER

<h5>This is a project on Web Servers</h5>
 * 0-transfer_file:  Bash script that transfers a file from our client to a server
 
 ```
 Requirements:
 1. Accepts 4 parameters
    *  The path to the file to be transferred
    *  The IP of the server we want to transfer the file to
    *  The username scp connects with
    *  The path to the SSH private key that scp uses
 2. Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
 3. scp must transfer the file to the user home directory ~/
 4. Strict host key checking must be disabled when using scp
 ```

 * 1-install_nginx_web_server: Bash script that configures a new Ubuntu machine to respect below requirements
 ```
 Requirements:
 Install nginx on your web-01
 server
 Nginx should be listening on port 80
 When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
 ```

 * 2-setup_a_domain_name: File with domain name
 * 3-redirection: Configures Nginx server so that '/redirect_me' is redirecting to another page.
 ```
 Requirements:
	* The redirection must be a "301 Moved Permanently"
	* With 1-install_nginx_web_server, 3-redirection configures a brand new Ubuntu machine.
 ```
 * 4-not_found_page_404: Configures Nginx server to have a custom 404 page that contains the string 'Ceci n'est pas une page'.

 * 7-puppet_install_nginx_web_server.pp: install and configure an Nginx server using Puppet instead of Bash.
 ```
 Requirements:
 * Nginx should be listening on port 80
 * When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
 * The redirection must be a "301 Moved Permanently"
 * Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
 ```