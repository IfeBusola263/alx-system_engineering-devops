# This puppet manifest fixes an internal server error issue in a server
# running apache2

exec { 'replace_string_in_php_settings':
  command =>  'sed -i "s|phpp|php|" /var/www/html/wp-settings.php',
  path    =>  '/usr/bin',
}
