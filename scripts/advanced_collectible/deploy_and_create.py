from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract, fund_link
from brownie import AdvancedCollectible, config, network


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link"),
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )

    fund_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)

    print("New token has been created")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()
