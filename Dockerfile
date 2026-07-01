FROM python
WORKDIR /smartlife
COPY . .
EXPOSE 5002
RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "src/main.py"]