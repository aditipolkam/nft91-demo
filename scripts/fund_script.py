from web3 import Web3
from brownie import NFT91

from scripts.help_script import get_account


def token_listing_fee():
    nft91 = NFT91[-1]
    account = get_account()
    fee_tx = nft91.tokenListingFee(
        {"from": account, "value": Web3.toWei(0.0025, "ether")}
    )
    print("Listing Fee transaction complete")


def withdraw():
    nft91 = NFT91[-1]
    account = get_account(owner=True)
    print("Withdrawing balance.....")
    nft91.withdraw({"from": account})
