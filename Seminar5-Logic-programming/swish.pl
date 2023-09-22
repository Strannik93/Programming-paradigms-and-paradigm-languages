/* List - список, R - результат, F - текущее значение */
/* H - голова списка, T - хвост списка, I - начальное значение */
/* F2 - обновленный результат */

sum(List,R) :-
    sum(List,0,R).

sum([],F,F).
sum([H|T],F,R) :-
    F2 is F+H,
    sum(T,F2,R).