FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements/* /code/
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r dev.txt
RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
RUN sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get --no-install-recommends install -q -y default-jre default-jdk \
    git cmake libeigen3-dev libboost-python-dev libopencv-dev python3-opencv \
    libgmp-dev libcgal-qt5-dev swig && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -U cffi service_identity cython==0.29 numpy==1.14.5
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r worker.txt

ADD . /code

CMD ["./docker/wait-for-it.sh", "django:8000", "--", "python", "-m", "scripts.workers.submission_worker"]