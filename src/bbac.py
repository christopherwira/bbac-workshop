from utils import web3_utils
import json
from web3.exceptions import ContractLogicError

w3 = web3_utils.create_http_provider('http://hardhat:8545')
prize_pool_eth = w3.to_wei(30, 'ether')
(contract, tx_receipt, _) = web3_utils.compile_and_deploy(w3, 'BlockchainBasedAccessControl')
# (proof, inputs) = zokrates_utils.parse_proof('zksudoku')
# tx_hash = contract.functions.submitSolution(proof, inputs).transact({"from":w3.eth.accounts[0]})
# submit_tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# print(web3_utils.get_account_balance(w3, 0))