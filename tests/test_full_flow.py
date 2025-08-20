# tests/test_full_flow.py

import unittest
import json
from web3.exceptions import ContractLogicError

# Use absolute imports, as your environment is configured for it
from utils import web3_utils

class TestFullBBACFlow(unittest.TestCase):

    # Class-level variables to share state between tests
    w3 = None
    contract = None
    proof = None
    inputs = None

    @classmethod
    def setUpClass(cls):
        """Set up the environment once for all tests."""
        print("\n--- Setting up Web3 Connection ---")
        cls.w3 = web3_utils.create_http_provider('http://hardhat:8545')
        cls.assertTrue(cls.w3.is_connected(), "Failed to connect to Hardhat node")
        print("Web3 connection successful.")

    def test_deploy_contract(self):
        """Tests contract compilation and deployment."""
        
        (contract, tx_receipt, _) = web3_utils.compile_and_deploy(
            self.w3, 
            'BlockchainBasedAccessControl'
        )
        
        self.assertIsNotNone(contract.address, "Contract deployment failed.")
        TestFullBBACFlow.contract = contract
        print(f"Contract deployed successfully at {contract.address}.")

    def test_grant_access_to_contract(self):
        """Tests submitting a valid proof to the smart contract."""
        self.assertIsNotNone(self.contract, "Contract not deployed, skipping test.")
        
        tx_hash = self.contract.functions.grantAccess(self.w3.eth.accounts[1]).transact({"from": self.w3.eth.accounts[0]})
        submit_tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        self.assertEqual(submit_tx_receipt.status, 1, "Transaction failed.")

if __name__ == '__main__':
    unittest.main()