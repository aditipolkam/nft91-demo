from brownie import NFT91
from scripts.help_script import get_account
from scripts.fund_script import token_listing_fee, withdraw


def main():
    account = get_account(owner=True)
    nft91 = NFT91.deploy({"from": account})
    print(f"Contract deployed at address: {nft91.address}")
    token_listing_fee()
    tx1 = nft91.createToken({"from": get_account()})
    tx1.wait(1)
    print("Token 0 created")
