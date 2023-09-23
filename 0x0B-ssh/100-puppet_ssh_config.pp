# This manifest configures the ssh configuration file

file { '/etc/ssh/ssh_config':
  ensure  =>  present,
  content => 'PasswordAuthentication no
IdentityFile ~/.ssh/school',
}
