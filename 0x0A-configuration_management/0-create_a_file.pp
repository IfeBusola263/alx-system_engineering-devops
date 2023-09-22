# This manifest creates a new file with contents in the /tmp folder

$str='I love Puppet'
$mod='0744'
$own='www-data'
$grp='www-data'

file { '/tmp/school':
  ensure  => present,
  content => $str,
  mode    => $mod,
  owner   => $own,
  group   => $grp,
  }
