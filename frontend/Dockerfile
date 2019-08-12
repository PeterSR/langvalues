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
RUN npm install -g local-web-server

# Copy the source and build
COPY . ./

RUN CI=true npm run build


# Run
WORKDIR dist

ENV API_HOST="http://localhost"

EXPOSE 8080

ENTRYPOINT ws --spa index.html -p 8080 --rewrite "/api/(.*) -> $API_HOST/api/\$1" --static.extensions
