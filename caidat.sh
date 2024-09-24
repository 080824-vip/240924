#!/bin/bash

# Đọc domain từ file domain.txt
DOMAIN=$(cat domain.txt)

# Cài đặt tmpmail
git clone https://github.com/sdushantha/tmpmail
cd tmpmail
sudo make install

# Sử dụng tmpmail với domain tùy chỉnh
tmpmail --domain $DOMAIN
