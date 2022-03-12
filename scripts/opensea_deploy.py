from lib2to3.pgen2 import token
from brownie import NFT91, network
from scripts.help_script import get_account

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_opensea(tokenId, tokenURI):
    nft91 = NFT91[-1]
    account = get_account(owner=True)
    tx = nft91.setTokenURI(tokenId, tokenURI, {"from": account})
    tx.wait(1)
    print(f"View your NFT at {OPENSEA_URL.format(nft91.address),tokenId}")
