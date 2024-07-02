FROM  ubuntu:16.04
ENV NAME Jaspreet
ENV PASS Jas@123
RUN mkdir -p /var/run/sshd
RUN apt-get update
RUN apt-get install -y python tree
COPY test.sh /tmp/
ENTRYPOINT ["/tmp/test.sh"]
