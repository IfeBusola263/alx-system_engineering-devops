# This manifest configures a new ubuntu server
include stdlib

package {'nginx':
  ensure  =>  installed,
  }

file {'/var/www/html/index.html':
  ensure  =>  present,
  content =>  'Hello World!',
  }

file { '/etc/nginx/sites-enabled/def*':
  ensure  =>  absent,
  }

file_line { 'including custom header':
  path  =>  '/etc/nginx/sites-available/default',
  line  =>  "\t\t# as directory, then fall back to displaying a 404.\
\n\t\tadd_header X-Served-By \"${::hostname}\";",
  match =>  '# as directory, then fall back to displaying a 404.',
  }

file {'/etc/nginx/sites-enabled/default':
  ensure =>  link,
  target =>  '/etc/nginx/sites-available/default',
  }

service { 'nginx':
  ensure  =>  running,
  }
