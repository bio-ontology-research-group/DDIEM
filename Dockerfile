FROM node:12

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY website/package.json .
COPY website/package-lock.json .

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY website/. .
COPY data/. data/.

EXPOSE 80   
EXPOSE 443
EXPOSE 8891 
CMD npm run build:ssr && PORT=80 HTTPS_PORT=443 npm run serve:ssr