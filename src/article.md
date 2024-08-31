# Ribosome Translation In Eukaryotes
**Tal Shachar**, **Noa David**, **Raz Cohen**

In collaboration with **Dr. Shimon Schocken**

## 1. Introduction
### 1.1: Idea
In this paper, instead of taking two smaller problems and seperating them into implementation and a purely informational article, together with Dr. Schocken we worked on making a sort of prototype for a future project Dr. Schocken is curious about. Said project would deal heavily with biologic and chemical subjects such as Ribosome Translation and mRNA/DNA, and this project was a stride at discovering those subjects through the lense of a Computer Software engineer/researcher.

### 1.2: Final Product
The initial concept for the project was simulating the process of translating mRNA - the coding for genomes in DNA - into poly-peptide chains, which are strands of the amino-acids that eventually take the forms of the proteins that make up all life.

We decided to develop upon this concept by grounding it in actual life, both to give semantic meaning to this process (Since proteins and amino-acids are purely-virtual entities when simulating them), and to discover this interesting subject a bit more.

> The final product is able to take in DNA code for a protein, exactly as coded inside human chromosomes, transcript it and finally tranlate it to proteins, all while being able to identify a sort of mutation that makes up a huge part of genetic rooted conditions.


## 2. Theoretical Background
In order to understand the pipeline of the project, the entire process from DNA to proteins can be seperated to serveral parts.

### 2.1: DNA (Deoxyribonucleic Acids) Transcription
All code and genes expressed in the life we see is written in molecules called DNA molecules, that appear in all living cells. Those molecules are composed of strands made up of _Nucleotides_, a molecule that can be thought of computer bits, with 4 states instead of 2. A strand of nucleotides can contain:
* Control Statements - Indications for the translator for beginning translation or ending it.
* Codons - Different codings for different amino-acids to be produced throughout the translation process
* Segment Seperation - Without any semantics, such nucleotide sequences can be a sign or indication for when the aforementioned types appear.

> Said nucleotides take different forms when in DNA or RNA;
$
N_{DNA} \in \{ A, T, C, G \}
$,
$
N_{RNA} \in \{ A, U, C, G \}
$.

The first step from DNA torwards translation of a protein is called Transcription.
A part of the DNA corresponding to a single gene is copied from the DNA nucleotide sequence; that copy is called an RNA seqeuence.
The data written in the RNA is pretty much that same as the data written in that section of the DNA, except for the replacement of the _T_(Thymine) Nucleotide with the _U_(Uracil) nucleotide. The other necleotides - Guanine, Cytosine and Adenine, are kept the same.

Just as in DNA, where Thymine and Adenine create hydrogen bonds that cause the attraction between the two, Uracil and Adenine also attract each other. The other pair, Cytosine and Guanine remain the same, also forming the same bonds.

> DNA is a double-helixed molecule, meaning that a single molecule of DNA is composed of two strands, held together by the bonds mentioned above; the two strands are Nucleotide complements of each other. The data copied from the DNA molecule comprises of a part of a single strand.

The product of the transcription process is called the precursor mRNA, or pre-mRNA for short. The mRNA molecule is released from the DNA strand and makes it's way to the Splicosome, where the Splicing Process occurs.

### 2.2: Splicing
The pre-mRNA sequence is composed of alternating parts called _Exons_ and _Introns_. Exons are the parts of the genetic code responsible for coding the amino-acid sequences that eventually become the proteins. Introns on the other hand, have no semantic meaning, and are structured in a way that makes identifying their edges possible using enzymes; We will dive deeper on this subject in the next parts. The part of the cell responsible for this identification is called the _Spliceosome_, which takes in said pre-mRNA, identifies where each Intron begins/ends and cuts those segments out, leaving only the coding Exons. The places where Introns were seperated are called Exon-Junction-Complex's (EJC), and are an integral part of the mutation identification process mentioned above.

The product created from this phase is called mRNA.

It is important to note that the Splicing process does not occur in Prokaryotes, such as bacteria like E. Coli. The splicing process only appears in Eukaryotes. In prokaryotes, the genes stored in the DNA are stored already as conjoined exons, meaning that immediately after transcription the mRNA is sent to the ribosome. This can cause problems with mutations as explained down below.

