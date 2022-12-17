FROM nginx:alpine

WORKDIR /etc/nginx/conf.d
COPY Server/webgl.conf default.conf

WORKDIR /webgl
COPY SNA_front/WebGL/WebGL/ .

