# This manifest installs a new Nginx web server in a server

$str1='listen \[::\]:80 default_server;'
$str2='listen \[::\]:80 default_server;\n\tlocation \/redirect_me {\n\treturn 301 https:\/\/www.youtube.com\/watch\?v\=QH2-TGUlwu4;\n\t}'
$str3= "sudo sed -i 's|${str1#\//\\/}|${str2#\//\\/}|' /etc/nginx/sites-available/default"

package { 'nginx':
  ensure   => installed,
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-enabled/':
  ensure    => absent,
}

exec { '/etc/nginx/sites-available/default':
  path    => '/bin',
  command => $str3,
}

file { '/etc/nginx/sites-enabled/default':
  ensure =>  link,
  target =>  '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure  => 'running',
}
