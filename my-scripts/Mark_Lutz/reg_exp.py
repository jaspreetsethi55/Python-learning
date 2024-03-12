'''
#####re.match is anchored at the beginning of the string. That has nothing to do with newlines, so it is not the same as using ^ in the pattern.

As the re.match documentation says:

If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding MatchObject instance. Return None if the string does not match the pattern; note that this is different from a zero-length match.

Note: If you want to locate a match anywhere in string, use search() instead.


####re.search searches the entire string, as the documentation says:
--use re.search() to search for a particular pattern inside a string.
--returns an object called MatchObject that stores different groups of data.This is because there might be matches inside other matches, and re.search() returns every possible result

Scan through string looking for a location where the regular expression pattern produces a match, and return a corresponding MatchObject instance. Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

So if you need to match at the beginning of the string, or to match the entire string use match. It is faster. Otherwise use search.

The documentation has a specific section for match vs. search that also covers multiline strings:

Python offers two different primitive operations based on regular expressions: match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).

Note that match may differ from search even when using a regular expression beginning with '^': '^' matches only at the start of the string, or in  MULTILINE mode also immediately following a newline. The “match” operation succeeds only if the pattern matches at the start of the string regardless of mode, or at the starting position given by the optional pos argument regardless of whether a newline precedes it.

Now, enough talk. Time to see some example code:
'''
# example code:
string_with_newlines = """something
someotherthing"""

import re

##########re.match##############
match = re.match('some', string_with_newlines) # matches
print(match) #<_sre.SRE_Match object; span=(0, 4), match='some'>

match = re.match('ome', string_with_newlines) # won't match
print(match) #None - Since re.match matches from starting from string and string doesn't starts from 'ome'

match = re.match('someother', string_with_newlines) # won't match
print(match) #None

match = re.match('^someother', string_with_newlines, re.MULTILINE) # also won't match
print(match) #None


###############re.search##########
search = re.search('someother', string_with_newlines) # finds something
print(search) #<_sre.SRE_Match object; span=(10, 19), match='someother'>

search = re.search('^someother', string_with_newlines) #It will treat the string as single line, we need to use flag re.MULTILINE to tell it to treat having \n as multiple lines
print(search) #None

search = re.search('^someother', string_with_newlines, re.MULTILINE) #finds something - using flag re.MULTILINE
print(search) #<_sre.SRE_Match object; span=(10, 19), match='someother'>


########Compiling regex########
##We can compile a pattern and store it in variable and then use it in any string
m = re.compile('(th)i(ng)$', re.MULTILINE)

print(m.match(string_with_newlines)) # no match

#passing positions to match after compile
print(m.match(string_with_newlines, pos=4)) # matches

print(m.search(string_with_newlines)) # also matches


####group and groups(Capturing)########
#group() returns the matching text if no matching text then it returns error. It has no relation with capturing in regex. We can use it on re.search and re.match results
#groups() only returns the captured and matched data within brackets() i.e. it works on capturing/grouping concept. It returns tuple of matched data if matched otherwise empty tuple

my_str = 'this is45 55 &311 0245'
match = re.search(r'\d\d',my_str)
print(match) #<_sre.SRE_Match object; span=(7, 9), match='45'>
print(match.group()) #45

match = re.search(r'\d(\d)',my_str)
print(match) #<_sre.SRE_Match object; span=(7, 9), match='45'>
print(match.group()) #45
print(match.groups()) #(5,)
print(match.groups()[0]) #5

print(re.search(r'\d(\d)',my_str).group()) #45 #will return error if not matched
print(re.search(r'\d(\d)',my_str).groups()) #(5,) #will return empty tuple of not matched

########findall######
#first argument of re.findall() is the regular expression that you want to match, and the second argument is the string to test.
#if no match is found, then .findall() returns an empty list
#Pattern matching is case sensitive. If you want to match this pattern regardless of the case, then you can pass a third argument with the value re.IGNORECASE:

match = re.findall("ab*c", "abcd")
#['abc']

match = re.findall("ab*c", "acc")
#['ac']

match = re.findall("ab*c", "abcac")
#['abc', 'ac']

match = re.findall("ab*c", "abdc")
#[]

match = re.findall("ab*c", "ABC")
#[]

match = re.findall("ab*c", "ABC", re.IGNORECASE)
#['ABC']

match = re.findall(r'\d\d',my_str)
print(match)


######sub#####
# re.sub(), which is short for substitute, allows you to replace the text in a string that matches a regular expression with new text. It behaves sort of like the .replace() string method.
#The arguments passed to re.sub() are the regular expression, followed by the replacement text, followed by the string

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)
#'Everything is ELEPHANTS.'

#re.sub() uses the regular expression "<.*>" to find and replace everything between the first < and the last >, which spans from the beginning of <replaced> to the end of <tags>. This is because Python’s regular expressions are greedy, meaning they try to find the longest possible match when characters like * are used.

#Alternatively, you can use the non-greedy matching pattern *?, which works the same way as * except that it matches the shortest possible string of text
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)
#"Everything is ELEPHANTS if it's in ELEPHANTS."


