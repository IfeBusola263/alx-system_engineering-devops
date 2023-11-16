# This manifest reconfigures the limit of a user to increase the number of files
# that can be opened by the user

file_line { 'Hard limit configuration':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 500',
  match => '^holberton hard nofile 5$',
}

file_line { 'Soft limit configuration':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 400',
  match => '^holberton soft nofile 4$',
}
