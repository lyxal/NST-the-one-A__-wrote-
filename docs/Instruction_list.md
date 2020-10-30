Empty rows are undefined instructions.
|Instruction|Arity|Description|
|:-----------:|-----|-----------|
|<code>¤</code>|?| |
|<code>½</code>|?| |
|<code>↕</code>|?| |
|<code>↑</code>|?|
|<code>↓</code>|?||
|<code>↔</code>|?||
|<code>←</code>|?||
|<code>→</code>|?||
|<code>∟</code>|?||
|<code>¦</code>|1|Returns the cardinality (i.e. the length) of the list.|
|<code>\ </code>|?||
|<code>¡</code>|?||
|<code>¿</code>|?||
|<code>‼</code>|?||
|<code>…</code>|?||
|<code>‰</code>|?||
|<code>†</code>|?||
|<code>‡</code>|?||
|<code>√</code>|?||
|<code>≤</code>|?||
|<code>≥</code>|?||
|<code>±</code>|1|Specify that the operand can be positive or negative. (1 -> `[1, -1]`; `[1,2]` -> `[-1, 1, -2, 2]`)|
|<code>∂</code>|?||
|<code>∫</code>|?||
|<code>∞</code>|?||
|<code>≈</code>|?||
|<code>≠</code>|?||
|<code>≡</code>|?||
|<code>⌐</code>|?||
|<code>¬</code>|?||
|<code>÷</code>|?||
|<code>×</code>|2|Lazy-evaluating cartesian product between two operands. E.g. `[1,2] × [3,4]` = `[[1,3],[2,3],[1,4],[2,4]]`|
|<code> </code>|?||
|<code>!</code>|?||
|<code>"</code>|?|String delimiter: `"` begins or ends a string. The preceding quote can be omitted. E.g. `"Test"`; `Test2"`|
|<code>#</code>|?||
|<code>$</code>|?||
|<code>%</code>|2|Modulo operator, vectorizes.|
|<code>&</code>|?||
|<code>'</code>|?||
|<code>(</code>|?||
|<code>)</code>|?||
|<code>*</code>|2|Push a * b, vectorizes.|
|<code>+</code>|2|Push a + b, vectorizes.|
|<code>,</code>|1|Pop an item off the stack. Treat the rest of the code as the body of the filter. Keep all items which make the expression true. Lazy-evaluating.|
|<code>-</code>|2|Push a - b, vectorizes.|
|<code>.</code>|?||
|<code>/</code>|?||
|<code>0</code>|0|Completes a number.|
|<code>1</code>|0|Completes a number.|
|<code>2</code>|0|Completes a number.|
|<code>3</code>|0|Completes a number.|
|<code>4</code>|0|Completes a number.|
|<code>5</code>|0|Completes a number.|
|<code>6</code>|0|Completes a number.|
|<code>7</code>|0|Completes a number.|
|<code>8</code>|0|Completes a number.|
|<code>9</code>|0|Completes a number.|
|<code>:</code>|?||
|<code>;</code>|?||
|<code><</code>|?||
|<code>=</code>|2|Checks if two operands are equal. Vectorizes.|
|<code>></code>|?||
|<code>?</code>|?||
|<code>@</code>|?||
|<code>A</code>|?||
|<code>B</code>|?||
|<code>C</code>|?||
|<code>D</code>|?||
|<code>E</code>|?||
|<code>F</code>|?||
|<code>G</code>|?||
|<code>H</code>|?||
|<code>I</code>|?||
|<code>J</code>|?||
|<code>K</code>|?||
|<code>L</code>|?||
|<code>M</code>|?||
|<code>N</code>|0|The "set" of natural numbers, starting from 0. `[0, 1, 2, 3, ...]`|
|<code>O</code>|?||
|<code>P</code>|?||
|<code>Q</code>|0|The "set" of all rational numbers. `[0/1, 1/1, 2/1, ... 0/2, 1/2, 2/2, ...]`|
|<code>R</code>|?||
|<code>S</code>|?||
|<code>T</code>|?||
|<code>U</code>|?||
|<code>V</code>|?||
|<code>W</code>|?||
|<code>X</code>|?||
|<code>Y</code>|?||
|<code>Z</code>|0|The set of all integers. `[0, -1, 1, -2, 2, -3, 3, -4, 4, ...]`. It's possible to generate this set via `N±`.|
|<code>[</code>|?||
|<code>\\</code>|?||
|<code>]</code>|?||
|<code>^</code>|2|Cartesian power. Cartesian product (i.e. execute the `×` instruction) the list by itself number-operand times.|
|<code>_</code>|?||
|<code>`</code>|?||
|<code>a</code>|?||
|<code>b</code>|?||
|<code>c</code>|?||
|<code>d</code>|?||
|<code>e</code>|?||
|<code>f</code>|?||
|<code>g</code>|?||
|<code>h</code>|?||
|<code>i</code>|?||
|<code>j</code>|?||
|<code>k</code>|?||
|<code>l</code>|?||
|<code>m</code>|?||
|<code>n</code>|?||
|<code>o</code>|?||
|<code>p</code>|?||
|<code>q</code>|?||
|<code>r</code>|?||
|<code>s</code>|?||
|<code>t</code>|?||
|<code>u</code>|?||
|<code>v</code>|?||
|<code>w</code>|?||
|<code>x</code>|?||
|<code>y</code>|?||
|<code>z</code>|?||
|<code>{</code>|?||
|<code>|</code>|1|Pops an item off the operand. Treat the rest of the code as the body of the map. Lazy-evaluating.|
|<code>}</code>|?||
|<code>~</code>|?||
|<code>·</code>|?||
|<code>₀</code>|?||
|<code>₁</code>|?||
|<code>₂</code>|?||
|<code>₃</code>|?||
|<code>₄</code>|?||
|<code>₅</code>|?||
|<code>₆</code>|?||
|<code>₇</code>|?||
|<code>₈</code>|?||
|<code>₉</code>|?||
|<code>⌈</code>|?||
|<code>⌉</code>|?||
|<code>⌊</code>|?||
|<code>⌋</code>|?||
|<code>Γ</code>|?||
|<code>Δ</code>|?||
|<code>Θ</code>|?||
|<code>Λ</code>|?||
|<code>Ξ</code>|?||
|<code>Π</code>|?||
|<code>Σ</code>|?||
|<code>Φ</code>|?||
|<code>Ψ</code>|?||
|<code>Ω</code>|?||
|<code>α</code>|1|Cyclically take an input from the input list.|
|<code>β</code>|?||
|<code>γ</code>|?||
|<code>δ</code>|?||
|<code>ε</code>|?||
|<code>ζ</code>|?||
|<code>η</code>|?||
|<code>θ</code>|?||
|<code>λ</code>|?||
|<code>μ</code>|?||
|<code>ξ</code>|?||
|<code>π</code>|?||
|<code>ρ</code>|?||
|<code>ς</code>|?||
|<code>σ</code>|?||
|<code>τ</code>|?||
|<code>φ</code>|?||
|<code>χ</code>|?||
|<code>ψ</code>|?||
|<code>ω</code>|?||
|<code>⁰</code>|?|Pushes 0 by itself.|
|<code>¹</code>|?|Pushes 1 by itself.|
|<code>²</code>|?|Pushes 2 by itself.|
|<code>³</code>|?|Pushes 3 by itself.|
|<code>⁴</code>|?|Pushes 4 by itself.|
|<code>⁵</code>|?|Pushes 5 by itself.|
|<code>⁶</code>|?|Pushes 6 by itself.|
|<code>⁷</code>|?|Pushes 7 by itself.|
|<code>⁸</code>|?|Pushes 8 by itself.|
|<code>⁹</code>|?|Pushes 9 by itself.|
|<code>¢</code>|2|Is the left operand NOT an item/instance of the right operand? Equivalent to Set Theory's `∉`|
|<code>£</code>|?||
|<code>€</code>|2|Is the left operand an item/instance of the right operand? (Equivalent to `∈` in the set theory.)|
|<code>¥</code>|?||
|<code>ƒ</code>|?||
|<code>´</code>|?||
|<code>▲</code>|?||
|<code>▼</code>|?||
|<code>►</code>|?||
|<code>◄</code>|?||
|<code>§</code>|2|Like `€`, but with swapped arguments. (Equivalent to `∍` in the set theory.)|
|<code>Ȧ</code>|1|Add the operand by 1,vectorizes.|
|<code>Ḃ</code>|?||
|<code>Ċ</code>|?||
|<code>Ḋ</code>|?||
|<code>Ė</code>|?||
|<code>Ḟ</code>|?||
|<code>Ġ</code>|?||
|<code>Ḣ</code>|?||
|<code>İ</code>|?||
|<code>Ŀ</code>|?||
|<code>Ṁ</code>|?||
|<code>Ṅ</code>|0|The set of all positive numbers, starting at 1: `[1, 2, 3, 4, ...]`|
|<code>Ȯ</code>|?||
|<code>Ṗ</code>|1|Powerset of the operand.|
|<code>Ṙ</code>|?||
|<code>Ṡ</code>|?||
|<code>Ṫ</code>|0|`Ṫ`erminates the looping structure no matter what.|
|<code>Ẇ</code>|?||
|<code>Ẋ</code>|?||
|<code>Ẏ</code>|?||
|<code>Ż</code>|?||
|<code>ȧ</code>|?||
|<code>ḃ</code>|?||
|<code>ċ</code>|?||
|<code>ḋ</code>|?||
|<code>ė</code>|?||
|<code>ḟ</code>|?||
|<code>ġ</code>|?||
|<code>ḣ</code>|?||
|<code>ı</code>|1|The opposite of the filter `,` operator. It performs a logical negation in the condition.|
|<code>ȷ</code>|?||
|<code>ŀ</code>|?||
|<code>ṁ</code>|?||
|<code>ṅ</code>|?||
|<code>ȯ</code>|?||
|<code>ṗ</code>|?||
|<code>ṙ</code>|?||
|<code>ṡ</code>|?||
|<code>ṫ</code>|?||
|<code>ẇ</code>|?||
|<code>ẋ</code>|?||
|<code>ẏ</code>|?||
|<code>ż</code>|?||
|<code>¨</code>|2|Inclusive range between the two operands. Vectorizes.|
|<code>Ä</code>|?||
|<code>Ë</code>|?||
|<code>Ï</code>|?||
|<code>Ö</code>|?||
|<code>Ü</code>|?||
|<code>Ÿ</code>|?||
|<code>Ø</code>|0|The empty set. `[]`|
|<code>ä</code>|?||
|<code>ë</code>|?||
|<code>ï</code>|?||
|<code>ö</code>|?||
|<code>ü</code>|?||
|<code>ÿ</code>|?||
|<code>ø</code>|?||
|<code>◊</code>|?||
|<code>□</code>|?||
|<code>¶</code>|?||
|<code>«</code>|?||
|<code>»</code>|?||
