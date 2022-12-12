from brownie import AdvancedCollectible, config, network
import pytest, time
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_get_advanced_collectible_integartion():

    if network.show_active in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(240)
    assert advanced_collectible.tokenCounter() >= 1
