FROM node:10

WORKDIR /usr/src/app

# Install packages
# (Currently not needed)
#RUN apt-get install -y \
#        package \
# && rm -rf /var/lib/apt/lists/*


# Install npm packages
COPY package*.json ./

RUN npm ci
RUN npm install -g serve

# Copy the source and build
COPY . ./

RUN CI=true npm run build


# Run
EXPOSE 8080

ENTRYPOINT serve -n -s dist/ -p 8080
