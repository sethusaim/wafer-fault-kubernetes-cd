import ruamel.yaml
from os import environ

new_tag = environ["DOCKERTAG"]

file_name = environ["COMP_FILE"]


def update_yaml():
    try:
        config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))

        old_image = config["implementation"]["container"]["image"]
        
        tagless_image = old_image.split(":")[0]
        
        new_image = tagless_image + ":" + str(new_tag)

        config["implementation"]["container"]["image"] = new_image

        yaml = ruamel.yaml.YAML()

        yaml.indent(mapping=ind, sequence=ind, offset=bsi)

        with open(file_name, "w") as fp:
            yaml.dump(config, fp)

    except Exception as e:
        raise e


if __name__ == "__main__":
    update_yaml()
