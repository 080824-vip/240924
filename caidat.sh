#!/bin/bash

# Đọc domain từ file domain.txt
DOMAIN=$(cat /home/user/domain.txt)

# Sử dụng API của 1secmail với domain tùy chỉnh
RESPONSE=$(curl -s "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1&domain=$DOMAIN")
if [[ $RESPONSE == *"@"* ]]; then
    EMAIL=$(echo $RESPONSE | jq -r '.[0]')
echo "Generated email: $EMAIL"
else
    echo "Domain $DOMAIN is not accepted by 1secmail API. Using default domain."
fi
