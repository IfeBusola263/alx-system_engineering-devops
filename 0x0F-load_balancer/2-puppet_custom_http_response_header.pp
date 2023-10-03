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

file { '/etc/nginx/sites-available/default':
  ensure  =>  present,
}
-> file_line { 'including custom header':
  path  =>  '/etc/nginx/sites-available/default',
  line  =>  "# as directory, then fall back to displaying a 404.\n\t\tadd_header X-Served-By \"${HOSTNAME}\";",
  match => '^# as directory, then fall back to displaying a 404.$',
}

file {'/etc/nginx/sites-enabled/default':
  ensure =>  present,
  link   =>  '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure  =>  running,
}
