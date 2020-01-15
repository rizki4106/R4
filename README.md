<h1>R4</h1>
<p>Install command</p>
<pre>pip install R4</pre>
<p><b>R4</b> is a package python for encrypt your important data. This package can encrypt your data or decrypt your data perfecly. See the example below</p>
<br/>
<pre>
//## main.py
from R4 import *

text = input(str("What is your name : ")) ## i fill this "rizki maulana"
print(encode(text))

// result R418HR42RR430ZAR410PR42RR459CR413MR40ZR421ER412NR40ZR414LR40Z
</pre>

<p>To decrypt you can do that easly let's see this</p>
<pre>
from R4 import *

text = input(str("What is your name : ")) ## i fill this "rizki maulana"
encode = encode(text)
print(decode(encode))

</pre>