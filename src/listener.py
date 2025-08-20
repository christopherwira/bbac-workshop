from utils import web3_utils
import json, time
from web3.exceptions import ContractLogicError


contract_name = 'BlockchainBasedAccessControl'
contract_address = ''

w3 = web3_utils.create_http_provider('http://hardhat:8545')
contract = web3_utils.create_contract_instance(contract_name,contract_address, w3)
event_filter = contract.events.AccessGranted.create_filter(from_block='latest')
while True:
    for event in event_filter.get_new_entries():
            print("Access Granted Event Detected!")
            print(f"  Device Address: {event['args']['device']}")
            print(f"  Block Number: {event['blockNumber']}")
    time.sleep(0.2)