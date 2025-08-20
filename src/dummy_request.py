from utils import web3_utils
import json, time
from web3.exceptions import ContractLogicError


contract_name = 'BlockchainBasedAccessControl'
contract_address = ''
account_index = 1

w3 = web3_utils.create_http_provider('http://hardhat:8545')
contract = web3_utils.create_contract_instance(contract_name,contract_address, w3)
tx_hash = contract.functions.grantAccess(w3.eth.accounts[account_index]).transact({"from":w3.eth.accounts[0]}) 
submit_tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(submit_tx_receipt)