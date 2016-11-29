#Dumb Function Specific Manager.
## Docker Build command
sudo docker build -t sonfsmfunctiondumb1 -f son-fsms/dumb/Dockerfile .
## Docker Run command
sudo docker run -it --rm --link broker:broker  --name sonfsmfunctiondumb1  sonfsmfunctiondumb1
