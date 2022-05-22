import yaml
from os import environ

new_tag = environ["DOCKERTAG"]

file_name = "components" + "/" + environ["COMP_FILE"]


def read_yaml():
    try:
        with open(file_name, "r") as f:
            content = yaml.safe_load(f)

        return content

    except Exception as e:
        raise e


def update_yaml():
    try:
        config = read_yaml()

        old_image = config["spec"]["steps"][0]["image"]

        tagless_image = old_image.split(":")[0]

        new_image = tagless_image + ":" + str(new_tag)

        config["spec"]["steps"][0]["image"] = new_image

        with open(file_name, "w") as fp:
            yaml.safe_dump(config, fp, sort_keys=False)

    except Exception as e:
        raise e


if __name__ == "__main__":
    update_yaml()
