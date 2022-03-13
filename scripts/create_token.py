from brownie import NFT91
from scripts.help_script import get_account
from scripts.ipfs_upload import upload_to_ipfs
from scripts.fund_script import token_listing_fee
from scripts.create_metadata import create_metadata
from scripts.opensea_deploy import deploy_opensea


def create_token():
    nft91 = NFT91[-1]
    tokenId = nft91.tokenCounter()
    print(tokenId)
    account = get_account()
    token_listing_fee()

    nft91.createToken({"from": account})

    tokenName = input("Enter the token name: ").replace(
        " ", ""
    )  # input("Enter the token name: ")
    desc = input(
        "Enter the token description: "
    )  # input("Enter the token description: ")
    fileLocation = input(
        "Enter the file location: "
    )  # (input("Enter the file location: ")) img/pug.png
    listingPrice = 1  # int(input("Enter the listing price: "))

    metadata_file = create_metadata(
        tokenId, tokenName, desc, fileLocation, listingPrice, get_account()
    )

    tokenURI = upload_to_ipfs(metadata_file)
    deploy_opensea(tokenId, tokenURI)


def main():
    create_token()
