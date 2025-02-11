Author: **Alëna Aksënova** <alena.aksenova@stonybrook.edu> <br>
Readme last updated: October 3, 2019


# [_SigmaPie_](https://github.com/alenaks/SigmaPie) for subregular grammar induction

## Subregular languages in phonology

This toolkit is relevant for anyone who is working or going to work with subregualar grammars both from the perspectives of theoretical linguistics and formal language theory.

**Why theoretical linguists might be interested in formal language theory?** <br>
_Formal language theory_ explains how potentially infinite string sets, or _formal languages_,
can be generalized to grammars encoding the desired patterns and what properties those
grammars have. It also allows one to compare different grammars regarding parameters such as expressivity.

**The Chomsky hierarchy** aligns the main classes of formal languages with respect to their expressive power [(Chomsky 1959)](http://www.cs.utexas.edu/~cannata/pl/Class%20Notes/Chomsky_1959%20On%20Certain%20Formal%20Properties%20of%20Grammars.pdf).

  * **Regular** grammars are as powerful as finite-state devices or regular expressions: they can "count" only until a certain threshold (no $a^{n}b^{n}$ patterns);
  * **Context-free** grammars have access to potentially infinite _stack_ that allows them to reproduce patterns that involve center embedding;
  * **Mildly context-sensitive** grammars are powerful enough to handle cross-serial dependencies such as some types of copying;
  * **Context-sensitive** grammars can handle non-linear patterns such as $a^{2^{n}}$ for $n > 0$;
  * **Recursively enumerable** grammars are as powerful as any theoretically possible computer and generate languages such as $a^n$, where $n \in \textrm{primes}$.



<img src="tutorial/images/chomhier.png" width="600">


Both phonology and morphology frequently display properties of regular languages.

**Phonology** does not require the power of center-embedding, which is a property of context-free languages. For example, consider a harmony where the first vowel agrees with the last vowel, the second vowel agrees with the pre-last one, etc.
    
    GOOD: "arugula", "tropicalization", "electrotelethermometer", etc.
    BAD:  any other word violating the rule.


While it is a theoretically possible pattern, harmonies of that type are unattested in natural languages.

**Morphology** avoids center-embedding as well. In [Aksënova et al. (2016)](https://www.aclweb.org/anthology/W16-2019) we show that it is possible to iterate prefixes with the meaning "after" in Russian. In Ilocano, where the same semantics is expressed via a circumfix, its iteration is prohibited.
    
    RUSSIAN: "zavtra" (tomorrow), "posle-zavtra" (the day after tomorrow), 
             "posle-posle-zavtra" (the day after the day after tomorrow), ...
    ILOCANO: "bigat" (morning), "ka-bigat-an" (the next morning),
             <*>"ka-ka-bigat-an-an" (the morning after the next one).


Moreover, typological review of patterns shows that phonology and morphology do not require the full power of regular languages. As an example of an unattested pattern, [Heinz (2011)](http://jeffreyheinz.net/papers/Heinz-2011-CPF.pdf) provides a language where a word must have an even number of vowels to be well-formed.


Regular languages can be sub-divided into another nested hierarchy of languages decreasing in their expressive power: **subregular hierarchy**.
Among some of the most important characteristics of subregular languages is their learnability only from the positive data: more powerful classes require negative input as well.


<img src="tutorial/images/subreg.png" width="250">


The _SigmaPie_ toolkit currently contains functionality for the following subregular language and grammar classes:
  * strictly piecewise (SP);
  * strictly local (SL);
  * tier-based strictly local (TSL);
  * multiple tier-based strictly local (MTSL).

## The functionality of the toolkit

  * **Learners** extract grammars from string sets.
  * **Scanners** evaluate strings with respect to a given grammar.
  * **Sample generators** generate stringsets for a given grammar.
  * **FSM constructors** translate subregular grammars to finite state machines.
  * **Polarity converters** switch negative grammars to positive, and vice versa.

## How to run the code

### Way 1: running from the terminal
  1. Download the code from the [SigmaPie GitHub folder](https://github.com/alenaks/SigmaPie);
  2. Open the terminal and use `cd` to move to the `SigmaPie/code/` repository.
  3. Run Python3 compiler by typing `python3`.
  4. `from main import *` will load all the modules of the package.
 
  <img src="tutorial/images/terminal.png" width="650">
  
### Way 2: running from the Jupyter notebooks
  1. Download the code from the [SigmaPie GitHub folder](https://github.com/alenaks/SigmaPie).
  2. Modify the second line in the cell below so that it contains the correct path to `SigmaPie/code/`.
  3. Run that cell.


```python
%cd
%cd SigmaPie/code/

from main import *
```

## Strictly piecewise languages

**Negative strictly piecewise (SP)** grammars prohibit the occurrence of sequences of symbols at an arbitrary distance from each other. Every SP grammar is associated with the value of $k$ that defines the size of the longest sequence that this grammar can prohibit. Alternatively, if the grammar is positive, it lists all subsequences that are allowed in well-formed words of the language.

    k = 2
    POLARITY: negative
    GRAMMAR:  ab, ba
    LANGUAGE: accaacc, cbccc, cccacaaaa, ...
              <*>accacba, <*>bcccacbb, <*>bccccccca, ...
              
              
In phonology, an example of an SP pattern is _tone plateauing_ discussed in [Jardine (2015,](https://adamjardine.net/files/jardinecomptone-short.pdf) [2016)](https://adamjardine.net/files/jardine2016dissertation.pdf).
For example, in Luganda (Bantu) a low tone (L) cannot intervene in-between two high tones (H): L is changed to H in such configurations.
The prosodic domain cannot have more than one stretch of H tones.

**Luganda verb and noun combinations** ([Hyman and Katamba (2010)](http://linguistics.berkeley.edu/phonlab/documents/2010/Hyman_Katamba_Paris_PLAR.pdf), cited by [Jardine (2016)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B01C656A2B96316F3ADCC836BD2A6244/S0952675716000129a.pdf/computationally_tone_is_different.pdf))

  * /tw-áa-mú-láb-a, walúsimbi/ $\Rightarrow$ tw-áá-mu-lab-a, walúsimbi <br>
    ‘we saw him, Walusimbi’ <br>
    **HHLLL, LHLL**
    
  * /tw-áa-láb-w-a walúsimbi/ $\Rightarrow$ tw-áá-láb-wá wálúsimbi <br>
    ‘we were seen by Walusimbi’ <br>
    **HHHHHHLL**
    
  * /tw-áa-láb-a byaa=walúsimbi/ $\Rightarrow$ tw-áá-láb-á byáá-wálúsimbi <br>
    ‘we saw those of Walusimbi’ <br>
    **HHHHHHHHLL**
    
This pattern can be described using SP grammar $G_{SP_{neg}} = \{HLH\}$.

### Learning tone plateauing pattern

Let us say that `luganda` represents a "toy" example of tone plateauing (TP) pattern.


```python
luganda = ["LLLL", "HHLLL", "LHHHLL", "LLLLHHHH"]
```

Our goal will be to learn the SP generalization behind TP.

Negative and positive SP grammars are implemented as the class `SP()`. The next code cell initialized a positive SP grammar `tp_pattern`.


```python
tp_pattern = SP()
```

### Attributes of SP grammars
  * `polar` ("p" or "n") is the polarity of the grammar, by default, it is "p";
  * `alphabet` (list) is the set of symbols that the grammar uses;
  * `grammar` (list of tuples) is the list of allowed or prohibited substructures of the language;
  * `k` (int) is the size of the locality window of the grammar, by default, it is $2$;
  * `data` (list of string) is the learning sample;
  * `fsm` (FSM object) is the finite state device that corresponds to the grammar.
  
The initial step is to define the training sample and the alphabet.


```python
tp_pattern.data = luganda
tp_pattern.alphabet = ["H", "L"]
```

By default, the locality window of the grammar is $2$.


```python
print("Locality of the SP grammar:", tp_pattern.k)
```

SP attributes can be directly accessed. For example, let us change the locality of the window from $2$ to $3$:


```python
tp_pattern.k = 3
print("Locality of the SP grammar:", tp_pattern.k)
```

### Methods defined for SP grammars
  * `check_polarity()` and `switch_polarity()` display and change the polarity of the grammar;
  * `learn()` extracts prohibited or allowed subsequences from the training sample;
  * `scan(string)` tells if a given string is well-formed with respect to the learned grammar;
  * `extract_alphabet()` collects alphabet based on the data or grammar attributes;
  * `generate_sample(n, repeat)` generates $n$ strings based on the given grammar; by default, `repeat` is set to False, and repetitions of the generated strings are not allowed, but this parameter can be set to True;
  * `fsmize()` creates the corresponding FSM family by following the steps outlined in [Heinz and Rogers (2013)](https://www.aclweb.org/anthology/W13-3007);
  * `subsequences(string)` returns all $k$-piecewise subsequences of the given string;
  * `generate_all_ngrams()` generates all possible strings of the length $k$ based on the provided alphabet.

**Checking and changing the polarity of the grammar**

By default, the grammars are positive. The polarity can be checked by running the `check_polarity` method:


```python
print("Polarity of the grammar:", tp_pattern.check_polarity())
```

If the polarity needs to be changed, this can be done using the `switch_polarity` method. It will automatically switch the grammar, if one is provided or already extracted, to the opposite one.


```python
tp_pattern.switch_polarity()
print("Polarity of the grammar:", tp_pattern.check_polarity())
```

**Learning the SP grammar**

Method `learn` extracts allowed or prohibited subsequences from the learning sample based on the polarity of the grammar and the locality window.


```python
tp_pattern.learn()
print("Extracted grammar:", tp_pattern.grammar)
```

Indeed, it learned the TP pattern!

$n$-grams are represented as tuples of strings, because in this case, elements of the alphabet are not restricted to characters.

**Scanning strings and telling if they are part of the language**

`scan` takes a string as input and returns True or False depending on the well-formedness of the given strings with respect to the encoded grammar.


```python
tp = ["HHHLLL", "L", "HHL", "LLHLLL"]
no_tp = ["LLLLHLLLLH", "HLLLLLLH", "LLLHLLLHLLLHL"]

print("Tonal plateauing:")
for string in tp:
    print("String", string, "is in L(G):", tp_pattern.scan(string))
    
print("\nNo tonal plateauing:")
for string in no_tp:
    print("String", string, "is in L(G):", tp_pattern.scan(string))
```

**Generating a data sample**

Based on the learned grammar, a data sample of the desired size can be generated.


```python
sample = tp_pattern.generate_sample(n = 10)
print("Sample:", sample)
```

**Extracting subsequences**

Finally, this toolkit can be used also in order to extract subsequences from the input word by feeding it to the `subsequences` method.


```python
tp_pattern.k = 3
print("k = 3:", tp_pattern.subsequences("regular"), "\n")
tp_pattern.k = 5
print("k = 5:", tp_pattern.subsequences("regular"))
```

While SP languages capture multiple long-distance processes such as tone plateauings or some harmonies, they are unable to encode a blocking effect or purely local processes.

## Strictly local languages

**Negative strictly $k$-local (SL)** grammars prohibit the occurrence of consecutive substrings consisting of up to $k$ symbols. The value of $k$ defines the longest substring that cannot be present in a well-formed string of a language. Positive SL grammars define substrings that can be present in the language.

Importantly, to define _first_ and _last_ elements, SL languages use delimiters (">" and "<") that indicate the beginning and the end of the string.

    k = 2
    POLARITY: positive
    GRAMMAR:  >a, ab, ba, b<
    LANGUAGE: ab, abab, abababab, ...
              <*>babab, <*>abaab, <*>bababba, ...

In phonology, very frequently changes involve adjacent segments, and the notion of locality is therefore extremely important. The discussion of local processes in phonology can be found in [(Chandlee 2014)](http://dspace.udel.edu/bitstream/handle/19716/13374/2014_Chandlee_Jane_PhD.pdf).


**Russian word-final devoicing**

In Russian, the final obstruent of a word cannot be voiced. <br>
  * "lug" \[luK\] _meadow_ $\Rightarrow$ "lug-a" \[luGa\] _of the meadow_
  * "luk" \[luK\] _onion_ $\Rightarrow$ "luk-a" \[luKa\] _of the onion_
  * "porog" \[paroK\] _doorstep_ $\Rightarrow$ "porog-a" \[paroGa\] _of the doorstep_
  * "porok" \[paroK\] _vice_ $\Rightarrow$ "porok-a" \[paroKa\] _of the vice_

### Learning word-final devoicing

Assume the following toy dataset where the following mapping is defined:
  * "a" stands for a vowel;
  * "b" stands for a voiced obstruent;
  * "p" stands for any other consonant.


```python
russian = ["", "ababa", "babbap", "pappa", "pabpaapba" "aap"]
```

In this term, the Russian word-final devoicing generalization would be _"do not have "b" at the end of the word"_.

This pattern can then be described using SL grammar $G_{SL_{neg}} = \{b<\}$.

Let us initialize an SL object.


```python
wf_devoicing = SL()
wf_devoicing.data = russian
```

### Attributes of SL grammars
  * `polar` ("p" or "n") is the polarity of the grammar, by default, it is "p";
  * `alphabet` (list) is the set of symbols that the grammar uses;
  * `grammar` (list of tuples) is the list of allowed or prohibited substructures of the language;
  * `k` (int) is the size of the locality window of the grammar, by default, it is $2$;
  * `data` (list of string) is the learning sample;
  * `edges` (list of two characters) are the delimiters used by the grammar, the default value is ">" and "<";
  * `fsm` (FSM object) is the finite state device that corresponds to the grammar.
  
### Methods defined for SL grammars
  * `check_polarity()` and `switch_polarity()` display and change the polarity of the grammar;
  * `learn()` extracts prohibited or allowed substrings from the training sample;
  * `scan(string)` tells if a given string is well-formed with respect to a learned grammar;
  * `extract_alphabet()` collects alphabet based on the data or grammar;
  * `generate_sample(n, repeat)` generates $n$ strings based on the given grammar; by default, `repeat` is set to False, and repetitions of the generated strings are not allowed, but this parameter can be set to True;
  * `fsmize()` creates the corresponding FSA;
  * `clean_grammar()` removes useless $k$-grams from the grammar.

**Extracting alphabet and learning SL grammar**

As before, `learn()` extracts dependencies from the data. It simply extracts $k$-grams of the indicated size from the data, and the default value of $k$ is $2$.


```python
wf_devoicing.learn()
print("The grammar is", wf_devoicing.grammar)
```

In order to automatically extract the alphabet from the data, it is possible to run `extract_alphabet()`.


```python
print("The original value of the alphabet is", wf_devoicing.alphabet)
wf_devoicing.extract_alphabet()
print("The modified value of the alphabet is", wf_devoicing.alphabet)
```

**Changing polarity of the grammar**

The grammar outputted above is positive. If we want to capture the pattern using restrictions rather then the allowed substrings, we can `switch_polarity()` of the grammar:


```python
wf_devoicing.switch_polarity()
print("The grammar is", wf_devoicing.grammar)
```

**Scanning strings**

As before, `scan(string)` method returns True or False depending on the well-formedness of the given string with respect to the learned grammar.


```python
wfd = ["apapap", "papa", "abba"]
no_wfd = ["apab", "apapapb"]

print("Word-final devoicing:")
for string in wfd:
    print("String", string, "is in L(G):", wf_devoicing.scan(string))
    
print("\nNo word-final devoicing:")
for string in no_wfd:
    print("String", string, "is in L(G):", wf_devoicing.scan(string))
```

**Generating data samples**

If the grammar is non-empty, the data sample can be generated in the same way as before: `generate_sample(n, repeat)`, where `n` is the number of examples that need to be generated, and `repeat` is a flag allowing or prohibiting repetitions of the same strings in the generated data.


```python
sample = wf_devoicing.generate_sample(5, repeat = False)
print(sample)
```

**Cleaning grammar**

Potentially, a grammar that user provides can contain "useless" $k$-grams. For example, consider the following grammar:


```python
sl = SL()
sl.grammar = [(">", "a"), ("b", "a"), ("a", "b"), ("b", "<"),
              (">", "g"), ("f", "<"), ("t", "t")]
sl.alphabet = ["a", "b", "g", "f", "t"]
```

This grammar contains $3$ useless bigrams:
  
  * `(">", "g")` can never be used because nothing can follow "g";
  * `("f", "<")` is useless because there is no way to start a string that would lead to "f";
  * `("t", "t")` has both problems listed above.
  
Method `clean_grammar()` removes such $n$-grams by constructing a corresponding FSM and trimming its inaccessible states.


```python
print("Old grammar:", sl.grammar)
sl.clean_grammar()
print("Clean grammar:", sl.grammar)
```

Even though SP and SL languages can capture a large portion of phonological well-formedness conditions, there are numerous examples of patterns that require increased complexity. For example, **harmony with a blocking effect** cannot be captured using SP grammars because they will "miss" a blocker, and cannot be encoded via SL grammars because they cannot be used for long-distance processes.

## Tier-based strictly local languages

**Tier-based strictly local (TSL)** grammars operate just like the strictly local ones, but they have the power to _ignore_ a certain set of symbols completely. The set of symbols that are not ignored are called **tier** symbols, and the ones that do not matter for the well-formedness of strings are the **non-tier** ones [(Heinz et al. 2011)](https://pdfs.semanticscholar.org/b934/bfcc962f65e19ae139426668e8f8054e5616.pdf).

Assume that we have the following sets of tier and non-tier symbols.

    tier = [l, r]
    non_tier = [c, d]
    
Non-tiers symbols are ignored when the strings are being evaluated by TSL grammars, so the alphabets `tier` and `non_tier` define the following mapping:

  * <b>l</b>cc<b>r</b>dc<b>l</b>cddc<b>rl</b>c $\Rightarrow$ <b>lrlrl</b>
  * <b>rl</b>dcd<b>r</b>cc<b>l</b>dcd<b>r</b>d<b>l</b> $\Rightarrow$ <b>rlrlrl</b>
  * cdcddcdcdcdc $\Rightarrow \epsilon$

The strings on the right-hand side are called _tier images_ of the original strings because they exclude all non-tier symbols. Then the TSL grammars can be defined as _SL grammars that operate on a tier._

Continuing the example above, let's prohibit "l" following "l" unless "r" intervenes, and also ban "r" following "r" unless "l" intervenes (it yields a toy Latin dissimilation pattern). Over the `tier`, $G_{TSL_{neg}} = \{ll, rr\}$ expresses this rule.

Intuitively, TSL grammars make non-local dependencies local by evaluating only tier images of strings.

**Latin liquid dissimilation**

In Latin, liquids tend to alternate: if the final liquid of the stem is "l", the adjectival affix is realized as "aris". And vice versa, if the final liquid is "r", the choice of the affix is "alis". Consider the examples below.

  * mi<b>l</b>ita<b>r</b>is \~ <*>mi<b>l</b>ita<b>l</b>is _"military"_
  * f<b>l</b>o<b>r</b>a<b>l</b>is \~ <*>f<b>l</b>o<b>r</b>a<b>r</b>is _"floral"_
  * p<b>l</b>u<b>r</b>a<b>l</b>is \~ <*>p<b>l</b>u<b>r</b>a<b>r</b>is _"plural"_
  
This pattern is _not SP_ because SP grammars cannot exhibit the blocking effect, and it is _not SL_ either due to its long-distance nature.


```python
lat_dissim = TSL()
```

### Attributes of TSL grammars
  * `polar` ("p" or "n") is the polarity of the grammar, the default value is "p";
  * `alphabet` (list) is the set of symbols that the grammar uses;
  * `grammar` (list of tuples) is the list of allowed or prohibited substrings of the language;
  * `k` (int) is the size of the locality window of the grammar, by default, it is $2$;
  * `data` (list of string) is the learning sample;
  * `edges` (list of two characters) are the delimiters used by the grammar, the default value is ">" and "<";
  * `fsm` (FSM object) is the finite state device that corresponds to the grammar;
  * `tier` (list) is the list of the tier symbols.
  
### Methods defined for TSL grammars
  * `check_polarity()` and `switch_polarity()` display and change the polarity of the grammar;
  * `learn()` detects tier symbols and learns the tier grammar;
  * `tier_image(string)` returns the tier image of a given string;
  * `scan(string)` tells if a given string is well-formed with respect to the learned grammar;
  * `extract_alphabet()` collects alphabet based on the data or grammar;
  * `generate_sample(n, repeat)` generates $n$ strings based on the given grammar; by default, `repeat` is set to False, and repetitions of the generated strings are not allowed, but this parameter can be set to True;
  * `fsmize()` creates the corresponding FSA;
  * `clean_grammar()` removes useless $k$-grams from the grammar.

### Learning liquid dissimilation

Assume the toy Latin dissimilation dataset, where we mask every non-liquid as "c".


```python
lat_dissim.data = ["ccc", "lccrcccclcr", "lrl", "rcclc"]
```

**Extracting alphabet**

We don't need to explicitly provide the alphabet. Instead, it can be extracted from the data using the `extract_alphabet()` method.


```python
lat_dissim.extract_alphabet()
print("Alphabet:", lat_dissim.alphabet)
```

**Learning the tier and the grammar**

After the alphabet is extracted and the training sample is provided, we can learn the dependency.


```python
lat_dissim.learn()
print('Tier:   ', lat_dissim.tier)
print('Grammar:', lat_dissim.grammar)
```

**Switching polarity**

By-default, the grammars are positive, but this pattern is more clear when represented as a restriction. We can convert the positive grammar to negative using the `switch_polarity()` method.


```python
print("Initial polarity of the grammar:", lat_dissim.check_polarity(), "\n")
lat_dissim.switch_polarity()
print("New polarity of the grammar:", lat_dissim.check_polarity())
print("New grammar:", lat_dissim.grammar)
```

### Learning stress culminativity

We can learn a negative grammar directly as well. For example, let us learn a pattern like this:

    aaabaaaa, baaaa, aaaaaba, aaaaaab, ...
    <*>aababaaa, <*>baaaababb, <*>aaaa, ...
    
In simple words, the desired pattern is _a single "b" must be present in a string_. Translating it to a pattern relevant to linguistics would give us _stress culminativity_.


```python
stress = TSL(polar="n")
stress.data = ["aaabaaaa", "baaaa", "aaaaaba", "aaaaaab"]
stress.extract_alphabet()
stress.learn()

print("Tier:    ", stress.tier)
print("Grammar: ", stress.grammar)
```

The learned negative TSL grammar prohibits an empty tier (stress must be present in a word) and prohibits a tier where there is more than a single stress.

**Generating sample**

Data sample generation is also available for the class of TSL languages. Repetition of the same items within the dataset can be allowed or prohibited by changing the parameter `repeat`.


```python
print(stress.generate_sample(n=10, repeat=True))
```


```python
print(stress.generate_sample(n=10, repeat=False))
```

The implemented learning algorithm for $k$-TSL languages is designed by [McMullin and Jardine (2017)](https://adamjardine.net/files/jardinemcmullin2016tslk.pdf), which is based on [Jardine and Heinz (2016)](http://jeffreyheinz.net/papers/Jardine-Heinz-2016-LTSLL.pdf).

However, there are some phonological processes that require more power than TSL. Some languages have more than just a single long-distance assimilation: for example, separate vowel and consonantal harmonies. In this case, one tier is not enough: putting both vowels and consonants on a single tier will create the desired locality neither among vowels nor among consonants. For cases like this, a subregular class of _multiple tier-based strictly local languages_ is especially useful.

## Multiple tier-based strictly local languages

There are numerous examples from the typological literature that show that there are phonological patterns complexity of which is beyond the power of TSL languages. The example could be any pattern where several long-distance dependencies affect different sets of elements, see [McMullin (2016)](https://www.dropbox.com/s/txmk4efif9f5bvb/McMullin_Dissertation_UBC.pdf?dl=0) and [Aksënova and Deshmukh (2018)](https://www.aclweb.org/anthology/W18-0307.pdf) for examples and discussions of those patterns.


**Two features spread, only one of them can be blocked**

The first example comes from Imdlawn Tashlhiyt [(Hansson 2010)](http://homes.chass.utoronto.ca/~cla-acl/actes2010/CLA2010_Hansson.pdf). Sibilants regressively agree in voicing and anteriority. 

  * <b>s</b>-a<b>s:</b>twa _CAUS-settle_
  * <b>S</b>-fia<b>S</b>r _CAUS-be.full.of.straw_
  * <b>z</b>-bru<b>z:</b>a _CAUS-crumble_
  * <b>Z</b>-m:<b>Z</b>dawl _CAUS-stumble_

However, while voicing harmony can be blocked by voiceless obstruents, they are transparent for the anteriority agreement.

  * <b>s</b>-m<b>X</b>a<b>z</b>aj _CAUS-loathe.each.other_
  * <b>S</b>-<b>q</b>u<b>Z:</b>i _CAUS-be.dislocated_

The blockers need to be projected in order to capture the voicing harmony, however, having those blockers on the tier would make sibilants non-adjacent anymore, and therefore would cause problems for the anteriority harmony.


**Vowel harmony and consonant harmony**

In Bukusu, vowels agree in height, and a liquid "l" assimilates to "r" if followed by "r" somewhere further in the word [(Odden 1994)](https://www.jstor.org/stable/415830?seq=1#metadata_info_tab_contents).

  * <b>r</b><i>ee</i>b-<i>e</i><b>r</b>- _ask-APPL_
  * <b>l</b><i>i</i>m-<i>i</i><b>l</b>- _cultivate-APPL_
  * <b>r</b><i>u</i>m-<i>i</i><b>r</b>- _send-APPL_
  
The tier containing both vowels and liquids would not capture this picture. Intervening vowels would make the liquid spreading non-local over the tier, and intervening liquids would cause vowels to be potentially far away from each other over the tier.


**Multiple tier-based strictly local** grammars are conjunction of multiple TSL grammars: they consist of several tiers, and restrictions defined for every one of those tiers. For example, consider the following toy example.


    Good strings: aaabbabba, oppopooo, aapapapp, obooboboboobbb, ...
    Bad strings:  <*>aabaoob, <*>paabab, <*>obabooo, ...
    Generalization: if a string contains "a", it cannot contain "o", and vice versa;
                    if a string contains "p", it cannot contain "b", and vice versa.
                    
Two tiers are required to encode this pattern: a tier of vowels ("o" and "a"), and a tier of consonants ("p" and "b"). This restriction can be expressed via the following MTSL grammar:

$G_{MTSL_{neg}} = \{
                      T_1 = [a, o], G_1 = [ao, oa];
                      T_2 = [b, p], G_2 = [pb, bp]
                   \}$
    

### Learning "independent" vowel and consonant harmonies



```python
data = ['aabbaabb', 'abab', 'aabbab', 'abaabb', 'aabaab', 'abbabb', 'ooppoopp',
        'opop', 'ooppop', 'opoopp', 'oopoop', 'oppopp', 'aappaapp', 'apap',
        'aappap', 'apaapp', 'aapaap', 'appapp', 'oobboobb', 'obob', 'oobbob',
        'oboobb', 'ooboob', 'obbobb', 'aabb', 'ab', 'aab', 'abb', 'oopp', 'op',
        'oop', 'opp', 'oobb', 'ob', 'oob', 'obb', 'aapp', 'ap', 'aap', 'app',
        'aaa', 'ooo', 'bbb', 'ppp', 'a', 'o', 'b', 'p', '']
```

The first step is to initialize the MTSL object.


```python
harmony = MTSL()
```

### Attributes of MTSL grammars
  * `polar` ("p" or "n") is the polarity of the grammar, where "p" is the default value;
  * `alphabet` (list) is the set of symbols that the grammar uses;
  * `grammar` (dictionary) is a dictionary, where the keys (tuple) are the tier alphabet, and the values (lists) are the restrictions imposed on those tiers;
  * `k` (int) is the size of the locality window of the grammar, by default, it is $2$;
  * `data` (list of string) is the learning sample;
  * `edges` (list of two characters) are the delimiters used by the grammar, the default value is ">" and "<".
  
### Methods defined for MTSL grammars
  * `check_polarity()` and `switch_polarity()` display and change the polarity of the grammar;
  * `learn()` detects the tier symbols and learns the tier grammar;
  * `scan(string)` tells if a given string is well-formed with respect to a learned grammar;
  * `extract_alphabet()` collects the alphabet based on the data and grammar.

**Extracting alphabet and learning the grammar**

Now we can initialize the `data` and `alphabet` attributes of the MTSL class, and apply the `learn` method to learn the tiers and the grammars that correspond to them.


```python
harmony.data = data
harmony.extract_alphabet()
harmony.learn()
```

The value of the attribute `grammar` is represented in the following way:

    G = {
            tier_1 (tuple): tier_1_restrictions (list),
            tier_2 (tuple): tier_2_restrictions (list),
                ...
            tier_n (tuple): tier_n_restrictions (list)
        }


```python
for i in harmony.grammar:
    print("Tier:", i)
    print("Restrictions;", harmony.grammar[i], "\n")
```

**Switching polarity**

The grammar that is learned by default is positive and is pretty verbose, and can be easily converted to negative by appying the `switch_polarity` method.


```python
print("Old polarity:", harmony.check_polarity())
harmony.switch_polarity()
print("New polarity:", harmony.check_polarity(), "\n")

for i in harmony.grammar:
    print("Tier:", i)
    print("Restrictions;", harmony.grammar[i], "\n")
```

The learning algorithm for $2$-MTSL languages is designed by [McMullin et al. (2019)](https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1079&context=scil).


**Scanning strings**

As before, the `scan` method tells if the given string is well-formed with respect to the learned grammar.


```python
good = ["apapappa", "appap", "popo", "bbbooo"]
bad = ["aoap", "popppa", "pabp", "popoa"]

for s in good:
    print("String", s, "is in L(G):", harmony.scan(s))
print()
for s in bad:
    print("String", s, "is in L(G):", harmony.scan(s))
```

**The current state of the MTSL-related research**

We are currently doing the theoretical work of extending the learning algorithm for MTSL languages from capturing $2$-local dependencies to $n$. Therefore this module of the toolkit will be updated as the theoretical work on this language class progresses.

## Future work

Formal languages and corresponding FSMs map strings to truth values. They answer the question **"Is this string well-formed according to the given grammar?"** This question helps to define the well-formedness conditions for _phonotactics_.

However, to capture _phonological processes_, we need to also ask
the question **"What string will be the output if we process the input string according to the given mapping?"** And indeed, subregular mappings and finite-state transductions map strings to strings.

<img src="tutorial/images/scheme.png" width="400">

Therefore the next steps of the development of _SigmaPie_ include the implementation of transducers and different transduction learning algorithms, such as:
  * Onward Subsequential Transducer Inference Algorithm (_OSTIA_) by [Oncina, Garcia and Vidal (1993)](https://pdfs.semanticscholar.org/9058/01c8e75daacb27d70ccc3c0b587411b6d213.pdf) and [de la Higuera (2014)](https://www.cambridge.org/core/books/grammatical-inference/CEEB229AC5A80DFC6436D860AC79434F);
  * Input Strictly Local Function Learning Algorithm (_ISLFLA_) by [Chandlee, Eyraud and Heinz (2014)](https://hal.archives-ouvertes.fr/hal-01193047/document);
  * Output Strictly Local Function Inference Algorithm (_OSLFIA_)by [Chandlee, Eyraud and Heinz (2015)](https://www.aclweb.org/anthology/W15-2310.pdf)
  
... and others.

**Acknowledgments** 

I am very grateful to [_Thomas Graf_](https://thomasgraf.net/), [_Jeffrey Heinz_](http://jeffreyheinz.net/), [_Aniello De Santo_](https://aniellodesanto.github.io/about/) and Ayla Karakas whose input on different parts of this project was extremely helpful.