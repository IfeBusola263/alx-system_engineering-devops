# This manifest fixes the limit of request nginx can attend to

package { 'nginx':
  ensure => 'installed',
}

exec { 'edit config file':
  command =>  'sed -i "s/15/4096/g" /etc/default/nginx',
  path    =>  '/usr/local/bin/:/bin/',
}

service { 'nginx':
  ensure  =>  'running',
  enable  =>  true,
  require =>  Package['nginx'],
}
