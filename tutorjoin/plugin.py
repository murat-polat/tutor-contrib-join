from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "tutorjoin", "templates"
)

from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "tutorjoin", "templates"
)

config = {
    "add": {
        "SECRET_KEY": "{{ 24|random_string }}",
    },

    "defaults": {
        "HOST": "join.{{ LMS_HOST }}",
        "DOCKER_REGISTRY": "{{ DOCKER_REGISTRY }}",
        "DOCKER_IMAGE": "muratp/join"
       
    }

}

hooks = {

     "init": ["lms","join"],   
# Pull and build docker containers
    "build-image": {"join": "muratp/join"},
    "remote-image": {"join": "muratp/join"},
# Initial all services
    
}

def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorjoin", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorjoin", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
