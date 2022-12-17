FROM nginx:alpine

WORKDIR /etc/nginx/conf.d
COPY Server/webgl.conf default.conf


