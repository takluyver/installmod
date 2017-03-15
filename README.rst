Prototype of installing modules from inside Python, using *pip* or *conda* 
as appropriate.

Usage::
  
  from install import install
  install('pandas')

At the moment, this assumes that the package has the same name in the two
packaging systems. This is not generally true, but it's true often enough to be
useful in many cases. I am also interested in `indexing pacakges
<https://github.com/takluyver/wheeldex>`__ to extract the names of importable
modules, which could provide a shared namespace for a tool like this.
