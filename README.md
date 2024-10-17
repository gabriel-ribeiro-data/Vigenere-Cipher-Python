
# Implementation of the Vigenère cipher in Python
----

### This repository contains the development of a Python-based implementation of the Vigenère cipher, created during my undergraduate studies in Computer Science. Please note that the language of the implementation is in the authors' native language (Brazilian Portuguese).
----

## Introduction
  This project consists of developing a software application using the Python programming language, focused on implementing the Vigenère cipher. The main objective is to create an application capable of demonstrating the encryption and decryption process of the Vigenère cipher in an interactive and educational format. Additionally, the aim is to provide a clear and accessible implementation, helping users understand the algorithm's functionality and its applications in cryptography, thereby enhancing their knowledge of data security concepts and practices. 
  
  The Vigenère cipher is a cryptographic method that uses a keyword to encode a message. It is a technique of polyalphabetic substitution, which means that each letter of the original message can be replaced by different letters of the alphabet, depending on the corresponding letter in the keyword. The main advantage of this method is that it is less predictable compared to simple techniques, such as the Caesar cipher, where each letter is uniformly shifted.

## Vigenere Table
  The Vigenère cipher employs a table known as the Vigenère table, which includes all combinations of letters in the alphabet. This table is organized as a matrix, with each row beginning with a different letter of the alphabet, and each column corresponding to a letter that is to be encoded.

  To encode a message, the first step is to align the letters of the plaintext message with the letters of the keyword. For each letter in the plaintext, the corresponding letter from the keyword is used to determine the appropriate row in the Vigenère table. The column is determined by the letter of the plaintext. The intersection of the selected row and column gives the encoded letter.

  For example, if we want to encode the letter 'H' from the plaintext using the letter 'L' from the keyword, we find the row starting with 'L' and look for the column under 'H'. The letter at the intersection is the encoded letter. This process is repeated for each letter in the plaintext, resulting in a ciphertext that is less predictable and more secure than simple substitution methods. The Vigenère table is shown in Fig. 1.

<table align="center">
  <tr>
    <td align="center">
      <img src='/Images/Image 1.png' width="400">
    </td>
  </tr>
  <tr>
    <td align="center">
      <em>Fig. 1. Vigenère Table </em>
    </td>
  </tr>
</table>

## Vulnerabilities and Weaknesses
  One of the main weaknesses of the Vigenère cipher arises from the fact that it does not conceal the letter frequencies in the original text. If an attacker knows or suspects that the Vigenère cipher is being used and can determine the length of the key, they can perform frequency analysis on groups of encrypted letters to identify patterns, which will reveal information about the key.

  Furthermore, there is another significant issue with the Vigenère cipher concerning the size of the key. If the key is too short relative to the length of the original text, the cipher becomes more vulnerable to brute force attacks, as there are fewer possible variations of the key to be tested.

## Running Application
  After opening the program, the user is presented with two options and must choose one of them, with the first option being “1 - Encrypt” and the second option “2 - Decrypt.” The user needs to enter “1” or “2” respectively to indicate the desired operation. If the user makes an invalid entry, the message “Please enter only '1' or '2':” will appear, repeating the two options above until a valid entry is made. Fig. 2 below illustrates the described situation.
  
<table align="center">
  <tr>
    <td align="center">
      <img src='/Images/Image 2.png' width="300">
    </td>
  </tr>
  <tr>
    <td align="center">
      <em>Fig. 2. User's choice between encrypting and decrypting </em>
    </td>
  </tr>
</table>
<br>

  Fig. 3 shows the complete operation of the application running, including input prompts and the output results generated during the encryption and decryption processes. This illustration provides a clear overview of how the application functions in real-time, demonstrating its capabilities and user interaction through console inputs and outputs.

<table align="center">
  <tr>
    <td align="center">
      <img src='/Images/Image 3.png' width="500">
    </td>
  </tr>
  <tr>
    <td align="center">
      <em>Fig. 3. Example of the Application Running </em>
    </td>
  </tr>
</table>

## Authors

* Gabriel Ribeiro Fernandes
* Filipe Pires Barbosa
* João Pedro Marinho Rego Grippa
* Lorena Costa Minsoni 
* Lucas Henrique dos Santos Oliveira
* Maria Luiza Alves Dominicali

## References

- [1] BORGES, Izabella B. F. Types of Cryptography: How They Work and Their Importance. Clicksign, Barueri, Apr. 17, 2023. Available at: clicksign.com.br. Accessed on: Oct. 8, 2023.

- [2] Caesar Cipher. Wikipedia, 2023. Available at: wikipedia.org. Accessed on: Sept. 26, 2023.

- [3] Vigenère Cipher. Wikipedia, 2023. Available at: wikipedia.org. Accessed on: Sept. 26, 2023.

- [4] Confederate Cipher Disc. Crypto Museum, 2023. Available at: cryptomuseum.com. Accessed on: Oct. 11, 2023.

- [5] Discover What Are the Types of Cryptography. DocuSign, Sept. 30, 2022. Available at: docusign.com.br. Accessed on: Oct. 7, 2023.

- [6] DONDA, Daniel. The Mathematics of the Vigenère Cipher. Daniel Donda, Aug. 31, 2010. Available at: danieldonda.com. Accessed on: Oct. 8, 2023.

- [7] DOS REIS, Fábio. Cryptography – Vigenère Cipher. Bóson Treinamentos, Sept. 6, 2016. Available at: bosontreinamentos.com.br. Accessed on: Oct. 8, 2023.

- [8] FIELDS, Brandon T. Figure 1. Vigenère Table. 2011. Digital image. Available at: wikipedia.org. Accessed on: Oct. 26, 2023.

- [9] JAMAL, Taha. The Vigenère Cipher: A Story of Cryptography and Intrigue. Museum, Jan. 25, 2023. Available at: medium.com. Accessed on: Oct. 11, 2023.

- [10] KHANDURI, Ayush. Vigenère Cipher. Geeks for Geeks, May 29, 2023. Available at: geeksforgeeks.org. Accessed on: Sept. 26, 2023.

- [11] What is Data Encryption? Definition and Explanation. Kaspersky, 2023. Available at: kaspersky.com.br. Accessed on: Oct. 7, 2023.

- [12] What is Cryptography? AWS Amazon, 2023. Available at: aws.amazon.com. Accessed on: Oct. 7, 2023.

- [13] ROBOT, Marvin T. How a 17th Century Cipher Becomes an Unbreakable Cryptography? Kaspersky, Sept. 21, 2015. Available at: kaspersky.com.br. Accessed on: Sept. 26, 2023.

- [14] SILVA, Bárbara L. Cryptography and Codes: See the Main Ways to Hide Information Used Throughout History. QueroBolsa, Aug. 24, 2023. Available at: querobolsa.com.br. Accessed on: Sept. 26, 2023.

- [15] SIMMONS, Gustavus J. Vigenère Cipher. Britannica, 2023. Available at: britannica.com. Accessed on: Sept. 26, 2023.

- [16] Vigenère Cipher. Wikipedia, 2023. Available at: wikipedia.org. Accessed on: Oct. 11, 2023.
