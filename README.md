
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

<table align="center">
  <tr>
    <td align="center">
      <img src='/Images/Image 3.png' width="300">
    </td>
  </tr>
  <tr>
    <td align="center">
      <em>Fig. 2. User's choice between encrypting and decrypting </em>
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

- [1] **BAHIENSE, Beatriz.** Environmental Education Quiz. *Racha Cuca*, 2014. Updated on Feb. 5, 2020. Available at: [rachacuca.com.br](https://rachacuca.com.br/quiz/77475/educacao-ambiental/). Accessed on: Apr. 25, 2024.

- [2] **BRUMATTI, Gabriela.** Entering the Red: the planet is about to exhaust the natural resources it had for 2021. *g1*, July 28, 2021. Available at: [g1.globo.com](https://g1.globo.com/sp/campinas-regiao/terra-da-gente/noticia/2021/07/28/entrando-no-vermelho-planeta-esta-prestes-a-esgotar-os-recursos-naturais-que-tinha-para-2021.ghtml). Accessed on: Apr. 3, 2024.

- [3] **CÉREBRO BINÁRIO.** Basic Java Beginner - Quiz Questions and Answers Program. *Cérebro Binário Channel*, published on Nov. 22, 2019. Available at: [YouTube](https://www.youtube.com/watch?v=grC4zaq01Vs). Accessed on: Apr. 25, 2024.

- [4] **DEV MEDIA.** Main Concepts about Interfaces. *DEV MEDIA*, [n.d.]. Available at: [devmedia.com.br](https://www.devmedia.com.br/interfaces-programacao-orientada-a-objetos/18695). Accessed on: Apr. 5, 2024.

- [5] **ELADIO, Nvutu.** OOP – Object-Oriented Programming: Complete Guide. *Dio*, [n.d.]. Available at: [dio.me](https://www.dio.me/articles/poo-programacao-orientada-a-objetos-guia-completo). Accessed on: Apr. 3, 2024.

- [6] **eCycle TEAM.** Deforestation: impacts, causes, and consequences. *eCycle*, [n.d.]. Available at: [ecycle.com.br](https://www.ecycle.com.br/desmatamento/). Accessed on: Mar. 18, 2024.

- [7] **Alura GROUP.** OOP: what is object-oriented programming? *Alura*, [n.d.]. Available at: [alura.com.br](https://www.alura.com.br/artigos/poo-programacao-orientada-a-objetos#:~:text=farol%20do%20carro-,Encapsulamento%2C%20heran%C3%A7a%20e%20polimorfismo%3A%20as%20principais%20caracter%C3%ADsticas%20da%20POO,alguns%20problemas%20da%20programa%C3%A7%C3%A3o%20estruturada). Accessed on: Apr. 4, 2024.

- [8] **INDUSTRY A - Z.** Deforestation. *Portal da Indústria*, [n.d.]. Available at: [portaldaindustria.com.br](https://www.portaldaindustria.com.br/industria-de-a-z/desmatamento/#:~:text=O%20desmatamento%20%C3%A9%20a%20remo%C3%A7%C3%A3o,minera%C3%A7%C3%A3o%20e%20infraestrutura%20e%20urbana). Accessed on: Mar. 18, 2024.

- [9] **MAGALHÃES, Lana.** Global Warming. *Toda Matéria*, [n.d.]. Available at: [todamateria.com.br](https://www.todamateria.com.br/aquecimento-global/). Accessed on: Mar. 5, 2024.

- [10] **WHAT ARE Greenhouse Gases?** *ABNT Online*, [n.d.]. Available at: [abntonline.com.br](https://www.abntonline.com.br/sustentabilidade/GHG/O_que_%C3%A9_gee). Accessed on: Mar. 6, 2024.

- [11] **OLIVEIRA, Paulo.** Object-Oriented Programming - When to Use this Resource? *Escola Linux*, [n.d.]. Available at: [nova.escolalinux.com.br](https://nova.escolalinux.com.br/blog/programacao-orientada-a-objetos-quando-utilizar-esse-recurso#:~:text=O%20que%20%C3%A9%20Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos%20(POO)%3F&text=Na%20POO%2C%20um%20objeto%2C%20%C3%A9,a%20execu%C3%A7%C3%A3o%20de%20a%C3%A7%C3%B5es%20espec%C3%ADficas). Accessed on: Apr. 4, 2024.

- [12] **PASSOS, R.; PARREIRA, F. J.; ULBRICHT, V. R. (Orgs.).** The Emerging Innovation: Technologies and Interfaces [Ebook]. Goiânia: CEGRAF UFG, 2020. Available at: [publica.ciar.ufg.br](https://publica.ciar.ufg.br/ebooks/cinahpa_a_inovacao_emergente/index.html). Accessed on: Apr. 8, 2024.

- [13] **AIR Quality National Policy will proceed urgently.** *Senate Agency*, Mar. 5, 2024. Available at: [senado.leg.br](https://www12.senado.leg.br/noticias/materias/2024/03/05/politica-nacional-de-qualidade-do-ar-tramitara-em-regime-de-urgencia). Accessed on: Mar. 30, 2024.

- [14] **WHAT are the consequences of overexploitation of natural resources?** *Ministry of Education*, Nov. 4, 2021. Available at: [gov.br](https://www.gov.br/fundaj/pt-br/destaques/observa-fundaj-itens/observa-fundaj/revitalizacao-de-bacias/copy_of_quais-sao-as-consequencias-da-superexploracao-dos-recursos-naturais#:~:text=Os%20seres%20humanos%20est%C3%A3o%20esgotando%20esses%20recursos%20naturais%20do%20planeta,est%C3%A1%20criando%20um%20enorme%20d%C3%A9ficit). Accessed on: Apr. 5, 2024.

- [15] **WHO, WMO, and UN Environment Programme.** *Air Quality and Health*. Geneva: World Health Organization, 2021. Available at: [who.int](https://www.who.int/teams/environmental-health-and-safety/air-quality-and-health). Accessed on: Mar. 30, 2024.

- [16] **ARAÚJO, Flávio.** What is Deforestation? *Portal da Indústria*, [n.d.]. Available at: [portaldaindustria.com.br](https://www.portaldaindustria.com.br/industria-de-a-z/desmatamento/o-que-e-desmatamento/). Accessed on: Apr. 10, 2024.

- [17] **WATTS, Jonathan.** "The World’s Water Crisis: 2.7 Billion People Face Water Scarcity." *The Guardian*, Aug. 7, 2023. Available at: [theguardian.com](https://www.theguardian.com/environment/2023/aug/07/water-crisis-scarcity-climate-change). Accessed on: Apr. 15, 2024.

- [18] **UNION OF CONCERNED SCIENTISTS.** "Climate Change Impacts." Available at: [ucsusa.org](https://www.ucsusa.org/resources/climate-change-impacts). Accessed on: Apr. 15, 2024.

- [19] **WORLD WILDLIFE FUND.** "Deforestation: Causes and Consequences." Available at: [worldwildlife.org](https://www.worldwildlife.org/threats/deforestation-and-forest-degradation). Accessed on: Apr. 15, 2024.

- [20] **FOOD AND AGRICULTURE ORGANIZATION OF THE UNITED NATIONS.** "State of the World’s Forests 2020." Available at: [fao.org](https://www.fao.org/state-of-forests/en/). Accessed on: Apr. 15, 2024.

- [21] **IPCC.** "Climate Change 2022: Impacts, Adaptation, and Vulnerability." Available at: [ipcc.ch](https://www.ipcc.ch/report/ar6/wg2/). Accessed on: Apr. 15, 2024.
