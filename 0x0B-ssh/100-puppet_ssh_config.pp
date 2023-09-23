# This manifest configures the ssh configuration file

file { '/etc/ssh/ssh_config':
  ensure  =>  present,
  content => '\nPasswordAuthentication no\nIdentityFile ~/.ssh/school',
  }
