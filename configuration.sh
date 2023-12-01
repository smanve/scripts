#!/bin/bash
#
# Configuration file for git for credentials, aliases, username and email.

# Set the username and email for git
echo ""
echo "Configuring git"
echo "Please enter your git username: "
read USERNAME
PRIVATE_EMAIL="$USERNAME@users.noreply.github.com"
read -s -p "Please enter your git email [Press enter to accept the private email $PRIVATE_EMAIL]: " EMAIL

# Using parameter expansion to provide default values
EMAIL="${EMAIL:-${PRIVATE_EMAIL}}"

