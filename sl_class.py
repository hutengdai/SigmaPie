#!/bin/python3

"""
   A class of Strictly Local Grammars.
   Copyright (C) 2017  Alena Aksenova
   
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
"""

from typing import TypeVar, Union, Tuple, List
from random import shuffle
from helper import *
from fsm import *
from grammar import *

PosStL = TypeVar('PosStL', bound='PosSL')
NegStL = TypeVar('NegStL', bound='NegSL')

class PosSL(PosGram):
    """ A class for Positive Strictly Local grammars. """

    def __init__(self:PosStL,alphabet:list=[], grammar:List[tuple]=[], k:int=2, data:list=[]) -> None:
        """ Initialize basic attributes """
        super().__init__(alphabet, grammar, k, data)
        self.fsm = None


    def learn(self:PosStL) -> None:
        """ Function for extracting positive SL grammar and alphabet
            from the given data.
        """

        if self.data:
            self.grammar = self.ngramize_data(self.k, self.data)


    def generate_sample(self:PosStL, n:int=10, rep:bool=True) -> None:
        """ Generates a sample of the data of a given size. """
        
        if self.fsm == None:
            self.fsmize()

        data = [self.generate_item() for i in range(n)]
        self.data_sample = data

        # fixme: without repetitions, this f is super slow!
        if rep == False:
            self.data_sample = list(set(self.data_sample))
            while len(self.data_sample) < n:
                self.data_sample += [self.generate_item()]
                self.data_sample = list(set(self.data_sample))


    def generate_item(self:PosStL) -> str:
        """ Generates a sample item """

        more = True
        word = ">"
        while more == True:
            shuffle(self.fsm.transitions)
            for i in self.fsm.transitions:
                # find first appropriate move
                if i[0] == (word[-1],):
                    word += i[1]
                break
            if word[-1] == "<":
                more = False
                
        return word

        
    def fsmize(self:PosStL) -> None:
        """ Function that builds FSM corresponding to the grammar """
        
        if self.grammar:
            fin_state = FiniteStateMachine()
            fin_state.sl_states(self.grammar)
            self.fsm = fin_state
        else:
            raise(IndexError("The grammar is not provided."))


    def clean(self:PosStL) -> None:
        """ Function for removing useless n-grams from the grammar """

        if self.fsm == None:
            self.fsmize()
        self.fsm.trim_fsm()
        self.grammar = self.build_ngrams(self.fsm.transitions)


    def change_polarity(self:PosStL) -> None:
        """ For a grammar with given polarity, returns set of ngrams
            of the opposite polarity.
        """
        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)
        self.__class__ = NegSL


    def annotate_data(self:PosStL, data:str, k:int) -> str:
        return ">"*(k-1) + data.strip() + "<"*(k-1)
        

    def ngramize_data(self:PosStL, k:int, data:list) -> list:
        """ Creates set of k-grams based on the given data. """
        
        grammar:list = []
        for s in data:
            item = self.annotate_data(s, k)
            grammar += self.ngramize_item(item, k)

        return list(set(grammar))


    def ngramize_item(self:PosStL, item:str, k:int) -> list:
        """ N-gramizes a given string """

        ngrams:list = []
        for i in range(len(item)-(k-1)):
            ngrams += [tuple(item[i:i+k])]
                
        return list(set(ngrams))


    def build_ngrams(self:PosStL, transitions:list) -> list:
        """ Generates SL grammar based on the given transitions.
            For the transition ("ab", "c", "bc") gives ngram "abc".
        """
        
        if transitions == []:
            return transitions

        ngrams:list = []
        for i in transitions:
            ngrams.append(i[0] + (i[1],))

        return ngrams


class NegSL(PosSL):
    """ A class for Negative Strictly Local grammars. """

    def __init__(self:NegStL, alphabet:list=[], grammar:List[tuple]=[], k:int=2, data:list=[]) -> None:
        super().__init__(alphabet, grammar, k, data)


    def learn(self:NegStL) -> None:
        """ Function for extracting negative SL grammar and alphabet
            from the given data.
        """
        super().learn()
        if not self.alphabet:
            raise(IndexError("The alphabet is not provided."))
        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)


    def generate_sample(self:NegStL, n:int=10, rep:bool=True) -> None:
        """ Generates a sample of the data of a given size. """

        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)
        super().generate_sample(n, rep)
        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)
        

    def clean(self:NegStL) -> None:
        """ Function for removing useless n-grams from the grammar """

        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)
        super().clean()
        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)


    def fsmize(self:NegStL) -> None:
        """ Function that builds FSM corresponding to the grammar """

        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)
        super().fsmize()
        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)

        
    def change_polarity(self:NegStL) -> None:
        """ For a grammar with given polarity, returns set of ngrams
            of the opposite polarity.
        """
        self.grammar = self.opposite_polarity(self.grammar, self.alphabet, self.k)
        self.__class__ = PosSL
