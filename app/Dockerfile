FROM alpine:3.10

#Add bash to our image
RUN apk add --no-cache bash
RUN apk add --update nodejs nodejs-npm
RUN apk add --no-cache rsync

WORKDIR /snow-vue

# copy project files
COPY . .

#Install yarm
RUN npm i -g yarn

#Use yarn to install the project
RUN yarn
ENTRYPOINT yarn start 

