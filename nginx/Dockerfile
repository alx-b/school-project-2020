FROM nginxinc/nginx-unprivileged:latest

RUN rm -rf /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/

RUN mkdir -p /etc/nginx/certs

COPY ./certs/* /etc/nginx/certs/

USER root

RUN mkdir -p /vol/static \
 && chmod 755 /vol/static \
 && chown -R nginx:nginx /etc/nginx/certs \
 && chmod -R 755 /etc/nginx/certs

USER nginx
