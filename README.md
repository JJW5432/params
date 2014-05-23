Bparams
======
Returns a dictionary of key value pairs from the query string. Automatically converts to ints and floats.

Basic Usage
-----------

```python
#QUERY_STRING = "length=5&name=Jake%20Waksbaum"
query = get_params()
print query #=> {'length':5, 'name':'Jake Waksbaum'}
```

Advanced Usage
-------------

```python
get_params(repl={}, allow={}, double=False, error='Error: <param> supplied more than once, using the leftmost value.', debug=False)
```

###Replace
Pass a dictionary of variable names that should be replaced as the repl parameter
```python
#QUERY_STRING = 'l=5'
>>> query = get_params(repl = {'l':'length'})
>>> print query #=> {'length':5}
```

###Filter Parameters and Types
Pass a dictionary in which the keys are the only key in the QUERY_STRING that will be included in the dictionary and whose values are either a type or an array of allowed types. If any type is acceptable, use None as the type.
```python
#QUERY_STRING = 'length=5&width=8.8&name=6&foo=bar'
>>> query = get_params(allow={'length':[int, float], 'width':[int, float], 'name':str]
>>> print query #=> {'length':5, 'width':8.8}

###Print Error on Multiple of Same Variable
If double is True, it will print the double_error for each variable that there is more than one of in the query string.
**Note:** this takes place *after* replace.
In the double_error, <param> will be replaced with the parameter name.
```python
#QUERY_STRING = 'length:5&l:3'
>>> query = get_params(repl={'l':'length}, double=True, double_error:'There is a problem with <param>') 
# will automatically print "There is a problem with length"
```

###Debug
If Debug is True, each variable and its value is printed.