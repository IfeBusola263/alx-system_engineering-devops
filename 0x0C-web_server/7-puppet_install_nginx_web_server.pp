# This manifest installs a new Nginx web server in a server
include stdlib

package { 'nginx':
  ensure   => installed,
  provider => 'apt-get',
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

exec { '/etc/nginx/sites-enabled/default':
  ensure  =>   present,
  command =>   'sudo rm /etc/nginx/sites-enabled/default'
  }

  file_line { 'listen \[::\]:80 default_server;':
    ensure             => present,
    path               => '/etc/nginx/sites-available/default',
    line               => 'listen \[::\]:80 default_server;',
    match              => 'listen \[::\]:80 default_server;\n\tlocation \/redirect_me {
\treturn 301 https:\/\/www.youtube.com\/watch\?v\=QH2-TGUlwu4;\n\t}',
    append_on_on_match => false,
  }

  exec { '/etc/nginx/sites-available/default':
    ensure  =>  present,
    command =>  'sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/'
  }

  exec { 'nginx':
    command  => 'sudo service nginx start',
  }

