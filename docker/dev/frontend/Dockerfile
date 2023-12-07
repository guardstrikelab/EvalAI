FROM node:16.20.2 as build-stage
RUN npm install -g @vue/cli

WORKDIR /code/frontend
ADD frontend /code/

# Install Prerequisites
RUN npm cache clean -f
RUN npm install
RUN npm run build
#CMD [ "npm", "run", "dev" ]

FROM nginx:1.13-alpine as nginx-stage
COPY docker/dev/frontend/single.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /code/dist /usr/share/nginx/html
EXPOSE 8888
CMD ["nginx", "-g", "daemon off;"]