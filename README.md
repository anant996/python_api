# Simple HTTP Server with Custom Endpoints

This is a simple HTTP server written in Python that serves custom endpoints and provides functionality for generating random passwords.
# Requirements

    Python 3.x
    passPkg (custom password generation package)

# Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/your-repo.git
cd your-repo

Install the required package (passPkg):

bash

    pip install passPkg

# Usage

    Start the server:

    bash

    python server.py

    The server will be running on http://localhost:8080.

# Endpoints

    Root URL (/):

    Returns a "Welcome to the server!" message.

    Ping Endpoint (/ping):

    Returns "Ponggg".

    Password Generation Endpoint (/pwd):

    Generates a random password using the generate_pass function from the passPkg package and returns it as plain text.

    Note: Ensure the passPkg package is installed before running this endpoint.

# Contributing

Contributions are welcome! If you find any bugs or want to add new features, please feel free to submit issues or pull requests.
License

This project is licensed under the MIT License.

Add or modify any additional sections as necessary to provide more details about your project. Include information such as project features, usage examples, and any other relevant details to help users understand and utilize your HTTP server. Replace the placeholders like your-username, 
