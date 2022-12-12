from brownie import AdvancedCollectible, network
from metadata.sample_metadata import metadata_template
from scripts.helpful_scripts import get_breed
from pathlib import Path
import requests


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"you have created {number_of_advanced_collectibles} collectiles")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print("this file alraedy exists, delete it to overwrite")
        else:
            print(f"creating metadata file {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            upload_to_ipfs(image_path)


def upload_to_ipfs(file_path):
    with Path(file_path).open("rb") as fp:
        image_binary = fp.read()
        # upload stuff
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        _files = {"file": image_binary}
        response = requests.post(ipfs_url + endpoint, files=_files)
        ipfs_hash = response.json()["Hash"]
        # "./img/PUG.png" -> "PUG.png"
        filename = file_path.split("/")[-1]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
