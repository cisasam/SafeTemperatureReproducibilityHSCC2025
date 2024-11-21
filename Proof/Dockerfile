# Use the official Wolfram Engine base image
FROM wolframresearch/wolframengine:14.1

USER root

# # Update packages:
RUN apt-get update

# # Install dependencies
RUN apt-get install -y wget openjdk-11-jdk

# Set the home directory as the working directory
WORKDIR /root

# Download the latest jar from keymaere
RUN wget https://github.com/LS-Lab/KeYmaeraX-release/releases/download/5.1.1/keymaerax.jar

# Copy the proof file to the home directory
COPY proof.kyx /root/proof.kyx

CMD [ "bash" ]