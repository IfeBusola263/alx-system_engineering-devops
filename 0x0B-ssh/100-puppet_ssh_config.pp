# This manifest configures the ssh configuration file

file { '/etc/ssh/*conf':
  ensure  =>  present,
  content => '\nPasswordAuthentication no\nIdentityFile ~/.ssh/school',
  }
