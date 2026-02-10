# Assumes cPanel access
echo "Upload /public to public_html"
echo "Create MySQL DB via cPanel"
echo "Create 50 emails via cPanel → Email Accounts"

# Database config
cat <<EOF > config.php
<?php
define('DB_NAME', 'empower_db');
define('DB_USER', 'empower_user');
define('DB_PASS', 'securepassword');
define('DB_HOST', 'localhost');
?>
EOF
