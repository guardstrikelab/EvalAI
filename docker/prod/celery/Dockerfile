ARG AWS_ACCOUNT_ID
ARG COMMIT_ID
ARG TRAVIS_BRANCH
ARG AWS_DEFAULT_REGION

FROM ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com.cn/arena/evalai-${TRAVIS_BRANCH}-backend:${COMMIT_ID}

CMD ["sh", "/code/docker/prod/celery/container-start.sh"]
