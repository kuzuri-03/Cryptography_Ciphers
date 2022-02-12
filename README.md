# Cryptography_Ciphers

Cryptography is the use of coding to secure computer networks, online systems, and digital data. It is a concept whose endgame is to keep vital information that is subject to potential data breaches safe and confidential. While the term tends to be associated with the modern digital era, the concept has played a significant role for centuries in military and government operations. 

For example, the Navajo code talkers from World War II, who communicated in their native tongue, deployed cryptography tactics to convey crucial data.

Ciphers are arguably the corner stone of cryptography. In general, a cipher is simply just a set of steps (an algorithm) for performing both an encryption, and the corresponding decryption.

Despite might what seem to be a relatively simple concept, ciphers play a crucial role in modern technology. Technologies involving communication (including the internet, mobile phones, digital television or even ATMs) rely on ciphers in order to maintain both security and privacy.

The classical algorithms are those invented pre-computer up until around the 1950's. The list below is roughly ordered by complexity, least complex at the top.

Classical ciphers are cryptographic algorithms that have been used in the past (pre WWII). Some of them have only ever been used by amateurs (e.g. Bifid), while some of them have been used by armies to secure their top level communications (e.g. ADFGVX).

None of these algorithms are very secure as far as protecting information goes (with todays computers to break them), so if real data security is needed you should probably look at modern algorithms.

**Atbash Cipher**

The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed. I.e. all As are replaced with Zs, all Bs are replaced with Ys, and so on.
   
**ROT13 Cipher**

The ROT13 cipher is not really a cipher, more just a way to obscure information temporarily. It is often used to hide e.g. movie spoilers.

**Caesar Cipher**

The caesar cipher (a.k.a the shift cipher, Caesar's Code or Caesar Shift) is one of the earliest known and simplest ciphers.

**Affine Cipher**

A type of simple substitution cipher, very easy to crack.

**Rail-fence Cipher**

A simple transposition cipher.

**Baconian Cipher**

The Baconian cipher is a 'biliteral' cipher, i.e. it employs only 2 characters. It is a substitution cipher.

**Polybius Square Cipher**

The Polybius Square is essentially identical to the simple substitution cipher, except that each plaintext character is enciphered as 2 ciphertext characters.

**Simple Substitution Cipher**

A simple cipher used by governments for hundreds of years. Code is provided for encryption, decryption and cryptanalysis.

**Codes and Nomenclators Cipher**

Nomenclators are a mix between substitution ciphers and Codes, used extensively during the middle ages. Codes in various forms were used up until fairly recently.

**Columnar Transposition Cipher**

Another simple transposition cipher in which letters are arranged in rows and the columns are transposed according to a key.
 
**Autokey Cipher**

The Autokey cipher is closely related to the Vigenere cipher, it differs in how the key material is generated. The Autokey cipher uses a key word in addition to the plaintext as its key material, this makes it more secure than Vigenere.
**Beaufort Cipher**

Very similar to the Vigenere cipher, but slightly different algorithm.

**Porta Cipher**

The Porta cipher is a polyalphabetic substitution cipher that uses a keyword to choose which alphabet to encipher letters.

**Running Key Cipher**

The Running Key cipher is similar to the Vigenere cipher, but the key is usually a long piece of non-repeating text. This makes it harder to break in general than the Vigenere or Autokey ciphers.

**Vigenère and Gronsfeld Cipher**

A more complex polyalphabetic substitution cipher. Code is provided for encryption, decryption and cryptanalysis.

**Homophonic Substitution Cipher**

The Homophonic Substitution cipher is a substitution cipher in which single plaintext letters can be replaced by any of several different ciphertext letters. They are generally much more difficult to break than standard substitution ciphers.

**Four-Square Cipher**

An algorithm invented by Felix Delastelle, published in 1902

**Hill Cipher**

An algorithm based on matrix theory. Very good at diffusion.

**Playfair Cipher**

The technique encrypts pairs of letters (digraphs), instead of single letters as in the simple substitution cipher. The Playfair cipher is thus significantly harder to break since the frequency analysis used for simple substitution ciphers does not work with it.

**ADFGVX Cipher**

A fractionating transposition cipher. Used by the Germans during the first world war, but cracked by the French. Quite a difficult cipher to break.

**ADFGX Cipher**

A fractionating transposition cipher. Used by the Germans during the first world war, closely related to ADFGVX (Note the extra V in the name).

**Bifid Cipher**

A fractionating transposition cipher. Only ever used by amateur cryptographers. Can be broken fairly easily.

**Straddle Checkerboard Cipher**

A substitution cipher with variable length substitutions.

**Trifid Cipher**

A fractionating transposition cipher. A variant of Bifid.

**Base64 Cipher**

Base64 isn't really a cipher, but I see it used all the time for "enciphering" text, so it gets an honorary mention.

**Fractionated Morse Cipher**

Fractionated Morse first converts the plaintext to morse code, then enciphers fixed size blocks of morse code back to letters. This procedure means plaintext letters are mixed into the ciphertext letters i.e. one plaintext letter does not map to one ciphertext letter.

