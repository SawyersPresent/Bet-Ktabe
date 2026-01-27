

## Server Setup Script

```sh
#!/bin/bash

# ============================================================================
# Apache Server Setup & Security Hardening Script
# ----------------------------------------------------------------------------
# Author: Sawyer 
# Organization: ARTOC
# Created: 03/13/2025
# Last Updated: 03/13/2025
#
# Description:
# This script automates the installation and configuration of an Apache web 
# server on an Ubuntu system. It includes security enhancements, SSL setup, 
# and configurations to hide server identity for improved security.
#
# Features:
# - Updates system package lists
# - Installs and configures Apache2
# - Sets up SSL using Certbot
# - Enhances security with mod_security2
# - Hides Apache version and identity
# - Enables necessary modules for proxying and security
#
# Usage:
# Run this script with root or sudo privileges.
#
# Example:
#   sudo bash server-setup.sh
#
# License:
# This script is provided "as is" without warranty of any kind.
# Feel free to use, modify, and distribute with proper credit.
# ============================================================================

set -e  # Exit immediately if a command exits with a non-zero status

# Wait for the cloud-init process to complete (for cloud instances)
echo "Waiting for instance boot process to finish..."
until [[ -f /var/lib/cloud/instance/boot-finished ]]; do
    sleep 1
done
echo "Instance is ready."

# Update package lists
echo "Updating system packages..."
sudo apt update -y

# Install Apache
echo "Installing Apache web server..."
sudo apt install apache2 -y
sudo systemctl enable apache2

# Install Certbot for SSL certificate management
echo "Installing Certbot for SSL..."
sudo apt install certbot python3-certbot-apache -y

# Install OpenJDK 17
echo "Installing OpenJDK 17..."
sudo apt install openjdk-17-jdk -y

# Install and enable ModSecurity for Apache
echo "Installing ModSecurity for enhanced security..."
sudo apt install libapache2-mod-security2 -y
sudo a2enmod security2

# Disable default Apache site configuration
echo "Disabling default Apache site..."
sudo a2dissite 000-default.conf

# Enable essential Apache modules
echo "Enabling necessary Apache modules..."
sudo a2enmod proxy proxy_ajp proxy_http rewrite deflate headers \
    proxy_balancer proxy_connect proxy_html

# Disable directory listing by forcefully disabling autoindex
echo "Disabling directory listing..."
sudo a2dismod autoindex -f

# Secure Apache configuration
SECURITY_CONF="/etc/apache2/conf-available/security.conf"

echo "Applying security configurations..."
sudo sed -i "s/ServerSignature On/ServerSignature Off/g" "$SECURITY_CONF"
sudo sed -i "s/ServerTokens OS/ServerTokens Full/g" "$SECURITY_CONF"

# Obfuscate the server signature to mislead attackers
echo "Obfuscating Apache server identity..."
echo "SecServerSignature Microsoft-IIS/10.0" | sudo tee -a "$SECURITY_CONF" > /dev/null

# Restart Apache to apply changes
echo "Restarting Apache to apply changes..."
sudo systemctl restart apache2

echo "Apache server setup and security hardening completed successfully!"
```






## Domain Setup Script


```sh
#!/bin/bash

# ============================================================================
# Apache Virtual Host & SSL Setup Script
# ----------------------------------------------------------------------------
# Author: Sawyer
#
# Description:
# This script automates the setup of a virtual host for a given domain on an 
# Apache web server. It also configures SSL using Certbot and ensures proper 
# permissions for the website directory.
#
# Features:
# - Creates necessary directories for the domain
# - Sets up an Apache Virtual Host configuration
# - Enables the site and restarts Apache
# - Checks if the domain resolves via DNS
# - Acquires and installs an SSL certificate using Certbot
#
# Usage:
# Run this script with root or sudo privileges, passing the domain name
# as an argument.
#
# Example:
#   sudo bash domain-setup.sh example.com
#
# License:
# This script is provided "as is" without warranty of any kind.
# Feel free to use, modify, and distribute with proper credit.
# ============================================================================

set -e  # Exit on errors

# Wait for the cloud-init process to complete (for cloud instances)
echo "Waiting for instance boot process to finish..."
until [[ -f /var/lib/cloud/instance/boot-finished ]]; do
    sleep 1
done
echo "Instance is ready."

# Validate input
if [[ -z "$1" ]]; then
    echo "Error: No domain provided. Usage: sudo bash $0 yourdomain.com"
    exit 1
fi

# Set important variables
MYDOMAIN=$1
VHOST_CONF="/etc/apache2/sites-available/${MYDOMAIN}.conf"
WEB_ROOT="/var/www/${MYDOMAIN}"
LOG_DIR="${WEB_ROOT}/logs"

echo "Configuring domain: $MYDOMAIN"

# Create necessary directories
echo "Creating website directory structure..."
sudo mkdir -p "$WEB_ROOT"
sudo mkdir -p "$LOG_DIR"
sudo chown -R root:root "$WEB_ROOT"
sudo chmod -R 755 "$WEB_ROOT"

# Setup Virtual Host file
echo "Creating Apache Virtual Host configuration..."
sudo tee "$VHOST_CONF" > /dev/null <<EOL
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName $MYDOMAIN
    ServerAlias www.$MYDOMAIN
    DocumentRoot $WEB_ROOT
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOL

# Enable the site and restart Apache
echo "Enabling the virtual host and restarting Apache..."
sudo a2ensite "${MYDOMAIN}.conf"
sudo systemctl restart apache2

# Wait for the domain to resolve
echo "Checking if domain resolves..."
while ! nc -z "$MYDOMAIN" 80; do
    echo "Waiting 2.5 minutes for DNS resolution..."
    sleep 150
done

echo "Domain appears to resolve. Proceeding with SSL setup..."

# Obtain an SSL certificate via Certbot
CERTBOT_CMD="sudo certbot --apache --email admin@$MYDOMAIN --agree-tos --no-eff-email -d $MYDOMAIN --redirect --hsts --uir"
echo "Running Certbot command: $CERTBOT_CMD"
$CERTBOT_CMD || {
    echo "Certbot failed! You may need to manually retry with:"
    echo "  $CERTBOT_CMD"
    exit 1
}

echo "SSL certificate setup complete."

# Restart Apache to apply changes
echo "Final Apache restart..."
sudo systemctl restart apache2

echo "Domain setup completed successfully for: $MYDOMAIN"
exit 0
```
