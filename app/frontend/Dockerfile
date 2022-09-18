#Import base node image
FROM node:16.13-alpine

# The source directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package.json .
COPY package-lock.json .

# Install the packages
RUN npm install

# Copy the rest of the source code
COPY . .

# Gets Executed when we run the image in the container (entrypoint)
CMD ["npm","run","start"]