### 2.3: Translation
The mRNA sequence, despite being only made Exons, still has parts with no semantic meaning. Those parts are called Untranslated Regions, or UTRs for short. Those parts are easily identifiable using the Control Codons mentioned above; The Prefixed-UTR ends immediately before the first appearance of the _Begin Translation Instruction Codon_, and the Suffixed-UTR ends Begins immediately after the first appearance of the _Stop Translation Instruction Codon_.

Codon Instructions, similarly to computer instructions in some Computer Architectures, are of a fixed size of 3 Nucleotides; This means that there can only be $ 4^3 = 64 $ codon representations. Since only 20 amino-acids make up the human body (And similar organisms), this coding limit suffices. The entity responsible for carrying out this translation process is called the _Ribosome_, a part of the Cell.

Immediately after reaching the _Begin Translation Codon_, the Ribosome starts reading the mRNA, one nucleotide-triplet at a time.
The mapping between nucleotide-triplet codons and actual amino-acids in practice happens via tRNA molecules. Each of the 4 nucleotide has a _Complementing Nucleotide_ - a different necleotide who's chemical properties create attraction between the two, such as hydrogen bonds. Inside the cell are tRNA molecules - molecules generated by the Cell's Nucleus, with nucleotide triplets at one end and a corresponding amino-acid at the other end. Those nucleotides are exactly the complementing nucleotides for the triplet corresponding to the bound amino-acid, which causes said tRNA molecules to attract torwards codons of their amino-acids. This attraction takes place at the Ribosome's Translation Site, where one-by-one the amino-acid is seperated from the tRNA and connected to a chain of the amino-acids chained thus far.

When the end codon is read, the ribosome is signaled to release the amino-acid chain (The poly-peptide chain), which immediately folds into proteins such as Hemoglobin, Insulin and many others.

