# This puppet manifest fixes an internal server error issue in a server
# running apache2

exec { 'sed -i "s|phpp|php|" var/www/html/wp-settings.php':
  path  => '/usr/bin',
}
