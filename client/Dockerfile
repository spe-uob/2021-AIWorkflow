FROM node:16

# Create app directory
WORKDIR /src

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /src

ENV NODE_ENV=production
RUN npm install --production

# Bundle app source
COPY . /src

EXPOSE 3000
CMD [ "node", "index.js" ]