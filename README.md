#PGP2IMG
### The easiest way to discreetly protect your files

![](http://newshour-tc.pbs.org/newshour/wp-content/uploads/2014/04/Niedringhaus-Anja_Afghanistan-2011.jpg)

[Download](https://github.com/icefalcn/pgp2img/archive/master.zip)

## Security

PGP2IMG utilizes [keybase's](https://keybase.io) public key encryption which also provides verifiable identities so your work can never be impersonated

Advanced steganography techniques securely transport and store your files

Make sure your files get back home even through the most oppressive government regimes

## Features

* Encrypt / Decrypt hidden PGP message hidden inside media files
* Encrypt / Decrypt hidden Saltpack signed files inside media files
* Ability to store encrypted files inside Keybase Filesystem   (kbfs)

## How to use

1. Install and setup keybase on your computer if this is not already done
2. Fire up your favorite terminal on your computer
3. Type the following line and fill in the square brackets accordingly
   
        ./main.py encrypt -m [keybase user] [message] [file path]
           
        ./main.py encrypt -i [keybase user] [file to hide] [file]
        
        ./main.py decrypt [file path]

## Built by

* [Justin Leger](https://justinleger.ca) - @jusleg
* [Michael Liu](https://ca.linkedin.com/in/michael-liu-b7b2b0115) - @icefalcn
* [Teodor Voinea](https://ca.linkedin.com/in/teodorvoinea) - @teovoinea

## License

MIT License

Copyright (c) 2017 Justin Léger, Michael Liu, Teodor Voinea

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
