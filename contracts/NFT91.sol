// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NFT91 is ERC721 {
    address public contractOwner;
    uint256 public tokenCounter;
    uint256 minListingPrice = 0.0025 * 10**18;

    constructor() public ERC721("NFT91", "nft91") {
        contractOwner = msg.sender;
    }
}
