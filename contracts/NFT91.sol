// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NFT91 is ERC721 {
    address public contractOwner;
    uint256 public tokenCounter;
    uint256 minListingPrice = 0.0025 * 10**18;

    mapping(uint256 => address) public tokenIdToOwner;
    event ownerMapped(uint256 indexed tokenId, address indexed owner);

    constructor() public ERC721("NFT91", "nft91") {
        contractOwner = msg.sender;
    }

    function createToken() public payable {
        require(msg.value >= minListingPrice, "Listing price is too low");
        tokenIdToOwner[tokenCounter] = msg.sender;
        emit ownerMapped(tokenCounter, msg.sender);
        _safeMint(msg.sender, tokenCounter);
        tokenCounter++;
    }

    function setTokenURI(uint256 tokenId, string memory tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "Only approved or owner can set token URI"
        );
        _setTokenURI(tokenId, tokenURI);
    }
}
