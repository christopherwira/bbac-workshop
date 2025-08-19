// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title SmartLock
 * @author Your Name
 * @notice A simple smart contract to manage access control for IoT devices.
 * This contract simulates a smart lock where an owner can grant or revoke
 * access to specific device addresses.
 */
contract BlockchainBasedAccessControl {
    // --- State Variables ---

    // The address of the administrator who can change permissions.
    address public owner;

    // A mapping to store the access list.
    // An address (representing an IoT device) maps to a boolean (true if it has access).
    // It's 'public' so anyone can check if a specific address has access.
    mapping(address => bool) public hasAccess;

    // --- Events ---

    // Emitted when a new device is granted access.
    event AccessGranted(address indexed device);

    // Emitted when a device's access is revoked.
    event AccessRevoked(address indexed device);

    // --- Modifiers ---

    /**
     * @dev A modifier to restrict a function's execution to only the contract owner.
     * It will revert the transaction if called by any other account.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _; // This special character represents the rest of the function's code.
    }

    // --- Constructor ---

    /**
     * @dev The constructor is called only once when the contract is deployed.
     * It sets the address of the person who deploys the contract as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    // --- Owner Functions ---

    /**
     * @notice Grants access to a new IoT device address.
     * @dev Can only be called by the contract owner.
     * @param _device The address of the device to be whitelisted.
     */
    function grantAccess(address _device) public onlyOwner {
        require(_device != address(0), "Cannot grant access to the zero address");
        hasAccess[_device] = true;
        emit AccessGranted(_device);
    }

    /**
     * @notice Revokes access from an existing IoT device address.
     * @dev Can only be called by the contract owner.
     * @param _device The address of the device to be removed from the whitelist.
     */
    function revokeAccess(address _device) public onlyOwner {
        require(_device != address(0), "Cannot revoke access from the zero address");
        hasAccess[_device] = false;
        emit AccessRevoked(_device);
    }

    // --- Public Access Function ---

    /**
     * @notice Simulates a device attempting to unlock the door.
     * @dev This function will only execute successfully if called by an address
     * that is on the access list. Otherwise, it will revert.
     * @return A boolean indicating the success of the operation.
     */
    function unlockDoor() public view returns (bool) {
        require(hasAccess[msg.sender], "Access Denied: Device not on the list");
        // In a real-world scenario, this function might trigger an off-chain event
        // or interact with another contract. For this example, simply returning
        // true is enough to prove the access check worked.
        return true;
    }
}
