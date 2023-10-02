# Load Balancer
This is a project on load balancing
* 0-custom_http_response_header:
```
Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02):
	  The name of the custom HTTP header must be X-Served-By.
	  The value of the custom HTTP header must be the hostname of the server Nginx is running on.
```

* 1-install_load_balancer:
```
Installs and configures HAproxy on your lb-01 server.
Requirements:

	Configure HAproxy so that it send traffic to web-01 and web-02
	Distribute requests using a roundrobin algorithm
	Make sure that HAproxy can be managed via an init script
```

* 2-puppet_custom_http_response_header.pp
```
Automates the task of creating a custom HTTP header response, but with Puppet.
	  The name of the custom HTTP header must be X-Served-By
	  The value of the custom HTTP header must be the hostname of the server Nginx is running on
```