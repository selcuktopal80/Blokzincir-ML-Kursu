// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MerhabaDunya {
    
    string public mesaj;

    uint sayi1 = 2;
    uint sayi2 = 4;
 
   function SonucYazdir() public view returns(uint carpim, uint toplam){
      carpim = sayi1 * sayi2;
      toplam = sayi1 + sayi2;
   }
     
    function mesajiAyarla(string memory _mesaj ) public {
        
        mesaj = _mesaj;
    }
    
    function mesajiSoyle () view public returns (string memory) {
        return mesaj;
    }

}