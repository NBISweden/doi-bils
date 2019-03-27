**Running the web server container**

To build the image:
```
docker build -t <image-name> <dockerfile-path>
```

Run the web server docker container as follows, where `src-dir` is the `data` folder containing the issued issued dois json file.
```
docker run --rm -d -p 8080:8080 -v <src-dir>:/doi-bils/data <image-name>
```
