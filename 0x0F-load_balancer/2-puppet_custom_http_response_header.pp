# This manifest configures a new ubuntu server

package {'nginx':
  ensure  =>  installed,
}

file {'/var/www/html/index.html':
  ensure  =>  present,
  content =>  'Hello World!',
}

file { '/etc/nginx/sites-enabled/':
  ensure  =>  absent,
}
