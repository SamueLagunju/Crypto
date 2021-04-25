import{o as n,c as s,d as a}from"./app.50dbb70a.js";const t='{"title":"","description":"","frontmatter":{},"relativePath":"projects/Crypto/crypto/helpers.md","lastUpdated":1619381236265}',p={},o=a('<p>PROJECT : Crypto FILE : <a href="http://helpers.py" target="_blank" rel="noopener noreferrer">helpers.py</a> PROGRAMMER : Samuel Lagunju DATE : 2020-08-07 DESCRIPTION : The functions in this file are miscellaneous</p><div class="language-python"><pre><code>\n<span class="token keyword">import</span> platform\n<span class="token keyword">import</span> argparse\n<span class="token keyword">import</span> sys\n\n\n\n</code></pre></div><p>FUNCTION: osCheck() DESCRIPTION: Checks which operating system its being run on PARAMETERS: N/A RETURNS: plt - Name of platform that was detected SYS_ERROR - Raised an error if it cannot detect an OS</p><div class="language-python"><pre><code>\n\n\n</code></pre></div><div class="language-python"><pre><code><span class="token keyword">def</span> <span class="token function">os_checker</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>\n\n</code></pre></div><p>OS Check</p><div class="language-python"><pre><code>    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">&quot;Verifying OS...&quot;</span><span class="token punctuation">)</span>\n    plt <span class="token operator">=</span> platform<span class="token punctuation">.</span>system<span class="token punctuation">(</span><span class="token punctuation">)</span>\n    <span class="token keyword">if</span> plt <span class="token operator">==</span> <span class="token string">&quot;Windows&quot;</span><span class="token punctuation">:</span>\n        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">&quot;Windows OS detected&quot;</span><span class="token punctuation">)</span>\n    <span class="token keyword">elif</span> plt <span class="token operator">==</span> <span class="token string">&quot;Linux&quot;</span><span class="token punctuation">:</span>\n        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">&quot;Linux OS detected&quot;</span><span class="token punctuation">)</span>\n    <span class="token keyword">elif</span> plt <span class="token operator">==</span> <span class="token string">&quot;Darwin&quot;</span><span class="token punctuation">:</span>\n        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">&quot;Mac OS detected&quot;</span><span class="token punctuation">)</span>\n    <span class="token keyword">else</span><span class="token punctuation">:</span>\n        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">&quot;Unidentified system&quot;</span><span class="token punctuation">)</span>\n        <span class="token keyword">raise</span> SystemError\n    <span class="token keyword">return</span> plt\n\n\n\n</code></pre></div><p>FUNCTION : arg_parser DESCRIPTION : This function parses arguments inputted by the user and returns it as a list PARAMETERS : sys.argv[1:] - A list of strings representing the arguments (as separated by spaces) on the command-line RETURNS : options - A parser object</p><div class="language-python"><pre><code><span class="token keyword">def</span> <span class="token function">arg_parser</span><span class="token punctuation">(</span>args<span class="token operator">=</span>sys<span class="token punctuation">.</span>argv<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">:</span>\n    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">&quot;Parsing Command line Argument...&quot;</span><span class="token punctuation">)</span>\n\n    parser <span class="token operator">=</span> argparse<span class="token punctuation">.</span>ArgumentParser<span class="token punctuation">(</span>\n        prog<span class="token operator">=</span>sys<span class="token punctuation">.</span>argv<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">,</span> description<span class="token operator">=</span><span class="token string">&quot;An encrypting / decrypting utility for Linux.\\n&quot;</span>\n    <span class="token punctuation">)</span>\n    parser<span class="token punctuation">.</span>add_argument<span class="token punctuation">(</span>\n        <span class="token string">&quot;-e&quot;</span><span class="token punctuation">,</span>\n        <span class="token string">&quot;--encrypt&quot;</span><span class="token punctuation">,</span>\n        metavar<span class="token operator">=</span><span class="token string">&quot;Encryption file&quot;</span><span class="token punctuation">,</span>\n        action<span class="token operator">=</span><span class="token string">&quot;append&quot;</span><span class="token punctuation">,</span>\n        dest<span class="token operator">=</span><span class="token string">&quot;encrypt_file&quot;</span><span class="token punctuation">,</span>\n        <span class="token builtin">help</span><span class="token operator">=</span><span class="token string">&quot;Produces an encrypted file\\n&quot;</span><span class="token punctuation">,</span>\n    <span class="token punctuation">)</span>\n    parser<span class="token punctuation">.</span>add_argument<span class="token punctuation">(</span>\n        <span class="token string">&quot;-d&quot;</span><span class="token punctuation">,</span>\n        <span class="token string">&quot;--decrypt&quot;</span><span class="token punctuation">,</span>\n        metavar<span class="token operator">=</span><span class="token string">&quot;Decryption file&quot;</span><span class="token punctuation">,</span>\n        action<span class="token operator">=</span><span class="token string">&quot;append&quot;</span><span class="token punctuation">,</span>\n        dest<span class="token operator">=</span><span class="token string">&quot;decrypt_file&quot;</span><span class="token punctuation">,</span>\n        <span class="token builtin">help</span><span class="token operator">=</span><span class="token string">&quot;Produces a decrypted file\\n&quot;</span><span class="token punctuation">,</span>\n    <span class="token punctuation">)</span>\n    parser<span class="token punctuation">.</span>add_argument<span class="token punctuation">(</span>\n        <span class="token string">&quot;Filename&quot;</span><span class="token punctuation">,</span>\n        metavar<span class="token operator">=</span><span class="token string">&quot;File.txt&quot;</span><span class="token punctuation">,</span>\n        nargs<span class="token operator">=</span><span class="token string">&quot;*&quot;</span><span class="token punctuation">,</span>\n        action<span class="token operator">=</span><span class="token string">&quot;append&quot;</span><span class="token punctuation">,</span>\n        <span class="token builtin">help</span><span class="token operator">=</span><span class="token string">&quot;Produces an encrypted file\\n&quot;</span><span class="token punctuation">,</span>\n    <span class="token punctuation">)</span>\n    options <span class="token operator">=</span> parser<span class="token punctuation">.</span>parse_args<span class="token punctuation">(</span>args<span class="token punctuation">)</span>\n    <span class="token keyword">return</span> options\n\n\n</code></pre></div>',9);p.render=function(a,t,p,e,c,u){return n(),s("div",null,[o])};export default p;export{t as __pageData};
