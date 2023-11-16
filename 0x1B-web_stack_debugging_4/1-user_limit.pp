# This manifest reconfigures the limit of a user to increase the number of files
# that can be opened by the user

exec { 'Hard limit configuration':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 500/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'Soft limit configuration':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 400/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
