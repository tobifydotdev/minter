from brownie import accounts, network, AdvancedCollectible
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
import pytest


def test_can_get_advanced_collectible():
    # arrange

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Act
    advanced_collectible, creation_tx = deploy_and_create()
    random_number = 777
    requestId = creation_tx.events["requestedCollectible"]["requestId"]
    print(requestId)
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )
    # Assert
    assert advanced_collectible.tokenCounter() >= 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
