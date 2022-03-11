from brownie import NFT91
from pathlib import Path
from scripts.ipfs_upload import upload_to_ipfs


def main():
    tokenName = "demo token"  # input("Enter the token name: ")
    fileLocation = "./img/wday.jpg"  # (input("Enter the file location: "))
    listingPrice = 0.025  # int(input("Enter the listing price: "))
    tokenURI = upload_to_ipfs(fileLocation)
    print(tokenURI)
