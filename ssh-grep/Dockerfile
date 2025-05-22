FROM python:3.10-slim

# Installeer OpenSSH-server en grep
RUN apt-get update \
 && apt-get install -y --no-install-recommends openssh-server grep \
 && rm -rf /var/lib/apt/lists/*

# Maak de SSH-directory aan en configureer password-login (voor PoC)
RUN mkdir /var/run/sshd \
 && echo 'root:airflow' | chpasswd \
 && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Zet werkdir
WORKDIR /opt/ssh-grep

COPY hello_grep.py input.txt /opt/ssh-grep/

RUN chmod +x /opt/ssh-grep/hello_grep.py

EXPOSE 22

# Start zowel SSH-daemon als slaaploop zodat de container blijft draaien
CMD ["/bin/sh", "-c", "service ssh start && tail -f /dev/null"]