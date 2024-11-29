![Logo designed for Brave synthesiser](braveLogo.png)

Engineering an Embedded Network Bending Instrument, Manifesting Model Diversity in Neural Audio Synthesis

This repository catalogues technical development/software components of "Brave": an embedded, electro-acoustic network-bending instrument. As neural audio synthesis advances, inadvertently becoming an agent of cultural construction, we face increased risk of cultural homogenisation - autophagous AI feedback cycles suppressing atypical expression. The work seeks to contribute to the "network bending" framework - the direct manipulation of internal ML architecture to promote active divergence [1] from this monolithic output. 

Through a sequence of iterative user-feedback cycles, drawing from the Proof-Of-Concept (POC) implementation of Media and Arts Technology (MAT) studies [2], I propose a user-centred, embedded network-bending device. The work, it is hoped, will benefit musicians wishing to integrate alternative ML methods into their practice, and engineers exploring embedded neural audio synthesis.

## Embedded Network-bending

Blazej Kotowski is the first software engineer to open up the RAVE model and expose it to network-bending techniques. The artist/researcher present this work at the [Art Meets Radical Openness (AMRO) festival](https://radical-openness.org/en) in Linz, Austria. This work taps into this research, using [Kotowski’s network-bending fork](https://github.com/blazejkotowski/nn_tilde_bending) of the IRCAM [nn∼ repository](https://github.com/acids-ircam/RAVE). The decision was made to compile this work and embed it within a stand-alone instrument. The embedding is motivated by a Proof-Of-Concept (POC) exploration of embedded neural instruments, and to gauge how real-time neural synthesis can perform with current micro-computer technology. It is hoped that this POC can be scaled, motivating greater efficiency and reduced form factor as parallel processor architecture continues to advance. A Raspberry Pi 5 was chosen as the micro-computer of choice.

The most significant technical hurdle at this point was managing dependencies, ensuring libraries align with the 64-bit Arm processor, and compiling the project. The network-bending fork was opened in a CMake environment, which was used for dependency management and build generation. A compatible version of libtorch was found on [Q-engineering](https://qengineering.eu/install%20pytorch%20on%20raspberry%20pi%205.html). CMake was configured for the 64-bit arm processor architecture. A full bash/CMake scipt, which can reproduce this embedding on other devices with the same architecture, can be found on the Brave project repository []. This builds a Pure Data external, which can then be opened in a new patch.

## Networking

## Computational Architecture

**References**  

[1] [Broad, T., Berns, S., Colton, S., and Grierson, M. Active divergence with generative deep learning - A survey and taxonomy. CoRR abs/2107.05599 (2021).](https://www.researchgate.net/publication/353208260_Active_Divergence_with_Generative_Deep_Learning_--_A_Survey_and_Taxonomy)

[2] [Bryan-Kinns, N., and Reed, C. N. A guide to evaluating the experience of media and arts technology, 2023.](https://arxiv.org/abs/2311.07490)