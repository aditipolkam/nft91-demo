from brownie import NFT91
from scripts.help_script import get_account
from scripts.ipfs_upload import upload_to_ipfs
from scripts.fund_script import token_listing_fee


def create_token():
    tokenName = "demo token"  # input("Enter the token name: ")
    fileLocation = "./img/wday.jpg"  # (input("Enter the file location: "))
    listingPrice = 1  # int(input("Enter the listing price: "))
    tokenURI = upload_to_ipfs(fileLocation)

    account = get_account()

    nft91 = NFT91[-1]
    token_listing_fee()

    # nft91.createToken(tokenName, tokenURI, listingPrice, {"from": account})


def main():
    create_token()
