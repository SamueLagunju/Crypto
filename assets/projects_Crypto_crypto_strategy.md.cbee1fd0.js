import{o as n,c as a,a as s}from"./app.5202dc78.js";const t='{"title":"","description":"","frontmatter":{},"relativePath":"projects/Crypto/crypto/strategy.md","lastUpdated":1617051445748}',p={},e=s('<p>PROJECT : Crypto FILE : <a href="http://strategy.py" target="_blank" rel="noopener noreferrer">strategy.py</a> PROGRAMMER : Samuel Lagunju DATE : 2020-08-20 DESCRIPTION : The functions in this file are used to support the strategy interface interface</p><div class="language-python"><pre><code>\n\n<span class="token keyword">import</span> abc\n\n\n\n</code></pre></div><p>NAME : Strategy PURPOSE : The Strategy class declares operations common to all supported versions of some algorithm.</p><div class="language-python"><pre><code><span class="token keyword">class</span> <span class="token class-name">Strategy</span><span class="token punctuation">:</span>\n\n</code></pre></div><div class="language-python"><pre><code>    <span class="token decorator annotation punctuation">@abc<span class="token punctuation">.</span>abstractmethod</span>\n    <span class="token keyword">def</span> <span class="token function">encrypt_text</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> input_text<span class="token punctuation">)</span><span class="token punctuation">:</span>\n        <span class="token keyword">pass</span>\n\n    <span class="token decorator annotation punctuation">@abc<span class="token punctuation">.</span>abstractmethod</span>\n    <span class="token keyword">def</span> <span class="token function">decrypt_text</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> cipher_text<span class="token punctuation">)</span><span class="token punctuation">:</span>\n        <span class="token keyword">pass</span>\n\n\n\n</code></pre></div><p>NAME : SeanStrategy PURPOSE : The SeanStrategy class implement the algorithms while following the base strategy interface. The interface makes them interchangeable in the context. Concrete strategy for Sean Clarke&#39;s encryption scheme.</p><div class="language-python"><pre><code><span class="token keyword">class</span> <span class="token class-name">SeanStrategy</span><span class="token punctuation">(</span>Strategy<span class="token punctuation">)</span><span class="token punctuation">:</span>\n\n\n</code></pre></div><p>METHOD : encrypt_text DESCRIPTION : This function translate the ASCII value of the new encrypted character to a 2 digit hexadecimal value. PARAMETERS : plain_text - Text that is about to be encrypted into cipher text RETURNS : cipher_text - 2 digit hexadecimal value</p><div class="language-python"><pre><code>    <span class="token keyword">def</span> <span class="token function">encrypt_text</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> plain_text<span class="token punctuation">)</span><span class="token punctuation">:</span>\n        cipher_text <span class="token operator">=</span> <span class="token string">&quot;&quot;</span>\n\n</code></pre></div><p>Transversing the string using range function</p><div class="language-python"><pre><code>        <span class="token keyword">for</span> pt_char_index <span class="token keyword">in</span> <span class="token builtin">range</span><span class="token punctuation">(</span><span class="token builtin">len</span><span class="token punctuation">(</span>plain_text<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">:</span>\n            <span class="token keyword">if</span> <span class="token string">&quot;\\n&quot;</span> <span class="token keyword">in</span> plain_text<span class="token punctuation">[</span>pt_char_index<span class="token punctuation">]</span><span class="token punctuation">:</span>\n                cipher_text <span class="token operator">+=</span> plain_text<span class="token punctuation">[</span>pt_char_index<span class="token punctuation">]</span>\n            <span class="token keyword">else</span><span class="token punctuation">:</span>\n\n</code></pre></div><p>Returning plain text into integer</p><div class="language-python"><pre><code>                ascii_plain_text <span class="token operator">=</span> <span class="token builtin">ord</span><span class="token punctuation">(</span>plain_text<span class="token punctuation">[</span>pt_char_index<span class="token punctuation">]</span><span class="token punctuation">)</span>\n\n</code></pre></div><p>If the character is a tab (ASCII value 9) it is just TT</p><div class="language-python"><pre><code>                <span class="token keyword">if</span> ascii_plain_text <span class="token operator">==</span> <span class="token number">9</span><span class="token punctuation">:</span>\n                    cipher_text <span class="token operator">+=</span> <span class="token string">&quot;TT&quot;</span>\n\n</code></pre></div><p>Apply encryption scheme</p><div class="language-python"><pre><code>                <span class="token keyword">else</span><span class="token punctuation">:</span>\n\n</code></pre></div><p>Taking the ASCII code for the input character and subtracting a value of 16 from it</p><div class="language-python"><pre><code>                    cipher_char <span class="token operator">=</span> ascii_plain_text <span class="token operator">-</span> <span class="token number">16</span>\n\n</code></pre></div><p>If the resulting outChar value is less than 32, another step must be taken:</p><div class="language-python"><pre><code>                    <span class="token keyword">if</span> cipher_char <span class="token operator">&lt;</span> <span class="token number">32</span><span class="token punctuation">:</span>\n                        cipher_char <span class="token operator">=</span> <span class="token punctuation">(</span>cipher_char <span class="token operator">-</span> <span class="token number">32</span><span class="token punctuation">)</span> <span class="token operator">+</span> <span class="token number">144</span>\n\n</code></pre></div><p>Transforming result to 2 digit hexadecimal value</p><div class="language-python"><pre><code>                    cipher_text <span class="token operator">+=</span> <span class="token builtin">format</span><span class="token punctuation">(</span>cipher_char<span class="token punctuation">,</span> <span class="token string">&quot;X&quot;</span><span class="token punctuation">)</span>\n\n        <span class="token keyword">return</span> cipher_text\n\n\n</code></pre></div><p>METHOD : decrypt_text DESCRIPTION : This function translates a 2 digit hexadecimal value to a decoded ASCII value PARAMETERS : cipher_text - Text that is about to be decrypted into plain text RETURNS : plain_text - ASCII value</p><div class="language-python"><pre><code>    <span class="token keyword">def</span> <span class="token function">decrypt_text</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> cipher_text<span class="token punctuation">)</span><span class="token punctuation">:</span>\n        plain_text <span class="token operator">=</span> <span class="token string">&quot;&quot;</span>\n        n <span class="token operator">=</span> <span class="token number">2</span>\n\n</code></pre></div><p>Parsing the cipher text, line by line</p><div class="language-python"><pre><code>        <span class="token keyword">for</span> cipher_line <span class="token keyword">in</span> cipher_text<span class="token punctuation">.</span>splitlines<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>\n\n</code></pre></div><p>Parsing each line and decrypting the file</p><div class="language-python"><pre><code>            <span class="token keyword">for</span> index <span class="token keyword">in</span> <span class="token builtin">range</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span> <span class="token builtin">len</span><span class="token punctuation">(</span>cipher_line<span class="token punctuation">)</span><span class="token punctuation">,</span> n<span class="token punctuation">)</span><span class="token punctuation">:</span>\n\n</code></pre></div><p>Capturing each pair of characters in the input line</p><div class="language-python"><pre><code>                char_pair <span class="token operator">=</span> cipher_line<span class="token punctuation">[</span>index <span class="token punctuation">:</span> index <span class="token operator">+</span> n<span class="token punctuation">]</span>\n\n</code></pre></div><p>If the pair of characters is the sequence TT it simply transforms into a tab character</p><div class="language-python"><pre><code>                <span class="token keyword">if</span> char_pair <span class="token operator">==</span> <span class="token string">&quot;TT&quot;</span><span class="token punctuation">:</span>\n                    plain_text <span class="token operator">+=</span> <span class="token string">&quot;\\t&quot;</span>\n                <span class="token keyword">else</span><span class="token punctuation">:</span>\n\n</code></pre></div><p>Converting from hex to decimal and adding 16</p><div class="language-python"><pre><code>                    plain_char <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>char_pair<span class="token punctuation">,</span> <span class="token number">16</span><span class="token punctuation">)</span> <span class="token operator">+</span> <span class="token number">16</span>\n\n</code></pre></div><p>If the resulting outChar value is greater than 127, then another step is taken</p><div class="language-python"><pre><code>                    <span class="token keyword">if</span> plain_char <span class="token operator">&gt;</span> <span class="token number">127</span><span class="token punctuation">:</span>\n                        plain_char <span class="token operator">=</span> <span class="token punctuation">(</span>plain_char <span class="token operator">-</span> <span class="token number">144</span><span class="token punctuation">)</span> <span class="token operator">+</span> <span class="token number">32</span>\n                    plain_text <span class="token operator">+=</span> <span class="token builtin">chr</span><span class="token punctuation">(</span>plain_char<span class="token punctuation">)</span>\n\n\n</code></pre></div><p>Adding the new line character back to the line</p><div class="language-python"><pre><code>            plain_text <span class="token operator">+=</span> <span class="token string">&quot;\\n&quot;</span>\n        <span class="token keyword">return</span> plain_text\n\n\n</code></pre></div>',39);p.render=function(s,t,p,o,c,r){return n(),a("div",null,[e])};export default p;export{t as __pageData};
