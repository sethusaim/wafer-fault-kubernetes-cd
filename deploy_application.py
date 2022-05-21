from os import environ
from subprocess import run
from urllib.request import urlopen

from yaml import safe_load


def get_application_image():
    try:
        x = urlopen(
            "https://raw.githubusercontent.com/sethusaim/Wafer-Fault-Kubernetes-CD/main/components/wafer_application.yaml"
        )

        content = safe_load(x)

        image = content["implementation"]["container"]["image"]

        return image

    except Exception as e:
        raise e


def run_docker_image(image):
    try:
        run("aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 347460842118.dkr.ecr.us-east-1.amazonaws.com")
        
        if environ["DOCKERTAG"] == "1":
            run(f"docker run --name wafer_app {image} -p 8080:8080")

        else:
            run("docker stop wafer_app")

            run("docker rm wafer_app")

            run(f"docker run --name wafer_app {image} -d -p 8080:8080")

    except Exception as e:
        raise e


if __name__ == "__main__":
    image = get_application_image()

    run_docker_image(image)
