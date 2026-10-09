|travis-badge| |gitter-badge|

.. |travis-badge| image:: https://travis-ci.org/jonashaag/klaus.svg?branch=master
    :target: https://travis-ci.org/jonashaag/klaus

.. |gitter-badge| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/jonashaag/klaus
   :target: https://gitter.im/jonashaag/klaus?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

klaus: a simple, easy-to-set-up Git web viewer that Just Works™.
================================================================

(If it doesn't Just Work for you, please file a bug.)

* Super easy to set up -- no configuration required
* Syntax highlighting
* Markdown + RestructuredText rendering support
* Pull + push support (Git Smart HTTP)
* Code navigation using Exuberant ctags

:Demo: https://github.com/jonashaag/klaus/wiki/Sites-using-klaus
:On PyPI: http://pypi.python.org/pypi/klaus/
:Wiki: https://github.com/jonashaag/klaus/wiki
:License: ISC (BSD)


Running with Docker
--------------------

The easiest way to get started. We maintain a Docker image that has syntax highlighting, Markdown rendering, code navigation, etc. pre-configured::

   docker run -v /path/to/your/repos:/repos \
              -p 7777:80 \
              -it ghcr.io/superderker/superklaus:main \
              klaus --host 0.0.0.0 --port 80 /repos/repo1 /repos/repo2 ...

(Replace ``/path/to/your/repos`` with the folder that contains your Git repositories on the Docker host. You can also pass in multiple ``-v`` arguments if your repos are in multiple folders on the host.)

Go to http://localhost:7777 on the Docker host et voilà!


|img1|_ |img2|_ |img3|_

.. |img1| image:: https://i.imgur.com/2XhZIgw.png
.. |img2| image:: https://i.imgur.com/6LjC8Cl.png
.. |img3| image:: https://i.imgur.com/EYJdQwv.png

.. _img1: https://i.imgur.com/MV3uFvw.png
.. _img2: https://i.imgur.com/9HEZ3ro.png
.. _img3: https://i.imgur.com/kx2HaTq.png
