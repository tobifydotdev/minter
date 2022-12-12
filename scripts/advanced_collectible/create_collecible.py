from brownie import Advancedcollectible, config, network
from scripts.helpful_scripts import get_account, get_contract, fund_link
from web3 import Web3


def main():
    account = get_account()
    advanced_collectible = Advancedcollectible[-1]
    fund_link(advanced_collectible.address, Web3.toWei(0.1, "ether"))
    creation = advanced_collectible.createCollectible({"from": account})
    creation.wait(1)
    print("Collectible Created")
