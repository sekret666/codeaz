FROM sandy1709/catuserbot:latest

#clonning repo 
RUN git clone https://github.com/texnocom/codeaz.git /root/codeaz
#working directory 
WORKDIR /root/codeaz

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/codeaz/bin:$PATH"

CMD ["python3", "main.py"]
