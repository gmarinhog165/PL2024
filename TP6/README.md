```
T = {'+', '-', '*', '/', '(', ')', '=', '!', '?', ID, NUMBER, NL}

    N = {Z, code, ops, op, expr, prio2, term, prio1, factor}

    Z       -> code             Lookahead = {'!', '?', ID}

    code    -> op ops        Lookahead = {'!', '?', ID} U {$}
            |

    ops  -> NL code          Lookahead = NL U {$}
            |
    
    op      -> '!' expr         Lookahead = {'!'}
            | '?' ID            Lookahead = {'?'}
            | ID '=' expr       Lookahead = {'ID'}

    expr    -> term prio2      Lookahead = {NUMBER, ID, '('}
    
    prio2  -> '+' expr         Lookahead = {'+'}
            | '-' expr          Lookahead = {'-'}
            |                 Lookahead = {$, NL, ')'}

    term    -> factor prio1    Lookahead = {NUMBER, ID, '('}
    
    prio1  -> '*' term         Lookahead = {'*'}
            | '/' term          Lookahead = {'/'}
            |                 Lookahead = {'+', '-', $, NL, ')'}
    
    factor  -> NUMBER           Lookahead = {NUMBER}
            | ID                Lookahead = {ID}
            | '(' expr ')'      Lookahead = {'('}
    
```