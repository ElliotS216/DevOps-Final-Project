# Use a C++ compiler image
FROM gcc:15.2

# Set working directory inside container
WORKDIR /app

# Copy your C++ file into the container
COPY . .

# Compile the program
RUN g++ -o app app.cpp

# Run the program
CMD ["./app"]