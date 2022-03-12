import json
from metadata.sample import metadata_template
from brownie import NFT91, network

from scripts.ipfs_upload import upload_to_ipfs


def create_metadata(tokenId, name, description, image, price, owner):
    nft91 = NFT91[-1]
    img_uri = upload_to_ipfs(image)
    metadata_filename = f"metadata/{network.show_active()}/{tokenId}-{name}.json"

    token_metadata = metadata_template
    token_metadata["name"] = name
    token_metadata["description"] = description
    token_metadata["image"] = img_uri
    token_metadata["price"] = price
    token_metadata["owner"] = str(owner)

    with open(metadata_filename, "w") as f:
        json.dump(token_metadata, f)

    return metadata_filename
