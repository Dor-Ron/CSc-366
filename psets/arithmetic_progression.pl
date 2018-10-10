% Author: Dor Rondel

% Base case for recursion, list of size two
% No need to declare empty and singleton lists,
% They are false by default this way
seqSameDiffs([X0,X1], Offset) :- Offset is X1 - X0.

% Recursive scenario, len(list) > 2
seqSameDiffs([X0,X1|Tail], Offset) :- 
    seqSameDiffs([X1|Tail], Offset),
    Offset is X1 - X0; % additive sequence
    X1 is X0 - Offset. % subtractive sequence