### 2.4: Mutation Identification
Since mutations and spontaneous changes in the chemical structures of molecules is not uncommon, cells evolved to be able to handle those changes with as little problems as possible. There are many ways a cell identifies such mutations, but the one we focused on in this project is called [Nonsense-Mediated-Decay](https://en.wikipedia.org/wiki/MRNA_surveillance#Nonsense-mediated%20mRNA%20decay:~:text=decay%20pathway%20(NGD).-,Nonsense%2Dmediated%20mRNA%20decay,-%5Bedit%5D). As a byproduct of the intron splicing process the spliceosome carries out, an EJC is placed where two exons were attached. This can inform the ribosome of information about what structure the gene had as a DNA strand, and not just as a sequence of Nucleotides.

This is very important for proper protein generation; if the polypeptide chain generation process is stopped prematurely, for example after 50 amino-acids instead of 100, a misshapen protein will emerge. This can cause immense damage to the cell or the entire organizm; an example of such genetic disease is [Cystic fibrosis](https://pubmed.ncbi.nlm.nih.gov/31585024/). Some instances of such mutation can be identified ahead of time, through a process called Nonsense-Mediated-Decay.

Since the exons are the parts of the gene responsible for coding a gene, the stop instruction always appears in the last exon on the gene, padded by an UTR. Using the EJC, the ribosome can identify where the last exon was once placed, before being conjoined with the other exons. This wouldn't have been possible had the DNA contained a pre-spliced strand of genetic code, since there would be no indication as to where the ending UTR starts and when the the stop codon should appear. The chemical and biological constraints of this mechanism are that the premature stop codon must appear at least 54 nucleotides ahead of the last exon-exon-junction (EEJ) for the nonsense to be identified. Once a ribosome detects such mutation nonsense, the partially constructed polypeptide chain is decayed and destroyed, with the amino acids being released back to the nucleus instead of being released as a misformed, dangerous partial protein.

> With a computer program on out hands we didn't have such evolutionary constraints such as the 54-nucleotide limit, but we still chose to implement it artificially to make the process as similar to the real cell's process as possible.

We also implemented another simpler mechanism of detecting mutations, [Nonstop Mediated mRNA Decay](https://en.wikipedia.org/wiki/MRNA_surveillance#Nonsense-mediated%20mRNA%20decay:~:text=upon%20further%20studies.-,Nonstop%20mediated%20mRNA%20decay,-%5Bedit%5D), which decays the polypeptide chain exactly as before, but does it in the case that a stop codon was missing from the mRNA. This requires no EJC knowledge, and therefore is possible to implement even when no splicing information is gathered.

> An example of a genetic disease caused by a missing stop codon is [Sickle-cell Anemia](https://www.mayoclinic.org/diseases-conditions/sickle-cell-anemia/symptoms-causes/syc-20355876), a very dangerous genetic disease.


## 3. Implementation
Our implementation is split to three components, all implemented in Python -

1. Model - The logical component of the project. This component is responsible for the logic behind parsing DNA, transcripting it into pre-mRNA, splicing the mRNA to exons and finally reading the conjoined exons and creating the final poly-peptide chain.
2. View - The visual component of the project. Responsible for painting and drawing the tRNA, mRNA, ribosome and other entities on screen without being bothered with the semantics tied to those elements.
3. Controller - A small component with the role of a proxy between the Model and the View component. Responsible for managing the use of the Model component according to what happens on screen and according to what the user does.

We will know give thorough explanation of the implementation, logic and features used in writing each component.

### 3.1 Model
The model component implementation can be seen under the [./RNA](https://github.com/TalSShachar/ribosome-sim/tree/main/src/RNA) subdirectory in the github repository.

Firstly, we implemented the Nucleotide and Codon data structures. The nucleotide representation we chose is a flag enum - a number consisting of disjoined base flags responsible for each of the four different Nucleotides. This means that each of the four nucleotide is of the form $2^k$ where $0 \leq k \leq 3$. This allows us to build concepts used for the Codons. Since some codons have a few representations - for example, the stop codon that can be coded as either UAA, UGA, and UAG - we chose to give nucleotides the feature of not being concrete, but as a number that represents some options. When the final mRNA is read, each nucleotide in the mRNA strand has a single bit turned on, since the nucleotides in that strand are concrete and are not conceptual constructs.

Thanks to [information on the internet](https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#:~:text=possible%20start%20codon%20%E2%87%92-,Standard%20genetic%20code,-%5B1%5D), we were able to map all nucleotide triplets to amino-acid/control codons, in a concise manner made possible by the Flag enum paradigm.

Next comes the CodonReader, which is a software grounded name for the Ribosome. The class on construction takes in the codon patterns it is able for identifying (All 20 amino acids and codon instruction in our case), and uses a one-to-one mapping of each concrete match of a codon to a number in [0, 63]. This allows us to treat nucleotide triplets as a 3 digit number in base 64, and use this number as an indexer to an array to find in $\Theta(1)$ the matching codon for a read nucleotide triplet.

> They way we chose to implement the reading method was using a python Generator function, that allows a function to lazily generate a stream of results without running to completion. This means that even though a call to the method is bound to fail, some amino-acids can still be be read until an error happens or until the chain is complete. This simulates the real life process, since parsing and translating the mRNA is not an atomic and immediate process in the ribosome.

The last component we implemented was the Spliceosome. Building upon what we said above, lets go over the splicing process.

The alternating layout of the pre-mRNA means that if we can identify where an exon ends and an intron starts (and the other way around), we can splice all introns out. The location where the exon ends is called the 5' (Pronounced five-prime) splice site, and the location where the intron ends is called the 3' Splice site.

The identification of tose splice sites is made possible by concensus sequences that evolved through time, that are identified by a lot of proteins and enzymes produced by the cell of Eukaryotes. Since enzymes are not a part of Python, we used Regex and scoring algorithms to identify those sequences.

The first sequence - the 5' splice sequence - is pretty simple to identify. A concensus sequence known as MAG/GURAGU is used to find the boundary between the exon and the intron downstream. In the sequence, $M\in \{A, C\}, R\in \{A, G\}$, and "/" marks where the exon ends and where the intron begins. Using a regex pattern, we can identify this pretty easily.
> It is important to know that the process of splicing is very stochastic, and cannot be simplified to 2 Regex's. The process is carried out by several complex machines, proteins and enzymes inside the cell, and even while some DNA sequences contain splice sequences that differ a bit from the MAG/GURAGU concensus sequences, sequences called Splice Enhancers/Silencers can help the spliceosome identify the splice sites better. Without a large training set an a neural/stochastic network/model this process cannot be implemented efficiently, so we sticked with a simpler model to shine light on this process's features and not implement it perfectly.

The second sequence is the 3' splice site concensus sequence. It is a very short sequence - YAG. Y stands for a pyrimidine, which is either C or U. Since this sequence is very short and unavoidably will occur in DNA sequences, we implemented some of the Splice Enhancers used by the Spliceosome.

The first is a poly-pyrimidine tract - a sequence of ~20 nucleotides immediately upstream of the 3' splice site, very rich in pyrimidines. In order to identify the poly-pyrimidine tract we look at suffixes from 16 to 21 nucleotides long and measure the ratio between pyrimidines and purines (A or G, the remaining nucleotides in RNA). If the ratio is high enough, we consider the sequence to be a polypyrimidine tract.

The next is the Branch Point Sequence (BPS) - a sequence of the form _YNYURAY_, where Y is a pyrimidine, R is a purine, and N is any nucleotide. The BPS usually appears between the 40 to 20 last nucleotides in the intron. So, when we find a 3' splice sequence that we consider a candidate to be the point that we would call the end of the current intron and consequently splice at, the existence of a branch point sequence gives us more confidence in the locations we identified.

After we found the 5' splice site, we choose the 3' splice site according to the splice site concensus sequence. We then rank each of the 3' splice sites found according to 3 criteria -

1. The overall percentage of Pyrimidines in the Poly Pyrimidine tract in the end of the resulting intron - We take the $ratio^{3}$ to create a bias torwards higher percentage, which gives a number in [0, 1]. This number is multiplied against the amount of 'points' we are willing to give based on this criteria.
2. BPS existence - If we found a BPS in the expected location, we give extra points of a predetermined amount.
3. Resulting Intron Length - Even if we found a very promising poly-pyrimidine tract and a 3' splice site concensus sequence, we need to take into accound the resulting length of the intron if we were to mark it's end right there. If that intron would end up being of length 40 nucleotides, we would not want to consider it, since introns in human genomes are of at least 70 nucleotides. Similarly, we wouldn't want to splice in points where the resulting intron would be too long. To make up for this, we chose to also give points based on the delta between the resultin intron's length and the average intron size in human genomes. We find the biggest and smallest deltas, and normalize each delta for each intron to a number in [0, 1]. We take this number and give it a bias such that very small numbers become much smaller and that very big numbers become much bigger. We take the final number in [0, 1] and multiply it by the max amount of points we are willing to give in that criteria.

In the end, we sort the resulting intron ends by the score we have given them, and take the splice site with the highest score. At that point we cut the intron out, and proceed to find the next intron.

At the end of this process we have a chain of Exons, that are fed to the CodonReader. Each node of this chain indicates an EJC, and that way the nonsense mediated decay can be carried out by the ribosome.

> It is important to note that we developed this approach, and that given exotic inputs our code would likely fail. We have examples where our code properly identifies such splice sequences, but in real life genetic databases the coding sequences, along with the actual exon and intron boundaries are long available, and given those database, much more dependable and accurate machine learning models have been developed. For example, one paper we looked at used Markov Chains along with 10 different splice ehancer identifications to accurately identify splice sites. This model was built atop thousands of genetic sequences, and we cannot expect to compete with such methods.

### 3.2 View: Visualization with Pygame
The visualization component of our project was implemented using Pygame, a Python library designed for writing video games but versatile enough for general graphical applications. This component is responsible for visually representing the complex processes of mRNA translation, tRNA interaction, and ribosome function.

We structured the visualization into several key classes, each corresponding to the biological entities they represent:

1. **mRNA**: Displays the sequence of nucleotides, along with the codons that are read by the ribosome.
2. **tRNA**: Represents the tRNA molecules, each carrying specific amino acids, and visually aligning with the mRNA to deliver the correct amino acid.
3. **Ribosome**: Simulates the movement along the mRNA strand, reading codons, and facilitating the assembly of the poly-peptide chain.
4. **Amino Acid**: Visually depicts the growing poly-peptide chain as amino acids are added.

The `Simulation` class manages the overall logic, ensuring that the visualization updates correctly as the simulation progresses. This includes handling the movement of tRNA molecules, the ribosome's progression along the mRNA strand, and the assembly of the poly-peptide chain.

The `Visualizer` class, which acts as a general-purpose drawing utility, handles the rendering of these components on the screen. It abstracts away the complexity of Pygame, allowing the simulation logic to focus on the biological processes rather than the intricacies of graphical rendering.

Through this Pygame-based visualization, users can observe the dynamic interactions between tRNA, mRNA, and the ribosome, gaining a deeper understanding of the translation process in an interactive and engaging way.


