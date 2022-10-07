# Bioinformatics-Projects
Mini projects for bioinformatics course at AUT, spring 2022. Implementations of Semi-Global alignment and MSA using PSSM profiles considering Gaps.

## [Semi-Global Alignment](https://github.com/hedzd/Bioinformatics-Projects/blob/main/Semi-Global-alignment.py)
Implementation of Semi-Global alignment for proteins with Dynamic Programming method. In this way, the gaps in the first and last alignment have not been considered in scoring. The PAM250 scoring matrix to score matches and mismatches penalties. For gaps, the constant penalty value is equal to 9.

### Input and output formats
The inputs are two protein strings that need to be semi-globally aligned with each other. The first line of the output shows the overall alignment score, while the remaining lines show every potential alignment form.
#### input sample: 
```
HEAGAWGHE
PAWHEA
```
#### output sample:
```
20
HEAGAWGHE-
---PAW-HEA
```

## [MSA using PSSM profiles](https://github.com/hedzd/Bioinformatics-Projects/blob/main/profile.py)  
In this project, a profile of an MSA have been created using PSSM matrix (considring gaps). Using that profile, find the part from a long input sequence that is most similar to the MSA. To avoid log(0), pseudocount = 2 was used. A sub-sequence from the input sequence with the highest score based on the PSSM profile would be the output once the profile had been built.

### Input and output formats  
The number of sequences in the MSA is given on the first line of the input, followed by a list of the sequences.In the last line comes a long sequence that the most-related sub-sequence should be detected in it (its length is at most 100.)  
The desired subsequence appears in the output.

#### input sample: 
```
4
HVLIP
H-MIP
HVL-P
LVLIP
LIVPHHVPIPVLVIHPVLPPHIVLHHIHVHIHLPVLHIVHHLVIHLHPIVL
```
#### output sample:
```
H-L-P
```
