FROM alpine:3.5

#Add bash to our image
RUN apk add --no-cache bash
RUN apk add --no-cache nodejs
RUN apk add --no-cache rsync
WORKDIR /snow-vue

# copy project files
COPY . .

#Install yarm
RUN npm i -g yarn

#Use yarn to install the project
RUN yarn
RUN yarn start 

