// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NFT91 is ERC721 {
    address public contractOwner;
    uint256 public tokenCounter;

    mapping(uint256 => address) public tokenIdToOwner;
    event ownerMapped(uint256 indexed tokenId, address indexed owner);

    modifier onlyOwner() {
        require(msg.sender == contractOwner);
        _;
    }

    constructor() public ERC721("NFT91", "nft91") {
        contractOwner = msg.sender;
        tokenCounter = 0;
    }

    function createToken() public {
        tokenIdToOwner[tokenCounter] = msg.sender;
        emit ownerMapped(tokenCounter, msg.sender);
        _safeMint(msg.sender, tokenCounter);
        tokenCounter++;
    }

    function tokenListingFee() public payable {
        uint256 listing_fee = 0.0025 * 10**18;
        require(msg.value >= listing_fee, "You need to pay more ETH!");
    }

    function setTokenURI(uint256 tokenId, string memory tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "Only approved or owner can set token URI"
        );
        _setTokenURI(tokenId, tokenURI);
    }

    function withdraw() public payable onlyOwner {
        msg.sender.transfer(address(this).balance);
    }
}
