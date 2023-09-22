# This manifest kills a process called 'killmenow'

exec {'killmenow':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  }
